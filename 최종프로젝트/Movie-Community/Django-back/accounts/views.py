from django.shortcuts import render, get_object_or_404
from .serializers import UserSerializer
from .models import User

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def read_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response({
        "username": "",
        "result": "본인만 조회 가능합니다."
    })

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_like_movie(request, username, movie_pk):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        user.like_movie = movie_pk
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    return Response({
        "username": "",
        "result": "본인만 조회 가능합니다."
    })
        
