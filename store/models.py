from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]
        verbose_name = "Category"
        db_table = 'category'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        permissions = [('increase_price', 'Product can increase price')]
        verbose_name_plural = "products"
        verbose_name = "Product"
        db_table = 'product'
        ordering = ["name"]
