from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='recipes'),
    path('<int:recipe_id>', views.recipe, name='recipe'),
]