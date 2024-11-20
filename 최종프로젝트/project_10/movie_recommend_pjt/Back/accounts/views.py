from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)