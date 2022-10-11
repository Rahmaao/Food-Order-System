from email.policy import default
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
    stock = models.IntegerField


class OrderItem(models.Model):
    fooditem = models.ForeignKey(MenuFoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

class Order(models.Model):
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=100)
    client_email = models.EmailField
    # orderitem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    total_charge = models.FloatField    
    client_location = models.TextField
    status = models.BooleanField(default=False)

    class OrderStatus(models.TextChoices):
        SETTLED = 'STLD', _('Settled')
        FAILED = 'FAIL', _('Failed')
        Pending = 'PEND', _('Pending')




    