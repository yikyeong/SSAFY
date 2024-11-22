from django.urls import path 
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/comment/', views.read_comment),
    # path('<int:movie_id>/comment/create', views.create_comment),
    # path('<int:movie_id>/comment/delete/<int:comment_id>', views.delete_comment),
]   
