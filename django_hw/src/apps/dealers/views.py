from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.core import serializers
from src.apps.dealers.models import Dealer


class DealerListView(ListView):
    model = Dealer
    context_object_name = 'orders'
    template_name = 'dealers/list.html'

    def get_queryset(self):
        return Dealer.objects.all()


class DealerDetailView(DetailView):
    model = Dealer
    context_object_name = 'orders'
    pk_url_kwarg = 'dealer_pk'
    template_name = 'dealers/detail.html'


def serialize_dealers(request):
    data = serializers.serialize('json', Dealer.objects.all())
    return HttpResponse(request.method + '<br>' + data)