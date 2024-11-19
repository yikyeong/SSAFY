from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('read/user/<str:username>/', views.read_user, name='read_user'),
    path('register/likemovie/<str:username>/<int:movie_pk>', views.update_like_movie, name='update_like_movie'),
]