from email.policy import default
from random import choices
from termios import PENDIN
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField
    description = models.TextField
    # photo = models.ImageField


class MenuFoodItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    stock = models.IntegerField(default=1)


class OrderItem(models.Model):
    fooditem = models.ForeignKey(MenuFoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

class Order(models.Model):

    class OrderStatus(models.TextChoices):
        SETTLED = 'STLD', _('Settled')
        FAILED = 'FAIL', _('Failed')
        PENDING = 'PEND', _('Pending')


    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=100)
    client_email = models.EmailField
    total_charge = models.FloatField    
    client_location = models.TextField
    status = models.CharField(max_length = 7, choices=OrderStatus.choices, default=OrderStatus.PENDING)






    