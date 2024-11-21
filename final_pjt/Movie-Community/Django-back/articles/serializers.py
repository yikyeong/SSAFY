from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Movie, Article, Comment


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    movie = MoviesSerializer()    
    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    # movie = MoviesSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

class CommentsListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    article = ArticleSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    
    class Meta:
        model = Comment
        fields = '__all__'


