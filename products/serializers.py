from rest_framework import serializers
from .models import Product
from product_items.serializers import ProductItemSerializer

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    items = ProductItemSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = ['url','title', 'description', 'category', 'price', 'items']