# models.py
from django.db import models
import django.utils.timezone as timezone 

class Food(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=20, default="food", choices=[("Beef","Beef"), ("Pork","Pork"), ("Duck", "Duck")])
    price = models.FloatField(default=16.0)



class OrderItem(models.Model):
    orderID = models.IntegerField()
    food = models.ForeignKey("Food", on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    itemAmount = models.FloatField(default=0.0)


class Order(models.Model):
    time = models.TimeField(default=timezone.now)
    date =models.DateField(default=timezone.now)

    amount = models.FloatField(default=0)
    payType = models.CharField(max_length=20, default="Card", choices=[("Card","Card"), ("Cash","Cash")])
    eatingType = models.CharField(max_length=20, default="DineIn", choices=[("DineIn","DineIn"), ("TakeAway","TakeAway")])
    orderContent = models.CharField(max_length=999)
