from django.db import models

from datetime import datetime
from products.models import Products

class Recipes(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    product_1 = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    ingredient_1 = models.IntegerField() 
    '''
    product_2 = models.ForeignKey(Products, on_delete=models.DO_NOTHING, blank=True)
    ingredient_2 = models.IntegerField(blank=True) 
    product_3 = models.ForeignKey(Products, on_delete=models.DO_NOTHING, blank=True)
    ingredient_3 = models.IntegerField(blank=True)
    product_4 = models.ForeignKey(Products, on_delete=models.DO_NOTHING, blank=True)
    ingredient_4 = models.IntegerField(blank=True)
    product_5 = models.ForeignKey(Products, on_delete=models.DO_NOTHING, blank=True)
    ingredient_5 = models.IntegerField(blank=True)
    product_6 = models.ForeignKey(Products, on_delete=models.DO_NOTHING, blank=True)
    ingredient_6 = models.IntegerField(blank=True)
    '''
    
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    recipe_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.name
