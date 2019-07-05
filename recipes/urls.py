from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='recipes'),
    path('<int:recipe_id>', views.recipe, name='recipe'),
    path('recipe_form', views.recipe_form, name='recipe_form'),
    path('add_recipe', views.add_recipe, name='add_recipe'),
    path('legend', views.legend, name='legend'),
]