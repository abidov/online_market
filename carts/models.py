from django.db import models
from django.contrib.auth.models import User
from products.models import ProductItem
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

class Cart(models.Model):
  user = models.OneToOneField(User, related_name='cart', on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username

@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
  if created:
    Cart.objects.create(user=instance)


class CartItem(models.Model):
  cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE, null=True, blank=True)
  product = models.ForeignKey(ProductItem, related_name='product_items', on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
