from django.db import models
from django.db.models.signals import post_save
from django_extensions.db.models import TimeStampedModel #A Django model that adds created_at and updated_at fields by default.
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from FreeMarket.settings import base

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.name

class Seller(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    price = models.PositiveIntegerField()
    description = models.TextField()

class Service(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    #not sure
