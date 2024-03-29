
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('produkty/', include('products.urls')),
    path('przepisy/', include('recipes.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('ulubione/', include('favourite.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
