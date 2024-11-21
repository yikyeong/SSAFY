from rest_framework import serializers
from .models import Actor,Movie,Review

class ActorListSerializer(serializers.ModelSerializer):
    class Meta :
        model = Actor
        fields = ('id', 'name')

class ActorDetailSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta :
            model = Movie
            fields = ('title',)
    
    movies= MovieTitleSerializer(read_only=True, many=True)
    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies',)

class MovieListSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Movie
        fields = ('title', 'overview',)
    

class MovieDetailSerializer(serializers.ModelSerializer):
    class ActorNamesSerializer(serializers.ModelSerializer):
        class Meta :
            model = Actor
            fields = ('name',)
    
    class ReviewSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('title', 'content')
    
    actors = ActorNamesSerializer(many=True, read_only=True)
    review_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors', 'review_set', 'title', 'overview', 'release_date', 'poster_path',)

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title', 'content')

class ReviewDetailSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer):
        class Meta :
            model = Movie
            fields = ('title',)
    movie = MovieTitleSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id','movie','title', 'content')        