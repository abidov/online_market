from rest_framework import serializers
from products.models import ProductItem
from products.serializers import ProductItemSerializer
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    cart = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Order
        fields = ['cart', 'price']
        read_only_fields = ['price', 'cart']


class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    cart = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Order
        fields = ['cart', 'price', 'created', 'updated']