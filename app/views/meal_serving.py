# app/views/meal_serving.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from app.models import MealServing, InventoryTransaction, ChangeType, Meal, MealIngredient
from app.serializers import MealServingSerializer
from rest_framework.permissions import IsAuthenticated

class ServeMealView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        meal_id = request.data.get('meal_id')
        portions = int(request.data.get('portions', 1))

        try:
            meal = Meal.objects.get(id=meal_id, is_active=True)
        except Meal.DoesNotExist:
            return Response({"error": "Meal not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check ingredient availability
        meal_ingredients = MealIngredient.objects.filter(meal=meal, is_active=True)
        with transaction.atomic():
            for mi in meal_ingredients:
                ingredient = mi.ingredient
                required = mi.quantity_required * portions
                if ingredient.total_weight < required:
                    return Response({"error": f"Insufficient {ingredient.name}: {ingredient.total_weight}g available, {required}g needed"}, status=status.HTTP_400_BAD_REQUEST)

            # Deduct ingredients and log transactions
            for mi in meal_ingredients:
                ingredient = mi.ingredient
                required = mi.quantity_required * portions
                ingredient.total_weight -= required
                ingredient.save()

                consumption_type, _ = ChangeType.objects.get_or_create(name="Consumption")
                InventoryTransaction.objects.create(
                    ingredient=ingredient,
                    quantity_change=-required,
                    change_type=consumption_type,
                    user=request.user,
                )

            # Log meal serving
            serving = MealServing.objects.create(
                meal=meal,
                user=request.user,
                portions_served=portions,
            )
            serializer = MealServingSerializer(serving)
            return Response(serializer.data, status=status.HTTP_201_CREATED)