# app/serializers/meal_serving.py
from rest_framework import serializers
from app.models import MealServing, InventoryTransaction, ChangeType

class ChangeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangeType
        fields = ['id', 'name']

class MealServingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealServing
        fields = ['id', 'meal', 'user', 'serving_date', 'portions_served', 'is_active', 'deleted_at', 'created_at', 'updated_at']

class InventoryTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryTransaction
        fields = ['id', 'ingredient', 'quantity_change', 'change_type', 'user', 'change_date', 'is_active', 'deleted_at', 'created_at', 'updated_at']