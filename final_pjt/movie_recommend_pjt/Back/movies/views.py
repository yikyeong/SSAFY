
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Movie, Comment
from .serializers import MovieListSerializer, MovieDetailSerializer, CommentSerializer

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)

def read_comment(request, movie_id):
    comment = Comment.objects.filter(movie_id=movie_id).order_by('-commentCreate')
    serializer = CommentSerializer(comment)
    return Response(serializer.data)