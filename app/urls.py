from django.urls import path, include
from .views import UnitListCreate, CategoryListCreate, IngredientViewSet, MealViewSet, ServeMealView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('ingredients', IngredientViewSet)
router.register('meals', MealViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('units/', UnitListCreate.as_view(), name='unit_list_create'),
    path('categories/', CategoryListCreate.as_view(), name='category_list_create'),
    path('meals/serve/', ServeMealView.as_view(), name='serve_meal'),
]
