from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('kontakt', views.contact_page, name='contact_page'),
    path('wspolpraca', views.cooperation, name='cooperation'),
    path('opis', views.description, name='description'),
    path('dla_kogo', views.for_whom, name='for_whom'),
    path('instrukcja', views.instruction, name='instruction'),
    path('dlaczego_warto', views.why_worth, name='why_worth'),
    path('bmi', views.bmi, name='bmi'),
    path('search1', views.search1, name='search1'), # Wyszukiwarka przepisów
    
]   