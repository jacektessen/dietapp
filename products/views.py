from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Products
from .choices import product_kcal_choices, product_protein_choices, product_category_choices, product_carbo_choices, product_fat_choices

def index(request):
    products = Products.objects.all().filter(is_active=True)

    paginator = Paginator(products, 25)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products,
        'product_kcal_choices': product_kcal_choices,
        'product_protein_choices': product_protein_choices,
        'product_category_choices': product_category_choices,
        'product_carbo_choices': product_carbo_choices,
        'product_fat_choices': product_fat_choices
    }
    
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product.html', context)

def search2(request):
    queryset_list = Products.objects.all()

    # Keywords w kolumnie nazwy produktu
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(product__icontains=keywords)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__iexact=category)

    # Kcal
    if 'kcal' in request.GET:
        kcal = request.GET['kcal']
        if kcal:
            queryset_list = queryset_list.filter(kcal__lte=kcal)

    # Protein
    if 'protein' in request.GET:
        protein = request.GET['protein']
        if protein == '3':
            queryset_list = queryset_list.filter(protein__lte=3)
        elif protein == '20':
            queryset_list = queryset_list.filter(protein__gte=3, protein__lte=10)
        elif protein == '50':
            queryset_list = queryset_list.filter(protein__gte=10, protein__lte=30)
        else:
            queryset_list = queryset_list.filter(protein__gte=30)

    # Carbo
    if 'carbo' in request.GET:
        carbo = request.GET['carbo']
        if carbo == '3':
            queryset_list = queryset_list.filter(carbo__lte=3)
        elif carbo == '20':
            queryset_list = queryset_list.filter(carbo__gte=3, carbo__lte=20)
        elif carbo == '50':
            queryset_list = queryset_list.filter(carbo__gte=20, carbo__lte=50)
        else:
            queryset_list = queryset_list.filter(carbo__gte=50)

    # Fat
    if 'fat' in request.GET:
        fat = request.GET['fat']
        if fat == '3':
            queryset_list = queryset_list.filter(fat__lte=3)
        elif fat == '20':
            queryset_list = queryset_list.filter(fat__gte=3, fat__lte=20)
        elif fat == '50':
            queryset_list = queryset_list.filter(fat__gte=20, fat__lte=50)
        else:
            queryset_list = queryset_list.filter(fat__gte=50)

    context = {
        'product_kcal_choices': product_kcal_choices,
        'product_protein_choices': product_protein_choices,
        'product_category_choices': product_category_choices,
        'product_carbo_choices': product_carbo_choices,
        'product_fat_choices': product_fat_choices,
        'products': queryset_list,
        'values': request.GET
    }
    return render(request, 'pages/search_products.html', context)
    