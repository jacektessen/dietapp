from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# from .models import TestRecipes, Ingredients

def test_form(request):
    return render(request, 'my_test/test_form.html')


def test_fill(request):
    # total = TestRecipes.objects.get(id=8)
    # product = Ingredients.objects.all().filter(recipe_id=8)
    # kcal1 = Ingredients.objects.get(id=2)
    # kcal = kcal1.product.kcal

    # sum = 0
    # for x in product:
    #     sum += (float(x.product.kcal) * float(x.ingredient)) /100

    # sum = round(sum,1)
    
    
    # context = {
    #     'total': total,
    #     'product': product,
    #     'sum': sum
    # }

    return render(request, 'my_test/test_recipes.html')
   
