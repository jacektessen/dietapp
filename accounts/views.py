from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from products.models import Products
from recipes.models import Recipes
from favourite.models import FavouriteRecipe

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # CHeck if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Ta nazwa użytkownika już istenie')
                return redirect('register')
            else: 
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Ten email został już użyty')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, 
                    first_name=first_name, last_name=last_name) 
                    user.save()
                    messages.success(request, 'Rejestracja gotowa! Zaloguj się')
                    return redirect('login')

            messages.error(request, 'Wprowadzono różne hasła')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Jesteś teraz zalogowany')
            return redirect('dashboard')
        else:
            messages.error(request, 'Nieprawidłowe dane')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Jesteś teraz wylogowany')
        return redirect('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    user_recipes = Recipes.objects.order_by('-recipe_date').filter(user_id=request.user.id)
    favourite_recipe = FavouriteRecipe.objects.all().filter(user_id=request.user.id)
    
    context = {
    'contacts': user_contacts,
    'user_recipes': user_recipes,
    'favourite_recipe': favourite_recipe
    }
    
    return render(request, 'accounts/dashboard.html', context)



def dashboard_message(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    context = {
        'contact': contact
    }
    return render(request, 'accounts/dashboard_message.html', context)


# def test(request, contact_id):
#     contact = get_object_or_404(Contact, pk=contact_id)

#     context = {
#         'contact': contact
#     }
#     return render(request, 'accounts/test.html', context)

def test(request, slug):
    contact = get_object_or_404(Contact, slug=slug)

    context = {
        'contact': contact
    }
    return render(request, 'accounts/test.html', context)
