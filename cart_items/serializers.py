from rest_framework import serializers
from .models import CartItem
from product_items.serializers import ProductItemSerializer

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductItemSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['product']