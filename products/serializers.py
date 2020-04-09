from rest_framework import serializers
from .models import Product, ProductItem

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['url', 'title', 'description', 'category', 'price']

class ProductItemSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProductItem
        fields = ['url', 'product', 'colour', 'size', 'quantity']

class ProductItemDetailSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedIdentityField(view_name='product-detail')
    add_to_cart = serializers.HyperlinkedIdentityField(view_name='cartitem-create')
    class Meta:
        model = ProductItem
        fields = ['colour', 'size', 'quantity', 'product', 'add_to_cart']


class ProductDetailSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedIdentityField(view_name='productitem-detail')
    class Meta:
        model = Product
        fields = ['title', 'description', 'category', 'price', 'items']

