# Generated by Django 4.2.16 on 2024-11-20 06:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieTitle', models.CharField(max_length=80)),
                ('movieContent', models.TextField()),
                ('movieDirector', models.CharField(max_length=200)),
                ('movieActor', models.CharField(max_length=200)),
                ('movieOpenDate', models.DateField()),
                ('movieVote', models.FloatField()),
                ('movieRunTime', models.IntegerField()),
                ('movieCountry', models.CharField(max_length=50)),
                ('moviePoster', models.CharField(max_length=255)),
                ('genres', models.ManyToManyField(related_name='movie_genres', to='movies.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentContent', models.TextField()),
                ('commentCreate', models.DateField(auto_now_add=True)),
                ('commentUpdate', models.DateField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_comment', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
