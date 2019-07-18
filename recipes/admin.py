from django.contrib import admin

from .models import Recipes, Ingredients, ingredients_inline, productsAdmin,  recipesAdmin

admin.site.register(Recipes, recipesAdmin)