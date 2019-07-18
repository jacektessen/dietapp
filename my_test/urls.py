from django.urls import path

from . import views

urlpatterns = [
    path('test_recipes', views.test_fill, name='test_recipes'),
    path('test_form', views.test_form, name='test_form'),
#     #path('<int:recipe_id>', views.recipe, name='recipe'),
]