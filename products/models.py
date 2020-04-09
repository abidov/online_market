from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField('Description')
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def get_all_categories(self):
    try:
      ancestors = self.category.get_ancestors(include_self=True)
    except:
      ancestors = []
    return ancestors

  def __str__(self):
    return self.title


class ProductItem(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
  colour = models.CharField(max_length=255, null=False)
  size = models.CharField(max_length=255, null=False)
  quantity = models.PositiveSmallIntegerField()
  
  def __str__(self):
    return f'{self.product.title} {self.colour} {self.size}'