import factory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'orders.Order'

    first_name = 'Maksym'
    second_name = 'Sharko'
    email = 'maks.sharko02@gmail.com'
    phone = '+380686868686'
    card_id = 10
