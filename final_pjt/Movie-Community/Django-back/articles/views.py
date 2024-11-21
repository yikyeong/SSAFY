import json
# 0615 19:51 추가 ↓
import sqlite3
import urllib.request as UR
import os
import psycopg2
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .models import Article, Comment, Movie
from .serializers import *

flag = False
df = pd.DataFrame(columns=['id', 'title', 'nouns', 'poster'])
entire_nouns = set()

@api_view(['GET'])
def init_get_data(request):  # 홈
    global flag, entire_nouns
    DATABASE_URL = os.environ['DATABASE_URL']
    if not flag:
        con = psycopg2.connect(DATABASE_URL, sslmode='require')
        cur = con.cursor()
        cur.execute("SELECT ID, TITLE, NOUNS, POSTER FROM articles_movie")
        res = cur.fetchall()
        con.close()

        NOUNS = []
        for i, t, n, p in res:
            NOUNS.append(n)
            df.loc[len(df)] = [i, t, n, p]

        # prev_calc_sim()
        for N in NOUNS:  # 명사 모음집을 set으로 구성한다.
            entire_nouns |= set(N.split())
        flag = True
        return Response({"result": "success"})
    return Response({"result": "fail"})


@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_movie(request):

    words = list(entire_nouns)
    new_nouns_data = []
    for word in words:
        if word in request.data['overview']: new_nouns_data.append(word)
    
    new_nouns = ' '.join(new_nouns_data)
    if new_nouns:
        movies = Movie.objects.all()
        request.data['nouns'] = new_nouns
        if not movies.filter(id=request.data['id']).exists():
            serializer = MoviesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(id=request.data['id'])
                last_idx = len(df)
                df.loc[last_idx] = [request.data['id'], request.data['title'], new_nouns, request.data['poster']]
                # prev_calc_sim()

                return Response(serializer.data)
    return HttpResponse(status=404)

@api_view(['GET'])
def search_movie(request, keyword):
    movies = Movie.objects.filter(title__contains=keyword)
    serializers = MoviesSerializer(movies, many=True)
    return Response(serializers.data)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def read_movies(request):
    movies = Movie.objects.all()
    serializers = MoviesSerializer(movies, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def read_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MoviesSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def read_articles(request):
    articles = Article.objects.order_by('-pk')
    serializers = ArticleListSerializer(articles, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def read_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user == article.user:
        article.delete()
        return Response({'result': 'success'})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
    serializer = CommentSerializer(data=request.data)
    # article값을 저장해야함    
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def read_comments(request, article_id):
    comments = Comment.objects.filter(article_id=article_id).order_by('-pk')
    serializers = CommentsListSerializer(comments, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_comment(request, article_id, comment_id):
    comment = get_object_or_404(Comment, article_id=article_id, pk=comment_id)
    if request.user == comment.user:
        comment.delete()
        return Response({'result': 'success'})



#------------------------------------------------------재호 작업

## 06-17 01:21 수정------------------------------------------------
@api_view(['GET'])
def recommend_movie(request, like_movie_id): # '추천 영화' 항목을 눌렀을 때 실행.
    do_vectorize = CountVectorizer()
    nouns_vectorize = do_vectorize.fit_transform(df['nouns'])
    nouns_sim = cosine_similarity(nouns_vectorize, nouns_vectorize).argsort()[:, ::-1]
    
    result = []
    target_index = df[df['id'] == like_movie_id].index.values
    sim_index = nouns_sim[target_index, :9].reshape(-1)

    
    for idx in sim_index:  
        if idx == target_index: continue
        result_dic = {'title':df.iloc[idx]['title'], 'poster':df.iloc[idx]['poster']}
        result.append(result_dic)

    return Response(result)
