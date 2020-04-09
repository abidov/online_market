from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from carts.models import CartItem
from .models import Product, ProductItem
from .serializers import ProductSerializer, ProductItemSerializer, ProductDetailSerializer, ProductItemDetailSerializer
from categories.serializers import CategorySerializer
from django.shortcuts import get_object_or_404


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductDetailSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def get_categories_of_product(self, request, pk=None):
        categories = Product.objects.get(pk=pk).get_all_categories()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ProductItemViewSet(viewsets.ModelViewSet):
    serializer_class = ProductItemSerializer
    queryset = ProductItem.objects.all()

    def retrieve(self, request, pk=None):
        queryset = ProductItem.objects.all()
        product_item = get_object_or_404(queryset, pk=pk)
        serializer = ProductItemDetailSerializer(product_item, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=True)
    def add_to_cart(self, request, pk=None):
        product_item = ProductItem.objects.get(pk=pk)
