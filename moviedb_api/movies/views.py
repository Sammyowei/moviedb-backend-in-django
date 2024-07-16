# movies/views.py

import requests
from django.conf import settings
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer
from .config import OMDB_API_KEY
from django.core import serializers

# OMDB API key (replace with your actual key


@api_view(['GET'])
def search_movie(request):
    """
    Endpoint to search for a movie by title using the OMDB API.
    """
    # Get the title from the query parameters
    title = request.GET.get('title')
    if not title:
        return Response({'error': 'Title parameter is required'}, status=400)

    # Generate a cache key using the movie title
    cache_key = f"movie_{title}"
    # Try to get the cached movie data
    cached_movie = cache.get(cache_key)

    if cached_movie:
        # Return the cached movie data if available
        return Response(cached_movie)

    # Make a request to the OMDB API to search for the movie
    response = requests.get(f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}')
    if response.status_code == 200:
        data = response.json()

        
        if data['Response'] == 'True':
            # Extract and structure the movie data
            movie_data = {
            "title": data['Title'],
            # Year of release
            "year": data['Year'],
            # IMDb ID (unique identifier)
            "imdb_id":data['imdbID'],
            # Type of the movie (e.g., movie, series)
            "type": data['Type'],
            # URL to the movie poster
            "poster":data['Poster'],
            
            "rated" :data['Rated'],

            "released" :data['Released'],

            "runtime" :data['Runtime'],

            "genre" :data['Genre'],

            "plot" :data['Plot'],

            "language" :data['Language'],
            }
            # Cache the movie data for future requests
            cache.set(cache_key, movie_data, timeout=settings.CACHE_TTL)
            return Response(movie_data)
        else:
            return Response({'error': 'Movie not found'}, status=404)
    else:
        return Response({'error': 'Failed to fetch data from OMDB'}, status=500)

@api_view(['GET'])
def get_movie(request, imdb_id):
    """
    Endpoint to retrieve a movie by its IMDb ID from the local database.
    """
    # Retrieve the movie from the database or return 404 if not found
    movie = get_object_or_404(Movie, imdb_id=imdb_id)
    # Serialize the movie data
    serializer = MovieSerializer(movie)
    return Response(serializer.data)



@api_view(['GET'])
def delete_movielist(request):
    Movie.objects.all().delete()

    return Response({"message": "Deleted all sucessfully"})


# @api_view(('GET'))
# def all_movies(request):
#     # movies = Movie.objects.all()

#     # serialized_movies = serializers.serialize('json', movies)

#     return Response({"movies": ''})