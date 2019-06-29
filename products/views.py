from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Products

def index(request):
    products = Products.objects.all().filter(is_active=True)

    paginator = Paginator(products, 25)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products
    }
    
    return render(request, 'products/products.html', context)

def product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)

    context = {
        'product': product
    }

    return render(request, 'products/product.html', context)
    