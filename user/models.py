from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import EmailValidator
from django.db import models

from modellearn.models import Person


# Create your models here.
# Here You can see Model custom with Abstract Base User
# We must  use Just One Model user

class UserCustomManager(BaseUserManager):
    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError('User must have a email')
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault('is_staff', True)
        extra.setdefault('is_superuser', True)

        if extra.get('is_staff') is not True:
            raise ValueError('Is staff must true')
        return self.create_user(email, password, **extra)


class User(AbstractBaseUser):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=100)
    email = models.EmailField(unique=True, validators=[EmailValidator])
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=128, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserCustomManager()

    REQUIRED_FIELDS = ['name', 'family']
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = "user_custom"
        ordering = ['name']
        verbose_name_plural = 'کاربران'
        verbose_name = 'کاربر'


class Profile(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE)
    bio = models.TextField()
    location = models.CharField(max_length=150, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pic/", null=True, blank=True)

    def __str__(self):
        return self.user.username
