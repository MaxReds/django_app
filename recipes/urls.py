from django.urls import path
from .views import home, recipe_detail, add_recipe, edit_recipe, signup, category_recipes

urlpatterns = [
    path('', home, name='home'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/add/', add_recipe, name='add_recipe'),
    path('recipe/edit/<int:recipe_id>/', edit_recipe, name='edit_recipe'),
    path('signup/', signup, name='signup'),
    path('category/<int:category_id>/', category_recipes, name='category_recipes'),

]
