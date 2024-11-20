from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    genreType = models.CharField(max_length=100)

class Movie(models.Model):
    movieTitle = models.CharField(max_length=80)
    movieContent = models.TextField()
    movieDirector = models.CharField(max_length=200)
    movieActor = models.CharField(max_length=200)
    movieOpenDate = models.DateField()
    movieVote = models.FloatField()
    movieRunTime = models.IntegerField()
    movieCountry = models.CharField(max_length=50)
    moviePoster = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name="movie_genres")

class Comment (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_comment')
    commentContent = models.TextField()
    commentCreate = models.DateField(auto_now_add=True)
    commentUpdate = models.DateField(auto_now=True)