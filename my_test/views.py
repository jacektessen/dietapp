from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from .models import TestRecipes

def test_form(request):
    return render(request, 'my_test/test_form.html')

# /my_test
# def index(request):
#     test_recipes = TestRecipes.objects.all()

#     context = {
#         'test_recipes': test_recipes
#     }

#     return render(request, 'my_test/test_recipes.html', context)

def test_fill(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = request.POST['category']
        author = request.POST['author']
        user_id = request.POST['user_id']
        description = request.POST['description']
        product_test_1_id = request.POST['product_test_1_id']
        # ingredient_1 = request.POST['ingredient_1']
        # product_test_2 = request.POST['product_test_2']
        # ingredient_2 = request.POST['ingredient_2']
        # product_test_3 = request.POST['product_test_3']
        # ingredient_3 = request.POST['ingredient_3']
        # photo_main = request.POST['photo_main']
        # recipe_date = request.POST['recipe_date']

        # if request.user.is_authenticated:
        #     user_id = request.user.id
        #     has_this_recipe = TestRecipes.objects.all().filter(name=name, user_id=user_id)
        #     if has_this_recipe:
        #         message.error(request, 'Wprowadziłeś już przepis o tej nazwie')
        #         return redirect('test_recipes')
        send = TestRecipes(
            name=name, 
            category=category, 
            author=author, 
            user_id=user_id, 
            description=description,
            product_test_1_id=product_test_1_id,
            # ingredient_1=ingredient_1,
            # product_test_2=product_test_2,
            # ingredient_2=ingredient_2,
            # product_test_3=product_test_3,
            # ingredient_3=ingredient_3,
            # recipe_date=recipe_date,
        )

        send.save()
 
        messages.success(request, 'Twój przepis został dodany. Dziękuję!!!')
        return redirect('index')
