# Generated by Django 4.1.7 on 2023-03-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('EUR', 'Euro'), ('USD', 'Dollar'), ('RUB', 'Rubles')], default='RUB', max_length=3),
        ),
    ]
