from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>', views.product, name='product'),
    path('search2', views.search2, name='search2'), # Wyszukiwarka produktów
]
