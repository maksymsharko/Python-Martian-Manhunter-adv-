from django.contrib import admin
from django.conf import settings
from src.apps.cars.models import Car, Color, Brand, Model, Picture, Property

admin.site.register(Car)
admin.site.register(Color)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Picture)
admin.site.register(Property)


