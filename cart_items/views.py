from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import CartItemSerializer
from product_items.models import ProductItem
from .models import CartItem
from carts.models import Cart

# Create your views here.
# class CartItemCreateView(generics.CreateAPIView):
#     serializer_class = CartItemSerializer

#     def perform_create(self, serializer):
#         product_item = ProductItem.objects.get(pk=self.kwargs['pk'])
#         serializer.save(product=product_item, cart=self.request.user.cart)

# class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = CartItemSerializer
    
#     def get_queryset(self):
#         cart_items = Cart.objects.get(user=self.request.user).items.all()
#         return cart_items

class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_items = Cart.objects.get(user=self.request.user).items.all()
        return cart_items
    
    def get_object(self):
        return CartItem.objects.all(pk=self.kwargs['pk'])
    
    @action(methods=['GET'], detail=True)
    def add_product_item(self, request, pk):
        product_item = ProductItem.objects.get(pk=self.kwargs['pk'])
        CartItem.objects.create()


