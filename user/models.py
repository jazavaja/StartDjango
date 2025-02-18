from django.db import models
from django.core.validators import EmailValidator
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=100)
    email = models.EmailField(unique=True,validators=[EmailValidator])
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'