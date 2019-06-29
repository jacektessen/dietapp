from django.db import models

from datetime import datetime

class Products(models.Model):
    product = models.CharField(max_length=200)
    kcal = models.IntegerField()
    protein = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)  # białko
    fat = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)      # tłuszcz
    carbo = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)    # węglowodany
    fibre = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)    # błonnik
    category = models.CharField(max_length=50)
    product_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.product
