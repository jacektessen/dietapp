from django.shortcuts import render, redirect
from recipes.models import Recipes
from .models import FavouriteRecipe
from django.contrib import messages


def add_favourite_recipe(request, recipe_id):
    recipe = Recipes.objects.get(id = recipe_id)

    context = {
        'recipe': recipe,
        }

    if request.method == 'POST':
        user_id = request.POST['user_id']
        recipe_id = request.POST['recipe_id']

        #  Check if user has like already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_liked = FavouriteRecipe.objects.all().filter(recipe_id=recipe_id, user_id=user_id)
            if has_liked:
                messages.error(request, 'Ten przepis masz już w ulubionych')
                return render(request, 'products/recipe.html', context)

        send = FavouriteRecipe(user_id=user_id, recipe_id=recipe_id)

        send.save()

        messages.success(request, 'Dodano do ulubionych')
        return render(request, 'products/recipe.html', context)
