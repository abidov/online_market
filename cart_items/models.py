from django.db import models
from carts.models import Cart
from product_items.models import ProductItem

# Create your models here.
class CartItem(models.Model):
  cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE, null=True, blank=True)
  product = models.ForeignKey(ProductItem, related_name='items', on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1, null=True, blank=True)