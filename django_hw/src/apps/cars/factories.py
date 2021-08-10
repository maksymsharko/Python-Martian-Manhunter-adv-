import factory


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Car'

    number = 'BC 1111 AX'
    slug = 'it is a car'
    engine_power = 170
    dealer_id = 1
    color_id = 1
    model_id = 1
    picture_id = 1


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Brand'

    name = 'VW PASSAT B6'


class PropertyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Property'

    name = 'sedan'


class ColorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'cars.Color'

    name = 'black'
