# movies/models.py

from django.db import models

class Movie(models.Model):
    # Movie title
    title = models.CharField(max_length=300)
    # Year of release
    year = models.CharField(max_length=10)
    # IMDb ID (unique identifier)
    imdb_id = models.CharField(max_length=50, unique=True)
    # Type of the movie (e.g., movie, series)
    type = models.CharField(max_length=50)
    # URL to the movie poster
    poster = models.URLField(max_length=300)
    
    rated = models.CharField(max_length=100)

    released = models.CharField(max_length=100)

    runtime = models.CharField(max_length = 100)

    genre = models.CharField(max_length=250)

    plot = models.CharField(max_length=1000)

    language = models.CharField(max_length =100)

    

    def __str__(self):
        return self.title  # String representation of the model
