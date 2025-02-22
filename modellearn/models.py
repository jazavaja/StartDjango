from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password


# Create your models here.


class Person(AbstractUser):
    age = models.IntegerField(default=18)
    mobile = models.CharField(unique=True, max_length=13, null=True, blank=True)
    sex = models.BooleanField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'person'
        ordering = ['create_at']
        verbose_name_plural = 'person ha'
        verbose_name = 'person'


class Student(models.Model):
    person = models.OneToOneField(Person, models.CASCADE)
    iq = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = "student"


class PersonAddress(models.Model):
    person = models.ForeignKey(Person, models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        db_table = "person_address"
