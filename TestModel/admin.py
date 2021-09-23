from django.contrib import admin
from TestModel.models import Food, Order, OrderItem

# Register your models here.
admin.site.register(Food)

admin.site.register(Order)

admin.site.register(OrderItem)