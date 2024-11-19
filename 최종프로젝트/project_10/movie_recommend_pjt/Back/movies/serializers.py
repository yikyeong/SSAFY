from rest_framework import serializers
from .models import Genre, Movie,Poster

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    posters = PosterSerializer(many=True)
    class Meta : 
        model = Movie
        fields = '__all__'
