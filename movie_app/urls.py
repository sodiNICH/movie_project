from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.one_all_movie, name='movie-detail')
]