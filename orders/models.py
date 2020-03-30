from django.db import models
from django.contrib.auth.models import User
from product_items.models import ProductItem
# Create your models here.
class Order(models.Model):
  user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
  product = models.ForeignKey(ProductItem, related_name='order_items', on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)