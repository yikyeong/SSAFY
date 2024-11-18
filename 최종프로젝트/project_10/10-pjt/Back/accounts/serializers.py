from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = ('userName', 'userImage', 'genres', 'email')

class SignupSerializers(serializers.ModelSerializers):
    class Meta:
        model = User
        fields = ('userName', 'userImage', 'genres')