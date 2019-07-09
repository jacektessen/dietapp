from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from django.contrib.auth.models import User
from django.contrib import messages #, auth
from django.db.models import Q

from .models import Recipes
from products.models import Products
from .choices import recipe_kcal_choices, recipe_category_choices

def index(request):
    recipes = Recipes.objects.all()

    paginator = Paginator(recipes, 25)
    page = request.GET.get('page')
    paged_recipes = paginator.get_page(page)

    context = {
        'recipes': paged_recipes,
        'recipe_kcal_choices': recipe_kcal_choices,
        'recipe_category_choices': recipe_category_choices
    }

    return render(request, 'products/recipes.html', context)

def recipe(request, recipe_id):
    recipe = Recipes.objects.get(id = recipe_id)

    amt_1 = recipe.ingredient_1 / 100
    amt_2 = recipe.ingredient_2 / 100
    amt_3 = recipe.ingredient_3 / 100
    amt_4 = recipe.ingredient_4 / 100
    amt_5 = recipe.ingredient_5 / 100
    amt_6 = recipe.ingredient_6 / 100

    kcal_1 = recipe.product_1.kcal
    kcal_2 = recipe.product_2.kcal
    kcal_3 = recipe.product_3.kcal
    kcal_4 = recipe.product_4.kcal
    kcal_5 = recipe.product_5.kcal
    kcal_6 = recipe.product_6.kcal

    total_kcal = ((kcal_1 * amt_1) + (kcal_2 * amt_2) + (kcal_3 * amt_3) + (kcal_4 * amt_4) + (kcal_5 * amt_5) + (kcal_6 * amt_6))
    total_kcal = round(total_kcal, 1)

    protein_1 = float(recipe.product_1.protein)
    protein_3 = float(recipe.product_3.protein)
    protein_2 = float(recipe.product_2.protein)
    protein_4 = float(recipe.product_4.protein)
    protein_5 = float(recipe.product_5.protein)
    protein_6 = float(recipe.product_6.protein)

    total_protein_p = ((protein_1 * amt_1) + (protein_2 * amt_2) + (protein_3 * amt_3) + (protein_4 * amt_4) + (protein_5 * amt_5) + (protein_6 * amt_6))
    total_protein = round(total_protein_p, 1)

    fat_1 = float(recipe.product_1.fat)
    fat_3 = float(recipe.product_3.fat)
    fat_2 = float(recipe.product_2.fat)
    fat_4 = float(recipe.product_4.fat)
    fat_5 = float(recipe.product_5.fat)
    fat_6 = float(recipe.product_6.fat)

    total_fat_p = ((fat_1 * amt_1) + (fat_2 * amt_2) + (fat_3 * amt_3) + (fat_4 * amt_4) + (fat_5 * amt_5) + (fat_6 * amt_6))
    total_fat = round(total_fat_p, 1)

    carbo_1 = float(recipe.product_1.carbo)
    carbo_3 = float(recipe.product_3.carbo)
    carbo_2 = float(recipe.product_2.carbo)
    carbo_4 = float(recipe.product_4.carbo)
    carbo_5 = float(recipe.product_5.carbo)
    carbo_6 = float(recipe.product_6.carbo)

    total_carbo_p = ((carbo_1 * amt_1) + (carbo_2 * amt_2) + (carbo_3 * amt_3) + (carbo_4 * amt_4) + (carbo_5 * amt_5) + (carbo_6 * amt_6))
    total_carbo = round(total_carbo_p, 1)

    fibre_1 = float(recipe.product_1.fibre)
    fibre_3 = float(recipe.product_3.fibre)
    fibre_2 = float(recipe.product_2.fibre)
    fibre_4 = float(recipe.product_4.fibre)
    fibre_5 = float(recipe.product_5.fibre)
    fibre_6 = float(recipe.product_6.fibre)

    total_fibre_p = ((fibre_1 * amt_1) + (fibre_2 * amt_2) + (fibre_3 * amt_3) + (fibre_4 * amt_4) + (fibre_5 * amt_5) + (fibre_6 * amt_6))
    total_fibre = round(total_fibre_p, 1)
    


    context = {
        'recipe': recipe,
        'total_kcal': total_kcal,
        'total_protein': total_protein,
        'total_fat': total_fat,
        'total_carbo': total_carbo,
        'total_fibre': total_fibre
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
        
        if product_1_id == '':
            product_1_id = 1
            ingredient_1 = 0
        if product_2_id == '':
            product_2_id = 1
            ingredient_2 = 0
        if product_3_id == '':
            product_3_id = 1
            ingredient_3 = 0
        if product_4_id == '':
            product_4_id = 1
            ingredient_4 = 0
        if product_5_id == '':
            product_5_id = 1
            ingredient_5 = 0
        if product_6_id == '':
            product_6_id = 1
            ingredient_6 = 0

        #  Check if recipe exist already
        exist_name = Recipes.objects.all().filter(name=name)
        exist_description = Recipes.objects.all().filter(description=description)
        if exist_name:
            messages.error(request, 'Przepis o takiej nazwie już istnieje')
            return redirect('recipe_form')    
        if exist_description:
            messages.error(request, 'Identyczny przepis już istnieje')
            return redirect('recipe_form')


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

def search1(request):
    queryset_list = Recipes.objects.all()

    # Keywords przepisu w kolumnie nazwy przepisu
    if 'keywords_recipes' in request.GET:
        keywords_recipes = request.GET['keywords_recipes']
        if keywords_recipes:
            queryset_list = queryset_list.filter(name__icontains=keywords_recipes)

    # Keywords produktu w kolumnie nazwy przepisu
    if 'keywords_products' in request.GET:
        keywords_products = request.GET['keywords_products']
        if keywords_products:
            queryset_list = queryset_list.filter(Q(product_1_id=keywords_products) |
                                                Q(product_2_id=keywords_products) |
                                                Q(product_3_id=keywords_products) |
                                                Q(product_4_id=keywords_products) |
                                                Q(product_5_id=keywords_products) |
                                                Q(product_6_id=keywords_products)
                                                )
        # dlaczego poniższe nie działa???
        # if queryset_list is None:
        #     queryset_list = queryset_list.filter(product_2_id=keywords_products)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category != 'Kategoria':
            queryset_list = queryset_list.filter(category__iexact=category)

    # Category
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            queryset_list = queryset_list.filter(author__icontains=author)

    context = {
        'recipe_category_choices': recipe_category_choices,
        # 'recipe_kcal_choices': recipe_kcal_choices,
        'recipes': queryset_list,
        'values': request.GET
    }

    return render(request, 'pages/search_recipes.html', context)