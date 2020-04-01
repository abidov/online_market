from rest_framework import viewsets, status
from .models import ProductItem
from .serializers import ProductItemSerializer
from products.models import Product
from rest_framework.decorators import action


class ProductItemViewSet(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    