from django.db import models
from django.contrib.auth.models import User
from product_items.models import ProductItem

class Cart(models.Model):
  user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username
