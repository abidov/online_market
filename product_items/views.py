from django.shortcuts import render
from rest_framework import generics
from .models import ProductItem
from .serializers import ProductItemSerializer
from products.models import Product
# Create your views here.

class ProductItemListView(generics.ListAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

class ProductItemCreateView(generics.CreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    def perform_create(self, serializer):
        serializer.save(product=Product.objects.get(pk=self.kwargs['pk']))

class ProductItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer

