from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    genreType = models.CharField(max_length=50)

class Movie(models.Model):
    movieTitle = models.CharField(max_length=80)
    movieContent = models.TextField()
    movieDirector = models.CharField(max_length=200)
    movieActor = models.CharField(max_length=200)
    movieOpenDate = models.DateField()
    movieVote = models.FloatField()
    movieRunTime = models.IntegerField()
    movieCountry = models.CharField(max_length=20)
    posterUrl = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre, related_name="movie_genres")
    
class Poster(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    posterUrl = models.CharField(max_length=500)

class Link(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    linkUrl = models.CharField(max_length=500, blank=True, null=True)

class Comment (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    commentContent = models.TextField()
    commentUpdate = models.DateField(auto_now=True)