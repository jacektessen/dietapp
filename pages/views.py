from django.shortcuts import render
from django.http import HttpResponse

from products.choices import (
    product_kcal_choices, 
    product_protein_choices, 
    product_category_choices, 
    product_carbo_choices, 
    product_fat_choices,
)

from recipes.choices import recipe_category_choices


def index(request):

    context = {
        'product_kcal_choices': product_kcal_choices,
        'product_protein_choices': product_protein_choices,
        'product_category_choices': product_category_choices,
        'product_carbo_choices': product_carbo_choices,
        'product_fat_choices': product_fat_choices,
        'recipe_category_choices': recipe_category_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def bmi(request):
    return render(request, 'pages/bmi.html')

def contact_page(request):
    return render(request, 'pages/contact_page.html')

def cooperation(request):
    return render(request, 'pages/cooperation.html')

def description(request):
    return render(request, 'pages/description.html')

def for_whom(request):
    return render(request, 'pages/for_whom.html')

def instruction(request):
    return render(request, 'pages/instruction.html')

def why_worth(request):
    return render(request, 'pages/why_worth.html')

def search1(request):
    return render(request, 'pages/search_recipes.html')

