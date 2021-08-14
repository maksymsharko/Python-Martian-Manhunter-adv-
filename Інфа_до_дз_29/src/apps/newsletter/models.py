from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Новий лист'
        verbose_name_plural = 'Нові листи'

