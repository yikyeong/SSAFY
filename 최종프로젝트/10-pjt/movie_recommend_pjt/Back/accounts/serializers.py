from rest_framework import serializers
from .models import User
# from movies.serializers import GenreSerializer

class UserSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True)
    class Meta:
        model = User
        fields = ('username', 'genres')
