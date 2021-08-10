from django.views.generic import ListView, DetailView
from src.apps.cars.models import Car
from django.core import serializers
from django.http import HttpResponse


class CarListView(ListView):
    model = Car.objects.all()
    context_object_name = 'cars'
    template_name = 'cars/list.html'

    def get_queryset(self):
        return Car.objects.all()


class CarsDetailBoardView(DetailView):
    model = Car
    slug_url_kwarg = 'car_slug'
    context_object_name = 'cars'
    template_name = 'cars/detail.html'
    #queryset = Car.objects.all()


def serialize_car(request):
    data = serializers.serialize('json', Car.objects.all())
    return HttpResponse(request.method + '<br>' + data)

