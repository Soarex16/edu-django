from django.shortcuts import render, get_object_or_404
from .models import Recipe

# список всех
# изменение
# добавление
# удаление

def recipes_list(request):
    params = {
        'title': 'Рецепты',
        'recipes_list': Recipe.objects.all(),
    }

    return render(request, 'recipes_list.html', params)

def recipe_details(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    params = {
        'title': recipe.recipe_name,
        'recipe': recipe,
        'caloricity': recipe.caloricity,
        'ingredients': recipe.recipeingredient_set.all(),
    }

    return render(request, 'recipe_details.html', params)

def add_recipe(request):
    return render(request, 'edit_recipe.html', {})

def edit_recipe(request):
    return render(request, 'edit_recipe.html', {})

def delete_recipe(request):
    return render(request, 'delete_recipe.html', {})
