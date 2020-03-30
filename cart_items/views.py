from django.shortcuts import render
from rest_framework import generics
from .serializers import CartItemSerializer
from product_items.models import ProductItem
from .models import CartItem
from carts.models import Cart

# Create your views here.
class CartItemCreateView(generics.CreateAPIView):
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        product_item = ProductItem.objects.get(pk=self.kwargs['pk'])
        serializer.save(product=product_item, cart=self.request.user.cart)

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    
    def get_queryset(self):
        cart_items = Cart.objects.get(user=self.request.user).items.all()
        return cart_items