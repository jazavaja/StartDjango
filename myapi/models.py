from django.db import models


# Create your models here.

class ProductApi(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product_api'


class AuthorApi(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'author_api'

    def __str__(self):
        return self.name


class BookApi(models.Model):
    author = models.ForeignKey(AuthorApi, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=150)

    class Meta:
        db_table = 'books_api'
    def __str__(self):
        return self.title
