from rest_framework import serializers
from .models import Cart, CartItem
from accounts.serializers import UserSerializer
from products.serializers import ProductItemSerializer
from products.models import ProductItem

class CartItemSerializer(serializers.HyperlinkedModelSerializer):
    product = ProductItemSerializer(read_only=True)
    class Meta:
        model = CartItem
        fields = ['url', 'product', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ['cart_items', 'price']

class CartItemCreateSerializer(serializers.ModelSerializer):
    product = ProductItemSerializer(read_only=True)
    cart = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'cart']
    
    def validate(self, data):
        product_item = ProductItem.objects.get(pk=self.context['pk'])
        if data['quantity'] > product_item.quantity:
            raise serializers.ValidationError('''Quantity must be less or equal to product's quantity''')
        return data