from django.db import models
from django.conf import settings
from .products import Meal, Ingredient
class ChangeType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MealServing(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    serving_date = models.DateTimeField(auto_now_add=True)
    portions_served = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Meal {self.meal.name} served by {self.user.username}"

class InventoryTransaction(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity_change = models.FloatField()
    change_type = models.ForeignKey(ChangeType, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    change_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity_change}g change for {self.ingredient.name}"