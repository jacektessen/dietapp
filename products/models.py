from django.db import models

from datetime import datetime

class Products(models.Model):
    product = models.CharField(max_length=200)
    kcal = models.IntegerField()
    protein = models.DecimalField(max_digits=3, decimal_places=1, blank=True)  # białko
    fat = models.DecimalField(max_digits=3, decimal_places=1, blank=True)      # tłuszcz
    carbo = models.DecimalField(max_digits=3, decimal_places=1, blank=True)    # węglowodany
    fibre = models.DecimalField(max_digits=3, decimal_places=1, blank=True)    # błonnik
    category = models.CharField(max_length=50)
    product_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Products"
        
    def __str__(self):
        return self.product
