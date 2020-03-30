from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import CartSerializer
from market.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from .models import Cart

# Create your views here.
class CartView(generics.RetrieveDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsOwner,)
    
    def get_object(self):
        try:
            cart = self.request.user.cart
        except:
            cart = Cart.objects.create(user=self.request.user)
        return cart

class CartCreateView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
