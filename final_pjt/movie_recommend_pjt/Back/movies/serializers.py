from rest_framework import serializers
from .models import Genre, Movie, Comment
from accounts.serializers import UserSerializer

# class GenreSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genre
#         fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    class Meta : 
        model = Movie
        fields = ('moviePoster', 'movieTitle', 'movieVote')

class MovieDetailSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    class Meta : 
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer()
    user = UserSerializer
    class Meta : 
        model = Comment
        fields = '__all__'
        read_only_fields = ('user',)
