from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=100)
    mobile = models.CharField(unique=True, max_length=13, null=True, blank=True)
    sex = models.BooleanField(blank=True, null=True)
    password = models.CharField(max_length=250, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)

        super().save(*args, **kwargs)

    class Meta:
        db_table = 'human'
        ordering = ['create_at']
        verbose_name_plural = 'personha'
        verbose_name = 'person'
