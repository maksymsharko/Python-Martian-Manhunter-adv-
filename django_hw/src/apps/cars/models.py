from django.db import models
from django.contrib.auth import get_user_model

AUTH_USER_MODEL = get_user_model()


class Car(models.Model):
    POLLUTANT_AA = 'a+'
    POLLUTANT_A = 'a'
    POLLUTANT_B = 'b'
    POLLUTANT_C = 'c'
    POLLUTANT_D = 'd'
    POLLUTANT_E = 'e'
    POLLUTANT_F = 'f'
    POLLUTANT_G = 'g'

    POLLUTANT_CHOICES = (
        (POLLUTANT_AA, 'A+'),
        (POLLUTANT_A, 'A'),
        (POLLUTANT_B, 'B'),
        (POLLUTANT_C, 'C'),
        (POLLUTANT_E, 'E'),
        (POLLUTANT_F, 'F'),
        (POLLUTANT_G, 'G'),
    )
    GEAR_BOX_MANUAL = 'manual transmission'
    GEAR_BOX_AUTOMATIC = 'automatic transmission'
    GEAR_BOX_AUTOMATIC_VARIATOR = 'automatic variator transmission'
    GEAR_BOX_AUTOMATIC_ROBOTIC = 'automatic robotic transmission'
    GEAR_BOX_CHOICES = (
        (GEAR_BOX_MANUAL, 'Manual Transmission'),
        (GEAR_BOX_AUTOMATIC, 'Automatic Transmission'),
        (GEAR_BOX_AUTOMATIC_VARIATOR, 'Automatic Variator Transmission'),
        (GEAR_BOX_AUTOMATIC_ROBOTIC, 'Automatic Robotic Transmission'),

    )
    STATUS_PENDING = 'pending'
    STATUS_PUBLISH = 'publish'
    STATUS_SOLD = 'sold'
    STATUS_ARCHIVED = 'archived'

    STATUS_CHOICES = (
        (STATUS_PENDING, 'Pending Car Sell'),
        (STATUS_PUBLISH, 'Published'),
        (STATUS_SOLD, 'Sold'),
        (STATUS_ARCHIVED, 'Archived'),
    )
    FUEL_PETROL = 'petrol'
    FUEL_DIESEL = 'diesel'
    FUEL_PETROL_GAS = 'gas and petrol'
    FUEL_HYBRID = 'hybrid'

    FUEL_CHOICES = (
        (FUEL_PETROL, 'Petrol'),
        (FUEL_DIESEL, 'Diesel'),
        (FUEL_PETROL_GAS, 'Gas and Petrol'),
        (FUEL_HYBRID, 'Hybrid'),
    )
    color = models.ForeignKey(
        'cars.Color',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    dealer = models.ForeignKey(
        'dealers.Dealer',
        on_delete=models.CASCADE,
        null=True,
        related_name='cars',
    )
    model = models.ForeignKey(
        'cars.Model',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    engine_type = models.CharField(
        max_length=25,
        default=0,
    )
    pollutant_type = models.CharField(
        max_length=10,
        choices=POLLUTANT_CHOICES,
        default=POLLUTANT_AA,
        blank=True,
    )
    price = models.PositiveIntegerField(
        default=0
    )
    fuel_type = models.CharField(
        max_length=25,
        choices=FUEL_CHOICES,
        default=FUEL_DIESEL,
    )
    status = models.CharField(
        max_length=25,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
        blank=True,
    )
    doors = models.PositiveIntegerField(
        default=4,
    )
    capacity = models.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    gear_case = models.CharField(
        max_length=255,
        choices=GEAR_BOX_CHOICES,
        default=GEAR_BOX_MANUAL,
    )
    number = models.CharField(
        max_length=25,
    )
    slug = models.SlugField(
        max_length=100,
    )
    sitting_place = models.PositiveSmallIntegerField(
        default=5,
    )
    first_date_registration = models.DateTimeField(
        auto_now_add=True,
    )
    engine_power = models.PositiveSmallIntegerField()

    class Meta:
        #abstract = True
        verbose_name = 'Машина'
        verbose_name_plural = 'Машини'

    def __str__(self):
        return self. slug


class Color(models.Model):
    name = models.CharField(
        max_length=40,
    )

    class Meta:
        verbose_name = 'Колір'
        verbose_name_plural = 'Кольори'

    def __str__(self):
        return self.name


class Model(models.Model):
    brand = models.ForeignKey(
        'cars.Brand',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=100,
    )

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Моделі'

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'


class Picture(models.Model):
    url = models.ImageField(
        upload_to='picture/%Y%M%D',
        null=True,
        blank=True,
    )
    position = models.IntegerField()
    metadata = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

    def __str__(self):
        return self.url.name


class Property(models.Model):
    CATEGORY_PASSENGER = 'passenger'
    CATEGORY_TRUCK = 'truck'
    CATEGORY_BUS = 'bus'

    CATEGORY_CHOICES = (
        (CATEGORY_PASSENGER, 'Passenger'),
        (CATEGORY_TRUCK, 'Truck'),
        (CATEGORY_BUS, 'Bus'),
    )
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_PASSENGER,
    )
    name = models.CharField(
        max_length=255,
    )

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name





