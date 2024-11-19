from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_sum = models.IntegerField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    nouns = models.TextField()
    
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_article')
    title = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_article')
    content = models.TextField()
    rank = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    