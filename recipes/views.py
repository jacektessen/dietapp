from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from django.contrib import messages, auth

from .models import Recipes
from products.models import Products

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

def recipe_form(request):
    return render(request, 'products/recipe_form.html')

def add_recipe(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        author = request.POST['author']
        user_id = request.POST['user_id']
        description = request.POST['description']
        product_1_id = request.POST['product_1_id']
        ingredient_1 = request.POST['ingredient_1']
        product_2_id = request.POST['product_2_id']
        ingredient_2 = request.POST['ingredient_2']
        product_3_id = request.POST['product_3_id']
        ingredient_3 = request.POST['ingredient_3']
        product_4_id = request.POST['product_4_id']
        ingredient_4 = request.POST['ingredient_4']
        product_5_id = request.POST['product_5_id']
        ingredient_5 = request.POST['ingredient_5']
        product_6_id = request.POST['product_6_id']
        ingredient_6 = request.POST['ingredient_6']
        # photo_main = request.POST['photo_main']
        # recipe_date = request.POST['recipe_date']

        # if request.user.is_authenticated:
        #     user_id = request.user.id
        #     has_this_recipe = TestRecipes.objects.all().filter(name=name, user_id=user_id)
        #     if has_this_recipe:
        #         message.error(request, 'Wprowadziłeś już przepis o tej nazwie')
        #         return redirect('test_recipes')
        
        if product_1_id == '':
            product_1_id = None
            ingredient_1 = 0
        if product_2_id == '':
            product_2_id = None
            ingredient_2 = 0
        if product_3_id == '':
            product_3_id = None
            ingredient_3 = 0
        if product_4_id == '':
            product_4_id = None
            ingredient_4 = 0
        if product_5_id == '':
            product_5_id = None
            ingredient_5 = 0
        if product_6_id == '':
            product_6_id = None
            ingredient_6 = 0


        send = Recipes(
            name=name, 
            category=category, 
            author=author, 
            user_id=user_id, 
            description=description,
            product_1_id=product_1_id,
            ingredient_1=ingredient_1,
            product_2_id=product_2_id,
            ingredient_2=ingredient_2,
            product_3_id=product_3_id,
            ingredient_3=ingredient_3,
            product_4_id=product_4_id,
            ingredient_4=ingredient_4,
            product_5_id=product_5_id,
            ingredient_5=ingredient_5,
            product_6_id=product_6_id,
            ingredient_6=ingredient_6,
            # photo_main=photo_main,
            # recipe_date=recipe_date,
        )

        send.save()
 
        messages.success(request, 'Twój przepis został dodany. Dziękuję!!!')
        return redirect('recipes')

def legend(request):
    queryset_list = Products.objects.all()

    # Keywords w kolumnie nazwy produktu
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(product__icontains=keywords)

    context = {
        'products': queryset_list
    }
    return render(request, 'products/legend.html', context)
