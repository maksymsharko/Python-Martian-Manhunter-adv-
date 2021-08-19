from django.core import serializers
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from src.apps.orders.models import Order


class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders/list.html'

    def get_queryset(self):
        return Order.objects.all()


class DetailOrderView(DetailView):
    model = Order
    context_object_name = 'orders'
    pk_url_kwarg = 'order_pk'
    template_name = 'orders/detail.html'


def serialize_orders(request):
    data = serializers.serialize('json', Order.objects.all())
    return HttpResponse(request.method + '<br>' + data)
