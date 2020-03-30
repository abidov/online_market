from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from categories.serializers import CategorySerializer

# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        product = Product.objects.get(pk=self.kwargs['pk'])
        return product.get_all_categories()