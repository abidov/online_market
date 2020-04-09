from django.db import models
from django.contrib.auth.models import User
from carts.models import CartItem
# Create your models here.

class Order(models.Model):
  user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, null=True, blank=True)
  cart = models.ForeignKey(CartItem, related_name='orders', on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)