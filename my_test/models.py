from django.db import models

from datetime import datetime
from products.models import Products

class TestRecipes(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    user_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    product_test_1 = models.ForeignKey(Products, null=True, related_name='product_test_1', on_delete=models.DO_NOTHING, blank=True)
    # product_test_1_kcal = models.ForeignKey(Products, null=True, related_name='product_test_1_kcal', on_delete=models.DO_NOTHING, blank=True)
    # ingredient_1 = models.IntegerField(default=0, null=True, blank=True) 
    product_test_2 = models.ForeignKey(Products, null=True, related_name='product_test_2', on_delete=models.DO_NOTHING, blank=True)
    # ingredient_2 = models.IntegerField(default=0, null=True, blank=True) 
    # product_test_3 = models.ForeignKey(Products, null=True, related_name='product_test_3', on_delete=models.DO_NOTHING, blank=True)
    # ingredient_3 = models.IntegerField(default=0, null=True, blank=True)
    # product_4 = models.ForeignKey(Products, null=True, related_name='product_4', on_delete=models.DO_NOTHING, blank=True)
    # ingredient_4 = models.IntegerField(default=0, null=True, blank=True)
    # product_5 = models.ForeignKey(Products, null=True, related_name='product_5', on_delete=models.DO_NOTHING, blank=True)
    # ingredient_5 = models.IntegerField(default=0, null=True, blank=True)
    # product_6 = models.ForeignKey(Products, null=True, related_name='product_6', on_delete=models.DO_NOTHING, blank=True)
    # ingredient_6 = models.IntegerField(default=0, null=True, blank=True)
    
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True )
    # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    # photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    # photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    recipe_date = models.DateTimeField(default=datetime.now, blank=True, null=True)

    class Meta:
        verbose_name_plural = "TestRecipes"

    def __str__(self):
        return self.name

    # def kcal_total(self):
    #     kcal_1 = self.product_test_1.values('product_test_1', 'product_test_1__kcal')
    #     kcal_2 = self.product_test_2.values('product_test_2', 'product_test_2__kcal')

    #     total = kcal_1 + kcal_2

        #total = self.product_test_1.filter(kcal=kcal) + self.product_test_2.filter(kcal=kcal)