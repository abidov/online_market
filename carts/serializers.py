from rest_framework import serializers
from .models import Cart
from accounts.serializers import UserSerializer
from cart_items.serializers import CartItemSerializer

class CartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    items = CartItemSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ['user', 'items']