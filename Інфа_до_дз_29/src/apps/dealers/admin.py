from django.contrib import admin

from src.apps.dealers.models import Dealer, City, Country, NewsLetter

admin.site.register(Dealer)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(NewsLetter)