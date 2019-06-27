from django.contrib import admin

from .models import Recipes

class RecipesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'author', 'photo_main')
    list_display_links = ('id', 'name')
    list_filter = ('category',)
    list_editable = ('photo_main',)
    search_fields = ('name', 'category')
    list_per_page = 25

admin.site.register(Recipes, RecipesAdmin)
