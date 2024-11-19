from rest_framework import serializers
from .models import User
from movies.serializers import GenreSerializer

class UserSerializers(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'userImage', 'genres', 'email')

class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'userImage', 'genres', 'password')
        extra_kwargs = {
            'password': {'write_only': True},  # 비밀번호 보안 추가
        }