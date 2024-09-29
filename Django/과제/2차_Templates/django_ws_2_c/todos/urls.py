from django.contrib import admin
from django.urls import path
from todos import views


app_name = 'coffee'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', views.index ),
    path('todos/create_todo/', views.create_todo),
    path('todos/<str:work2>/', views.detail , name = 'detail'),
]
