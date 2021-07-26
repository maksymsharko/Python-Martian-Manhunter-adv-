from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def status(request):
    return HttpResponse("OK")


def return_random_color(request):
    rand = lambda: random.randint(0, 255)
    color = '#%02X%02X%02X' % (rand(), rand(), rand())
    html = f"<html><body bgcolor={color}>Color: {color}</body></html>"
    return HttpResponse(html)


