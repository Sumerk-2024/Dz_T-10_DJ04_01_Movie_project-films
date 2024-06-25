from django.urls import path
from .views import add_movie, movie_list

urlpatterns = [
    path('add/', add_movie, name='add_movie'),
    path('', movie_list, name='movie_list'),
]
