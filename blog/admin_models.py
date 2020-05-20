from django.contrib import admin
from .models import Recipe, RecipeIngredient

class RecipeIngredientsInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientsInline, )