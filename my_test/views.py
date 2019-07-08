from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import TestRecipes

def test_form(request):
    return render(request, 'my_test/test_form.html')


def test_fill(request):
    total = TestRecipes()
    k = total.kcal_total
    
    context = {
        'k': k
    }
    return render(request, 'my_test/test_recipes.html', context)
   
