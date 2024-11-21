from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import User

# User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','is_superuser', 'like_movie',)