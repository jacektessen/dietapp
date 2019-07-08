from django.urls import path

from . import views

urlpatterns = [
    path('<int:recipe_id>', views.add_favourite_recipe, name='add_favourite_recipe'),
]