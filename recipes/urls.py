from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='recipes'),
    path('<int:recipe_id>', views.recipe, name='recipe'),
    path('recipe_form', views.recipe_form, name='recipe_form'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('add_products_to_recipe', views.add_products_to_recipe, name='add_products_to_recipe'),
    path('add_recipe_finish', views.add_recipe_finish, name='add_recipe_finish'),
    path('legend', views.legend, name='legend'),
    path('search1', views.search1, name='search1'), # Wyszukiwarka przepisów
]