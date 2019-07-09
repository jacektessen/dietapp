from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import TestRecipes

def test_form(request):
    return render(request, 'my_test/test_form.html')


def test_fill(request):
    total = TestRecipes.objects.all()
    x = TestRecipes.objects.get(product_test_1=1)
    kcal = (x.product_test_1.kcal + 2)
    
    context = {
        'total': total,
        'kcal': kcal
    }
    return render(request, 'my_test/test_recipes.html', context)
   
