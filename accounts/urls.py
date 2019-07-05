from django.urls import path, re_path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),  
    path('dashboard_message/<int:contact_id>', views.dashboard_message, name='dashboard_message'),  
    path('test/<str:slug>', views.test, name='test'), 
    #re_path(r'^test/(?P<int:slug>\w+)/$', views.test, name='test'),
]