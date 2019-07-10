from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        # fields = '__all__' # - jeśli wszystkie pola
        fields = ('id', 'url', 'product', 'kcal', 'protein', 'fat', 'carbo', 'fibre')