from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages

from .models import Recipe
from .forms import RecipeForm

# список всех
# изменение
# добавление
# удаление

def recipes_list(request):
    params = {
        'title': 'Рецепты',
        'recipes_list': Recipe.objects.filter(published_date__isnull=False),
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
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            if form.cleaned_data['should_publish']:
                recipe.published_date = timezone.now()
            recipe.save()
            messages.success(request, 'Recipe was successfully created')
            return redirect('recipes_list')
    else:
        form = RecipeForm(initial={'author': request.user})

    return render(request, 'edit_recipe.html', {'form': form})

def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            new_recipe = form.save(commit=False)
            new_recipe.id = recipe.id
            new_recipe.author = request.user
            if form.cleaned_data['should_publish']:
                new_recipe.published_date = timezone.now()
            new_recipe.save()
            messages.success(request, 'Recipe was successfully updated')
            return redirect('recipes_list')
    else:
        form = RecipeForm(initial={'should_publish': recipe.published_date is not None}, instance=recipe)

    return render(request, 'edit_recipe.html', {'form': form})

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe was successfully deleted')

    return redirect('recipes_list')
