import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from django.db import models
from django.contrib.auth.models import AbstractUser
from articles.models import Movie

# Create your models here.
class User(AbstractUser):
    like_movie = models.IntegerField(default=109445)
