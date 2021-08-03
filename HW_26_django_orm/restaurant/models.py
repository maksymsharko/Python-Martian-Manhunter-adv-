from django.db import models


class Restaurant(models.Model):
    STATUS_OPENED = 'opened'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = (
        (STATUS_OPENED, "Opened"),
        (STATUS_CLOSED, "Closed"),
    )

    name = models.CharField(
        max_length=64,
        blank=False
    )
    owner = models.CharField(
        max_length=64,
        blank=False
    )
    status = models.CharField(
        max_length=64,
        choices=STATUS_CHOICES,
        default=STATUS_OPENED,
        blank=True
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        related_name='cities'
    )
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE
    )
    personal = models.ManyToManyField(
        'Personal'
    )

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Ресторани'

    def __str__(self):
        return self.name


class Personal(models.Model):
    first_name = models.CharField(
        max_length=64,
        blank=False
    )
    last_name = models.CharField(
        max_length=64,
        blank=False
    )
    position = models.CharField(
        max_length=64,
        blank=False
    )

    class Meta:
        verbose_name = 'Працівник'
        verbose_name_plural = 'Персонал'

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.position}'


class Country(models.Model):
    country = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(
        max_length=64
    )

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'

    def __str__(self):
        return self.city


class Dish(models.Model):
    name_of_the_dish = models.CharField(
        max_length=64
    )
    price = models.DecimalField
    weight = models.IntegerField
    ingredients = models.TextField()

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'

    def __str__(self):
        return self.name_of_the_dish


class Menu(models.Model):
    SEASON_WINTER = 'winter'
    SEASON_SPRING = 'spring'
    SEASON_SUMMER = 'summer'
    SEASON_AUTUMN = 'autumn'

    SEASON_CHOICES = (
        (SEASON_WINTER, 'Winter'),
        (SEASON_SPRING, 'Spring'),
        (SEASON_SUMMER, 'Summer'),
        (SEASON_AUTUMN, 'Autumn'),
    )

    name = models.CharField(
        max_length=64
    )
    list_of_dishes = models.ManyToManyField(
        Dish
    )
    season_dish = models.CharField(
        max_length=64,
        choices=SEASON_CHOICES,
        default=SEASON_SUMMER,
        blank=True,
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name
