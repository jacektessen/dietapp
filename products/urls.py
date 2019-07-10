from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('', views.ProductsView)

urlpatterns = [
    path('', views.index, name='products'),
    path('<int:product_id>', views.product, name='product'),
    path('search2', views.search2, name='search2'), # Wyszukiwarka produktów
    path('product_form', views.product_form, name='product_form'), # Formularz dodawania produktów
    path('add_product', views.add_product, name='add_product'),
    path('rest/', include(router.urls)),
    # path('rest/<int:pk>/', views.ProductsDetail.as_view()),
]

# urlpatterns += format_suffix_patterns(urlpatterns, allowed=['json', 'html'])