from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.init_get_data, name='init_get_data'),
    path('create/movie/', views.create_movie, name='create_movie'),
    path('read/movies/', views.read_movies, name='read_movies'),
    path('read/movie/<int:movie_id>/', views.read_movie, name='read_movie'),
    path('search/movie/<str:keyword>/', views.search_movie, name='search_movie'),
    path('recommend/movie/<int:like_movie_id>/', views.recommend_movie, name='recommend_movie'),
    path('create/article/', views.create_article, name='create_article'),
    path('read/articles/', views.read_articles, name='read_articles'),
    path('read/article/<int:article_id>/', views.read_article, name='read_article'),
    path('delete/article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('create/comment/', views.create_comment, name='create_comment'),
    path('read/article/<int:article_id>/comments/', views.read_comments, name='read_comments'),
    path('delete/article/<int:article_id>/comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]