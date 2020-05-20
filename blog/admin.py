from django.contrib import admin

from .models import Ingredient, IngredientType, Recipe, RecipeIngredient
from .admin_models import RecipeAdmin, RecipeIngredientsInline

admin.site.register(Ingredient)
admin.site.register(IngredientType)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient)