from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieForm
from django.views.decorators.http import require_http_methods, require_safe

# Create your views here.
def index(request):     # 전체 영화 데이터 조회
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request, 'movies/index.html', context)

def create(request):    # 영화 데이터 작성 폼 출력
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else :
        form = MovieForm()
    context = {
        'form' : form
    }
    return render(request,'movies/create.html',context)

def detail(request, pk):    # 단일 영화 데이터 목록 조회
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie' : movie
    }
    return render(request, 'movies/detail.html', context)

def update(request,pk):    # 영화 수정 페이지 조회, 유효성 검증, 데이터 수정
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else :
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form' : form
    }
    return render(request, 'movies/update.html', context)

def delete(request, pk):    # 영화 데이터 삭제
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

# @require_http_methods(["GET", "POST"])
# def create(request):
#     if request.method == "POST": # 만들 내용을 적었으면
#         form = MovieForm(request.POST) # form을 만들고
#         if form.is_valid(): # form이 유효하면
#             movie = form.save() # 저장하고
#             return redirect("movies:index") # 메인페이지로 이동
#     else: # POST가 아니라면
#         form = MovieForm() # 비어있는 form 받고
#     # method == POST이면 form = MovieForm(request.POST)
#     # method != POST이면 form = MovieForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, "movies/create.html", context)

# def update(request,movie_pk):
#     movie = Movie.objects.get(pk=movie_pk) # update할 movie를 가져오고
#     if request.method == "POST": # 수정했으면
#         # 수정한 내용과 수정하기 전 내용 포함해서 form 만들기
#         form = MovieForm(request.POST, instance=movie)
#         if form.is_valid(): # form이 유효하면
#             form.save() # form을 저장하고
#             return redirect('movies:detail', movie.pk) # detail페이지로 이동
#     else: # POST가 아니면
#         form = MovieForm(instance=movie) # 수정하기 전 내용을 form 에 담고
#     # method == POST이면 form = MovieForm(request.POST,instance=movie)
#     # method != POST이면 form = MovieForm(instance=movie)
#     context = {
#         'form' : form,
#         'movie' : movie,
#     }
#     # 수정하는 페이지로 이동
#     return render(request, 'movies/update.html', context)
