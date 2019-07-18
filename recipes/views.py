from django.shortcuts import render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# from django.contrib.auth.models import User
from django.contrib import messages #, auth
from django.db.models import Q

from .models import Recipes, Ingredients
from products.models import Products
from .choices import recipe_kcal_choices, recipe_category_choices

def index(request):
    recipes = Recipes.objects.order_by('-recipe_date')

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
    products = Ingredients.objects.all().filter(recipe_id=recipe_id)

    total_kcal = total_protein = total_fat = total_carbo = total_fibre = 0

    for kcal in products:
        total_kcal += (float(kcal.product.kcal) * float(kcal.ingredient)) / 100
    total_kcal = round(total_kcal, 1)

    for protein in products:
        total_protein += (float(protein.product.protein) * float(protein.ingredient)) / 100
    total_protein = round(total_protein, 1)

    for fat in products:
        total_fat += (float(fat.product.fat) * float(fat.ingredient)) / 100
    total_fat = round(total_fat, 1)

    for carbo in products:
        total_carbo += (float(carbo.product.carbo) * float(carbo.ingredient)) / 100
    total_carbo = round(total_carbo, 1)

    for fibre in products:
        total_fibre += (float(fibre.product.fibre) * float(fibre.ingredient)) / 100
    total_fibre = round(total_fibre, 1)

    context = {
        'recipe': recipe,
        'products': products,
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
        
        # photo_main = request.POST['photo_main']

        # Check if recipe exist already
        exist_name = Recipes.objects.all().filter(name=name)
        exist_description = Recipes.objects.all().filter(description=description)

        if exist_name:
            messages.error(request, 'Przepis o takiej nazwie już istnieje')

            return redirect('recipe_form')

        if exist_description:
            messages.error(request, 'Identyczny przepis już istnieje')

            return redirect('recipe_form')


        send_part_1 = Recipes(
            name=name, 
            category=category, 
            author=author, 
            user_id=user_id, 
            description=description,
        )

        send_part_1.save()

        recipe_id = send_part_1.pk

        context = {
            'recipe_id': recipe_id,
            'name': name, 
            'category': category, 
            'description': description,
        }
 
        return render(request, 'products/recipe_form_add_products.html', context)


def add_products_to_recipe(request):

    if request.method == 'POST':
        product_id = request.POST['product_id']
        ingredient = request.POST['ingredient']
        recipe_id = request.POST['recipe_id']

        name = request.POST['name']
        category = request.POST['category']
        author = request.POST['author']
        user_id = request.POST['user_id']
        description = request.POST['description']

        send_part_2 = Ingredients(
            product_id = product_id,
            ingredient = ingredient, 
            recipe_id = recipe_id
        )

        send_part_2.save()

        part_2 = Ingredients.objects.all().filter(recipe_id=recipe_id)

        context = {
            'part_2': part_2,
            'name': name, 
            'category': category, 
            'description': description,
            'recipe_id': recipe_id
        }

        return render(request, 'products/recipe_form_add_products.html', context) 

def add_recipe_finish(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        ingredient = request.POST['ingredient']
        recipe_id = request.POST['recipe_id']

        send_part_2 = Ingredients(
            product_id = product_id,
            ingredient = ingredient, 
            recipe_id = recipe_id
        )

        send_part_2.save()

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