from django.db import models
from categories.models import Category

# Create your models here.
class Product(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField('Description')
  category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  slug = models.SlugField()

  def get_all_categories(self):
    try:
      ancestors = self.category.get_ancestors(include_self=True)
    except:
      ancestors = []
    return ancestors

  def __str__(self):
    return self.title
