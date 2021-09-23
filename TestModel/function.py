from django.shortcuts import render
from TestModel.models import Food, Order, OrderItem
# Create your views here.

def get_all():
    result = Food.objects.all()
    return result


def get_price(foodID):
    result = Food.objects.get(id=int(foodID))
    return  result.price


def make_order(orderInfor):
    contentList = orderInfor['content']
    buffer = ""
    for i in contentList:
        buffer += str(i['id']) + ":" + str(i['number']) + ";"

    print(buffer + "  " + orderInfor['amount'])

    tmp = Order(payType=orderInfor['payType'], eatingType=orderInfor['eatType'], amount=orderInfor['amount'], orderContent=buffer)
    tmp.save()


    