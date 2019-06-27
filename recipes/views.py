from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Recipes

def index(request):
    recipes = Recipes.objects.all()

    paginator = Paginator(recipes, 25)
    page = request.GET.get('page')
    paged_recipes = paginator.get_page(page)

    context = {
        'recipes': paged_recipes
    }

    return render(request, 'products/recipes.html', context)
'''
def product(request, recipe_id):
    return render(request, 'products/product.html')
'''

def recipe(request, recipe_id):
    recipe = Recipes.objects.get(id = recipe_id)

    context = {
        'recipe': recipe
    }

    return render(request, 'products/recipe.html', context)
