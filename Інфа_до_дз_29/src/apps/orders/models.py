from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    car = models.ForeignKey(
        'cars.Car',
        on_delete=models.CASCADE,
    )
    status = models.CharField(
        max_length=50,
    )
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(
        max_length=50,
    )
    email = models.EmailField(
        max_length=30,
    )
    phone = PhoneNumberField(
        null=False,
        blank=False,
        unique=False,
    )
    message = models.TextField(max_length=255)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'