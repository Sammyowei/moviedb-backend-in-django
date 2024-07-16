# movies/urls.py

from django.urls import path
from .views import search_movie, get_movie, delete_movielist

urlpatterns = [
    path('search/', search_movie, name='search_movie'),  # Endpoint for searching movies
    path('movie/<str:imdb_id>/', get_movie, name='get_movie'),  # Endpoint for retrieving movie by IMDb ID
    path('movies/delete/', delete_movielist, name='delete_movie_list'),
    # path('movies/all', all_movies, name='all_movies'),
]
