from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes_list, name='recipes_list'),
    path('recipes/', views.recipes_list, name='recipes_list'),
    path('recipes/<int:recipe_id>/', views.add_recipe, name='recipe_details'),
    path('recipes/<int:recipe_id>/edit', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:recipe_id>/delete', views.delete_recipe, name='delete_recipe'),
]