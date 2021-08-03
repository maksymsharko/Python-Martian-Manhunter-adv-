# Generated by Django 3.2.6 on 2021-08-03 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Місто',
                'verbose_name_plural': 'Міста',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Країна',
                'verbose_name_plural': 'Країни',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_the_dish', models.CharField(max_length=64)),
                ('ingredients', models.TextField()),
            ],
            options={
                'verbose_name': 'Страва',
                'verbose_name_plural': 'Страви',
            },
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Працівник',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('owner', models.CharField(max_length=64)),
                ('status', models.CharField(blank=True, choices=[('opened', 'Opened'), ('closed', 'Closed')], default='opened', max_length=64)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='restaurant.city')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.country')),
                ('personal', models.ManyToManyField(to='restaurant.Personal')),
            ],
            options={
                'verbose_name': 'Ресторан',
                'verbose_name_plural': 'Ресторани',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('season_dish', models.CharField(blank=True, choices=[('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'), ('autumn', 'Autumn')], default='summer', max_length=64)),
                ('list_of_dishes', models.ManyToManyField(to='restaurant.Dish')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
