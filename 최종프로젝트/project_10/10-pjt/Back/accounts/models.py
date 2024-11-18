from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Genre

# Create your models here.
class User(AbstractUser):
    userName = models.CharField(max_length=10)
    userImage = models.CharField(max_length=300, null=True, blank=True)
    genres = models.ManyToManyField(Genre, related_name='users', blank=True)
    # userId, userEmail, userPassword, userName, userImage 가 컬럼 

    def __str__(self):
        return self.userName
