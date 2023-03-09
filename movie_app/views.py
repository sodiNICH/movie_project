from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie


def show_all_movie(request):
    # movies = Movie.objects.filter(rating__gt=70)
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_field=Value('hello'),
        int_field=Value(123),
        new_bidget=F('budget') + 100,
        sum_rating_and_year=F('rating') + F('year'),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    return render(request, 'movie_app/all_movie.html', {
        'movies': movies,
        'agg': agg,
    })


def one_all_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {
        'movie': movie
    })
