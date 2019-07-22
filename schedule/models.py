from django.db import models
from django.contrib import admin
from datetime import datetime
from recipes.models import Recipes

class Schedule(models.Model):
    when = models.DateTimeField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    portion = models.DecimalField(max_digits=2, decimal_places=1, default=1)

    class Meta:
        verbose_name_plural = "Schedule"


