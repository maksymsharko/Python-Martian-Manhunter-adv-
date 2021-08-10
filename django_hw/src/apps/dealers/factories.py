import factory


class DealerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.Dealer'

    title = 'Ukranian dealer'
    email = ''


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Country'

    name = 'Ukraine'
    email = 'dealer@gmail.com'
    user_id = 1
    city_id = 1


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'dealer.City'

    name = 'Komarno'

