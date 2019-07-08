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

    context = {
        'recipe': recipe,
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