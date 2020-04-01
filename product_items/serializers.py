from rest_framework import serializers
from .models import ProductItem

class ProductItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['url' ,'colour', 'size', 'quantity']