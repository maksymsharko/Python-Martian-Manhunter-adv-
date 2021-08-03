from django.contrib import admin
from restaurant.models import Restaurant, Dish, Personal, City, Country, Menu

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Personal)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Menu)
