from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name_plural = 'categories'

    def get_all_products(self):
        try:
          descendants = self.get_descendants(include_self=True)
        except:
          descendants = []
        products = []
        for category in descendants:
          for product in category.products.all():
            products.append(product)
        return products


    def __str__(self):
        return self.name
