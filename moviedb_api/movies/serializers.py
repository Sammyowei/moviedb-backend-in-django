# movies/serializers.py

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # Model to be serialized
        fields = '__all__'  # Serialize all fields
