from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.utils import timezone

class IngredientType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.type_name

class Ingredient(models.Model):
    type = models.ForeignKey(IngredientType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()

    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    preparation_time = models.DurationField()

    created_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    @property
    def caloricity(self):
        return self.recipeingredient_set.aggregate(Sum('caloricity'))['caloricity__sum']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.recipe_name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    measure = models.FloatField()
    measurement_unit = models.CharField(max_length=15)
    caloricity = models.FloatField()