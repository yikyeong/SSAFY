from django.db import models
from django.conf import settings
from accounts.models import User
# Create your models here.

class Genre(models.Model):
    genreId = models.IntegerField(unique=True)
    genreName = models.CharField(max_length=50)

class UserSelectedGenre(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selected_genres')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='selected_by_users')
    class Meta:
        unique_together = ('user', 'genre')  # 중복 선택 방지
    def __str__(self):
        return f'{self.user.username} - {self.genre.name}'

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
    commentCreate = models.DateTimeField(auto_now_add=True)
    commentUpdate = models.DateTimeField(auto_now=True)