from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),  
    path('dashboard_message/<int:contact_id>', views.dashboard_message, name='dashboard_message'),  
    path('test', views.test, name='test'),  
]