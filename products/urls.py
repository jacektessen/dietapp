from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>', views.product, name='product'),
    path('search2', views.search2, name='search2'), # Wyszukiwarka produktów
    path('product_form', views.product_form, name='product_form'), # Formularz dodawania produktów
    path('add_product', views.add_product, name='add_product'),
]
