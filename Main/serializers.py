from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Seller
        fields = ('user', 'category')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
