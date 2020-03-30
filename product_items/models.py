from django.db import models
from products.models import Product
# Create your models here.

class ProductItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
  colour = models.CharField(max_length=255, null=False)
  size = models.CharField(max_length=255, null=False)
  quantity = models.PositiveSmallIntegerField()
  
  def __str__(self):
    return f'{self.product.title} {self.colour} {self.size}'