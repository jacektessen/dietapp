from django.db import models

from datetime import datetime
from recipes.models import Recipes

class FavouriteRecipe(models.Model):
    user_id = models.IntegerField()
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "FavouriteRecipes"

