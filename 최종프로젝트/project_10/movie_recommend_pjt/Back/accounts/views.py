from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import UserSerializers, SignupSerializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['POST'])
def signup(request):
    serializer = SignupSerializers(data=request.data)
    password = request.data.get('password')
    if serializer.is_valid(raise_exception=True):
        # 비밀번호 해싱
        if serializer.validated_data.get('password') == serializer.validated_data.get('password2'):
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    pass


@api_view(['GET'])
def profile(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserSerializers(user)
    return Response(serializer.data)