from django.db import models

from datetime import datetime
from products.models import Products

class Recipes(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    product_1 = models.ForeignKey(Products, null=True, related_name='product_1', on_delete=models.DO_NOTHING)
    ingredient_1 = models.IntegerField(default=0) 
    product_2 = models.ForeignKey(Products, null=True, related_name='product_2', on_delete=models.DO_NOTHING)
    ingredient_2 = models.IntegerField(default=0, blank=True) 
    product_3 = models.ForeignKey(Products, null=True, related_name='product_3', on_delete=models.DO_NOTHING)
    ingredient_3 = models.IntegerField(default=0, blank=True)
    product_4 = models.ForeignKey(Products, null=True, related_name='product_4', on_delete=models.DO_NOTHING)
    ingredient_4 = models.IntegerField(default=0, blank=True)
    product_5 = models.ForeignKey(Products, null=True, related_name='product_5', on_delete=models.DO_NOTHING)
    ingredient_5 = models.IntegerField(default=0, blank=True)
    product_6 = models.ForeignKey(Products, null=True, related_name='product_6', on_delete=models.DO_NOTHING)
    ingredient_6 = models.IntegerField(default=0, blank=True)
    
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    recipe_date = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.name
