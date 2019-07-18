# from django.db import models
# from django.contrib import admin

# from datetime import datetime
# from products.models import Products

# class TestRecipes(models.Model):
#     name = models.CharField(max_length=200)
#     category = models.CharField(max_length=50)
#     author = models.CharField(max_length=50)
#     user_id = models.IntegerField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     recipe_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
#     products = models.ManyToManyField(Products, through='Ingredients')

#     class Meta:
#         verbose_name_plural = "TestRecipes"

#     def __str__(self):
#         return self.name

# class Ingredients(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(TestRecipes, on_delete=models.CASCADE)
#     ingredient = models.IntegerField(default=0, null=True, blank=True)

# class ingredients_inline(admin.TabularInline):
#     model = Ingredients
#     extra = 1

# class productsAdmin(admin.ModelAdmin):
#     inlines = (ingredients_inline,)

# class testrecipesAdmin(admin.ModelAdmin):
#     inlines = (ingredients_inline,)
#     list_display = ('id', 'name', 'category', 'author', 'user_id')
#     list_display_links = ('id', 'name')
#     list_filter = ('category',)
#     search_fields = ('name', 'category')
#     list_per_page = 25