from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('cooperation', views.cooperation, name='cooperation'),
    path('description', views.description, name='description'),
    path('for_whom', views.for_whom, name='for_whom'),
    path('instruction', views.instruction, name='instruction'),
    path('why_worth', views.why_worth, name='why_worth'),
    path('bmi', views.bmi, name='bmi'),
]   