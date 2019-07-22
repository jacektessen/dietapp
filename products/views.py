from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .serializers import ProductsSerializer
# from rest_framework import generics
from rest_framework import viewsets

from .models import Products
from .choices import (product_kcal_choices, product_protein_choices, 
                    product_category_choices, product_carbo_choices, 
                    product_fat_choices)

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

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(product__icontains=keywords)

    if 'category' in request.GET:
        category = request.GET['category']
        if category != 'Kategoria':
            queryset_list = queryset_list.filter(category__iexact=category)

    if 'kcal' in request.GET:
        kcal = request.GET['kcal']
        if kcal != 'Max. kaloryczność':
            queryset_list = queryset_list.filter(kcal__lte=kcal)

    if 'protein' in request.GET:
        protein = request.GET['protein']
        if protein != 'Białko':
            if protein == '3':
                queryset_list = queryset_list.filter(protein__lte=3)
            elif protein == '20':
                queryset_list = queryset_list.filter(protein__gte=3, protein__lte=10)
            elif protein == '50':
                queryset_list = queryset_list.filter(protein__gte=10, protein__lte=30)
            else:
                queryset_list = queryset_list.filter(protein__gte=30)

    if 'carbo' in request.GET:
        carbo = request.GET['carbo']
        if carbo != 'Węglowodany':
            if carbo == '3':
                queryset_list = queryset_list.filter(carbo__lte=3)
            elif carbo == '20':
                queryset_list = queryset_list.filter(carbo__gte=3, carbo__lte=20)
            elif carbo == '50':
                queryset_list = queryset_list.filter(carbo__gte=20, carbo__lte=50)
            else:
                queryset_list = queryset_list.filter(carbo__gte=50)

    if 'fat' in request.GET:
        fat = request.GET['fat']
        if fat != 'Tłuszcz':
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

def product_form(request):
    return render(request, 'products/product_form.html')

def add_product(request):
    if request.method == 'POST':
        product = request.POST['product']
        kcal = request.POST['kcal']
        protein = request.POST['protein']
        fat = request.POST['fat']
        carbo = request.POST['carbo']
        fibre = request.POST['fibre']
        category = request.POST['category']
        user_id = request.POST['user_id']
        # photo_main = request.POST['photo_main']

        if protein == '':
            protein = 0
        if fat == '':
            fat = 0
        if carbo == '':
            carbo = 0
        if fibre == '':
            fibre = 0

        #  Check if product exist already
        exist = Products.objects.all().filter(product=product)
        if exist:
            messages.error(request, 'Produkt o takiej nazwie już istnieje')
            return redirect('legend')


        send = Products(
            product=product,
            kcal=kcal,
            protein=protein,
            fat=fat,
            carbo=carbo,
            fibre=fibre,
            category=category,
            user_id=user_id,
            # photo_main=photo_main,
        )        

        send.save()

        messages.success(request, 'Produkt został dodany. Dziękuję!!!')
        return redirect('legend')


# https://www.youtube.com/watch?v=263xt_4mBNc

class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer