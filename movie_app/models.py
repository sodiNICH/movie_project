from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Movie(models.Model):
    EURO = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(100),
                                             ])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True,
                                 validators=[
                                     MinValueValidator(1),
                                     MaxValueValidator(10000000),
                                 ])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=(self.slug,))

    def __str__(self):
        return f'{self.name} - {self.rating}%'

#  python manage.py shell_plus --print-sql
#  from movie_app.models import Movie
