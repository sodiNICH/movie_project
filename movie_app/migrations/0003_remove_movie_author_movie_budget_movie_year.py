# Generated by Django 4.1.7 on 2023-03-06 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_movie_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='author',
        ),
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default=1000000),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True),
        ),
    ]
