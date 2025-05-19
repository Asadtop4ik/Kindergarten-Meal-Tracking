from rest_framework import serializers
from app.models import Ingredient, Unit, Meal, Category, MealIngredient

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class IngredientSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'total_weight', 'unit', 'threshold', 'is_active', 'deleted_at', 'created_at', 'updated_at']

class MealIngredientSerializer(serializers.ModelSerializer):
    meal = serializers.PrimaryKeyRelatedField(queryset=Meal.objects.all())
    ingredient = serializers.PrimaryKeyRelatedField(queryset=Ingredient.objects.all())
    unit = UnitSerializer()

    class Meta:
        model = MealIngredient
        fields = ['id', 'meal', 'ingredient', 'quantity_required', 'unit', 'portion_yield_factor', 'updated_by', 'is_active', 'deleted_at', 'created_at', 'updated_at']

class MealSerializer(serializers.ModelSerializer):
    ingredients = MealIngredientSerializer(many=True, required=False)
    category = CategorySerializer()

    class Meta:
        model = Meal
        fields = ['id', 'name', 'category', 'ingredients', 'created_by', 'is_active', 'deleted_at', 'created_at', 'updated_at']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        meal = Meal.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            MealIngredient.objects.create(meal=meal, **ingredient_data)
        return meal

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        instance.name = validated_data.get('name', instance.name)
        instance.category = validated_data.get('category', instance.category)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.save()


        instance.ingredients.all().delete()
        for ingredient_data in ingredients_data:
            MealIngredient.objects.create(meal=instance, **ingredient_data)
        return instance