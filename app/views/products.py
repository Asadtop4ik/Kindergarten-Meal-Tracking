from rest_framework import generics
from app.models import Ingredient, Unit, Meal, Category
from app.serializers import IngredientSerializer, UnitSerializer, MealSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated

class UnitListCreate(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class IngredientListCreate(generics.ListCreateAPIView):
    queryset = Ingredient.objects.filter(is_active=True)
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

class IngredientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

class MealListCreate(generics.ListCreateAPIView):
    queryset = Meal.objects.filter(is_active=True)
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

class MealRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]