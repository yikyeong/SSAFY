from rest_framework import serializers
from .models import Genre, Movie, Comment, UserSelectedGenre
from accounts.serializers import UserSerializer

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class UserSelectedGenreSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # username 표시
    genre = GenreSerializer()  # 장르 정보를 포함

    class Meta:
        model = UserSelectedGenre
        fields = ['user', 'genre',]

class MovieListSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Movie
        fields = ('moviePoster', 'movieTitle', 'movieVote')

class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta : 
        model = Movie
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer()
    user = UserSerializer()
    class Meta : 
        model = Comment
        fields = '__all__'
