from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Food, Order
from TestModel import function as fc
from django.views.decorators.csrf import csrf_protect

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
import xhtml2pdf.pisa as pisa
import json



FOOD_CARD = '<div class="card menuItem" style="width: 18rem;">' + \
                '<img class="card-img-top" src="/static/img/food.jpg" alt="Card image cap">' + \
                 '<div class="card-body">'+\
                     '<h5 class="card-title" id="{}-name">{}</h5>' + \
                    '<p class="card-title" >${}</p>' + \
                        '<input type="hidden" id = "{}-price" value={}>' + \
                      '<div class="orderCount">' + \
                          '<input type="number" name="count" id = "{}-number"style="width:30%;" value=0></input>' + \
                         '<button class="btn btn-primary order" id="{}">Order</button>' +\
                     '</div>'+\
                '</div>'+\
            '</div>'


def main(request):
    return render(request, 'main/main.html')


def order(request):
    result = fc.get_all()
    htmlContent = []
    for i in result:
        htmlContent.append(FOOD_CARD.format(i.id, i.name,i.price, i.id, i.price, i.id, i.id))
    return render(request, 'order/order.html', {"food": result, "html": htmlContent, "eatType": request.GET.get("type")})


def orderDetail(request):
    return render(request, 'order/orderDetail.html')


def checkout(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST
        order = {}
        order['content'] = json.loads(data.get('order'))
        order['payType'] = data.get('payType')
        order['eatType'] = data.get('eatType')
        order['amount'] = data.get('amount')

        fc.make_order(order)

        
    return JsonResponse({"result": "ajax on Django works"})


def test(request):
    html = "<h1>Hooooo sad </h1>"
    response = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)


