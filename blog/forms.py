from django import forms

from .models import Recipe

class RecipeForm(forms.ModelForm):
    should_publish = forms.Field(widget=forms.CheckboxInput)

    class Meta:
        model = Recipe
        exclude = ['author', 'published_date']