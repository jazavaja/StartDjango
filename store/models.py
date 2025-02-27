import os

from django.core.exceptions import ValidationError
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


# -----------------------PRODUCT START--------------------------


def max_upload_with_ext(file):
    max_upload_size = 500 * 1024
    if file.size > max_upload_size:
        raise ValidationError('File too large')
    my_ext = os.path.splitext(file.name)[1]
    valid_ext = ['.jpg', '.jpeg', '.png']
    if my_ext.lower() not in valid_ext:
        raise ValidationError('please attention picture extension must be jpg or jpeg or png')


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to='products/', null=True, blank=True, validators=[max_upload_with_ext])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        permissions = [('increase_price', 'Product can increase price')]
        verbose_name_plural = "products"
        verbose_name = "Product"
        db_table = 'product'
        ordering = ["name"]

# -----------------------PRODUCT END--------------------------
