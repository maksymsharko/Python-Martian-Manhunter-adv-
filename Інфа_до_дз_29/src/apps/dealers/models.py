from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class Dealer(models.Model):
    title = models.CharField(
        max_length=100,
    )
    email = models.EmailField(
        max_length=25,
        unique=True,
    )
    city = models.ForeignKey(
        'dealers.City',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
    )

    class Meta:
        verbose_name = 'Диллер'
        verbose_name_plural = 'Диллери'

    def __str__(self):
        return self.title


class City(models.Model):
    name = models.CharField(
        max_length=50,
    )
    country = models.ForeignKey(
        'dealers.Country',
        on_delete=models.CASCADE,
        related_name='cities',
    )

    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(
        max_length=50,
    )
    code = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Країна'
        verbose_name_plural = 'Країни'

    def __str__(self):
        return self.name


class NewsLetter(models.Model):
    email = models.EmailField(
        max_length=100,
    )

    class Meta:
        verbose_name = 'Новий лист'
        verbose_name_plural = 'Нові листи'

    def __str__(self):
        return self.email