# Final_Project

## 프로젝트 개요

### 기간

* 2020/06/11 - 2020/06/17

### 개요

* 영화 데이터 베이스를 가지고 영화관련 커뮤니티를 제작
* 사용자에게 영화를 추천해주는 알고리즘을 적용

### 개발환경

* Python 3.7 이상
* Django 2.1.15
* Node 12.18.x
* Vue 2.6
* TMDB영화 API를 이용해 최초 Database 구성
* Django REST API 서버 & Vue.js
  * Vue에서 props와 emit을 이용해 구현 
  * axios요쳥은 App.vue에서만 진행하도록 주요 methods를 App.vue로 모아서 관리

### 팀원

 * 엄홍재(팀장) : Full Stack - Django와 Vue를 이용한 웹페이지 제작

* 편재호(팀원) : 영화추천 알고리즘 개발 및 적용

### 배포

* Vue는 Netilfy 서버 이용
* Django는 Heroku 서버 이용
* 홈페이지: [HONGFLIX](https://gifted-murdock-8a50bc.netlify.app/)

### 기본 입력어(환경설정)

```bash
$ python -m venv venv
$ source venv/Source/activate
$ pip install requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata MovieDB.json
$ python manage.py runserver

$ npm i
$ npm run serve
```

## 프로젝트 진행과정

### 초기 DB 생성

TMDB의 API를 이용해 영화에 대한 평점을 기록한 사람(field_name:vote_sum)이 3500명 이상이고 영화등급이 19세 미만(adult=False)인 모든 장르의 영화를 받아 DB에 저장하였다.

영화추천 알고리즘에 사용하기 위해 줄거리(field_name:overview)에서 명사를 추출하여 각 명사를 띄워쓰기로 연결하여 하나의 String으로 만들어 nouns라는 필드를 생성하였다.

기존의 필드와 만드들어진 필드를 연결해 직접 JSON을 제작하였다.

```bash
$ python manage.py loaddata MovieDB.json
```

위의 명령어로 초기 DB입력



### 회원관리

#### Django DRF 생성

필요한 라이브러리 설치 작업

```bash
$ pip install djangorestframework
```

 [REST Framework 관련 공식문서](django-rest-framework.org/)

```bash
$ pip install django-rest-auth
```

[REST-AUTH 관련 공식문서](https://django-rest-auth.readthedocs.io/en/latest/installation.html)

```bash
$ pip install django-allauth
```

[Django-allauth 관련 공식문서](https://django-allauth.readthedocs.io/en/latest/installation.html)

생성된 URL

1. rest-auth/registration/
2. rest-auth/login/
3. rest-auth/logout/
4. read/user/(username)/

#### Vue - 회원기능

API를 위한 요청을 위해 axios 설치 :  `npm i axios`

Vue router 사용

로그인을 유지하기 위해 cookie를 이용

로그인을 함과 동시에 username을 이용해 관리자인지 좋아하는 영화가 무엇인지 axios요청을 통해 받아온다.

관리자 정보도 cookie에 저장해놓음.

로그인정보나 회원가입 정보가 일치하지 않다면 `alert`를 이용해 알림창을 뜨게 함.

로그아웃은 다른 브라우져에서 로그아웃 하였을 때 원래 사용하던 브라우져에는 유효하지 않은 토큰이 남아 있을 수 있어 `finally`로 구현하여 기존 브라우저에서도 토큰이 사라지게 만듦

### 영화관리(관리자)

관리자는 사용자가 요청하거나 필요한 영화를 추가 할 수 있다.

#### Django 영화추가

Vue에서 받아온 영화정보를 받아 DB에 저장함

Movie의 modeling

```python
class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_sum = models.IntegerField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    nouns = models.TextField()
```

생성된 URL

1. create/movie/

#### Vue - TMDB API

관리자인 경우 TMDB의 API를 이용하여 검색어와 관련된 영화를 추가할 수 있으며 추가될 때 기존 DB에 있는 nouns필드도 제작하여 DB에 추가,  이미 DB에 있는 영화이거나 적절하지 않은 영화인경우(overview가 존재하지 않는 영화 등)라면 추가되지 않는다.

```vue
axios.get("https://api.themoviedb.org/3/search/movie", {
          params: {
            api_key: TMDB_API_KEY,
            query: movieTitle,
            language: "ko-KR",
            page: 1,
            include_adult: false
          }
        })
```

### ARTICLE 관리

login한 사용자만 Article을 쓸 수 있고 모든 사용자는 Article의 내용을 볼 수 있다.

Article을 쓸 때에는 등록된 영화에 관련하여서만 쓸 수 있고 DB에 있는 영화 중 검색 가능하다.

본인만 본인이 작성한 Article을 삭제 할 수 있다. 만일 자신이 쓰지 않은 글에대해 삭제버튼을 누른다면 '본인만 글을 삭제할 수 있습니다.' 라는 알림창을 뜨게 구현하였다.

#### Django

Article의 modeling

```python
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_article')
    title = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_article')
    content = models.TextField()
    rank = models.FloatField(validators = [MinValueValidator(0.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

생성된 URL

1. read/movies - 검색기능 구현 전 영화 전체목록을 보여줄 때 사용, 검색기능을 구현 후 사용하지 않음
2. read/movie/(movie_id)/
3. search/movie/(keyword)/
4. create/article/
5. read/articles/
6. read/article/(article_id)/
7. delete/article/(article_id)/

#### Vue

구현한 페이지

1. 글 목록 보기

   1. `read/articles/`에 요청을 보내 존재하는 글 목록을 가져옴

2. 글 상세페이지

   1. 등록한 영화에 대해서 기본정보를 같이 등록해 주기 위해 영화의 정보를 읽어온다.

   2. `this.$route.params.id`을 통해 article의 ID값을 가져올 수 있다.

   3. 글을 작성한 시간(`created_at`)을 표현하기 위해 `moment.js`사용

      * ```bash
        $ npm install moment --save
        ```

      * computed를 이용해 날짜형식 지정

        ```vue
        computed: {
          createdArticleDate() {
            return this.$moment(this.selectedArticle.created_at).format(
              "YYYY-MM-DD A hh:mm:ss"
            );
          }
        }
        ```

3. 글 작성페이지

   1. 원하는 영화를 검색하기 위해 DB에서 검색하는 기능 추가

### 댓글 관리

로그인 한 사람만 댓글을 작성할 수 있다.

본인만 본인이 작성했던 댓글을 삭제할 수 있다.

사용자 누구나 댓글을 볼 수 있다.

#### Django

Comment의 modeling

```python
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comment')
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

생성된 URL

1. create/comment/
2. read/article/(article_id)/comments/
3. delete/article/(article_id)/comment/(comment_id)/

#### Vue

1. Aritlcle의 구현과 동일하게 구현

### 좋아하는 영화 관리

로그인 한 사용자는 자신이 좋아하는 영화를 하나 선택 할 수 있다.

회원가입과 동시에 가장먼저 좋아하는 영화를 선택하는 페이지로 이동한다.

만약, 좋아하지 않는 영화를 설정하지 않으면 기본값은 겨울왕국으로 설정되어 있다.

좋아하는 영화는 언제나 바꿀 수 있다.

좋아하는 영화를 기준으로 영화를 추천해주는 알고리즘이 작용한다.

#### Django

로그인한 사용자마다 좋아하는 영화를 가지고 있어야하기 때문에 User에 필드를 추가해 주어야 한다.

```python
class User(AbstractUser):
    like_movie = models.IntegerField(default=109445)
```

생성된 URL

1. register/likemovie/(username)/(movie_pk)/

위에서 이미 만든 영화 정보 가져오기, 영화 검색하기 등을 이용해 좋아하는 영화를 검색하는 기능을 구현한다.

#### Vue

1. 위의 URL로 axios요청을 보내 좋아하는 영화를 변경할 수 있게 만든다.

### 추천 알고리즘

#### 전체적인 구현

- Data의 Field값 중 하나인 `Overview`에서 '명사'만을 추출하여(자연어 모듈 사용) 새로운 Field인 `'nouns'`로 구성한다. 이 후,  각 Record(movie)들의 nouns를 기반으로 Cosine Similarity (scikit-learn 제공)를 구한 뒤, Descending sorting하여 상위 8개의 영화를 도출한다. 
- 즉, Input으로 제공된 영화의 줄거리와 가장 유사한 영화를 데이터베이스에서 찾아 Output으로 제공 하고자 한다.

#### 데이터 추출 및 구성(초기DB 설정)

 1. `TMDB`라는 영화정보 제공 사이트에서 open API를 이용하여 JSON 형태로 추출

    > 데이터는 TMDB에서 평점을 매긴 사용자의 수가 3500 이상인 영화들로 구성하였다.

 2. 데이터의 Contents에는 필요하지 않는 정보가 있기에, 필요한 데이터 Feature만으로 구성된 새로운 JSON 파일 구성

    > 제공된 정보 (Fields는 movie ID / movie Name / movie Release_Date / movie Poster_URLS / movie Genre / movie Overview)와 데이터 처리를 이용한 nouns필드를 이용해 JSON 형식으로 제작
    
3. 필요 데이터로 구성된 JSON을 저장하여, 사전에 Django DataBase에 구성 (sqlite3)

    > python에서 제공하는 sqlite3 module을 이용하여 import 시킨 뒤 시행하였다.

#### 데이터 처리

 1. Database에 저장하기 전, 영화의 줄거리를 기반으로 명사를 구해내야 하기에 한국어 자연어 처리 모듈인 `konlpy`를 이용하였다. 그리고 줄거리의 명사를 새로운 데이터 필드에 추가하여 Database를 구성하였다.

    > 영화가 관리자에 의해 새로 생성될 때에도 nouns 필드의 값을 제작하여 DB에 입력된다.

2. Database의 Value 값을 이용하기 위하여 DataFrame (pandas 제공)로 구성하는 과정을 가졌다.

     > sqlite3 모듈을 이용하여 필요한 필드의 값들을 Fetch 시켜, pandas에서 제공하는 DataFrame으로 구성하였다. 이를 통해 Vectorize (string의 vector화)시키고, 유사도를 측정할 수 있다.

#### 유사도 구현

1. DataFrame으로 구성된 영화 Records들의 nouns값들은 현재, String형태로 되어있기에 유사도 측정하기 위한 과정을 거쳤다. 먼저 scikit-learn에서 제공하는 CountVectorize 모듈을 이용하여 모든 nouns의 인자들을 BOW(Bag Of Words)로 구성한다.

	> 이 과정 또한 시간이 걸리기에, 서버가 첫 시작 혹은 Home으로 접근 할 때만 동작하여 BOW를 구성하도록 했다

2. 구현한 BOW값들의 Cosine_Similarity(scikit-learn)를 구하여 새로운 변수로 저장한다.

	> 동시에 내림차순으로 Sorting하여 가장 유사도가 높은 순으로 구성한다.

3. Input으로 들어온 영화 ID를 기반으로 DataFrame에서 Index를 찾으며, 이 Index를 이용해 코사인 유사도가 가장 높은 상위 8개의 영화를 Output으로 Return 한다.

	> Poster URL과 movie_name을 JSON 형태로 return함으로서, Front-end part에서 바로 이미지와 영화정보를 시각화 할 수 있게 한다.

#### Django

생성된 URL

1. / - 기본 페이지, 데이터를 생성하고 DB에서 필요한 필드만 추출하여 DataFrame을 만드는 과정
2. recommend/movie/(like_movie_id)/ - 좋아하는 영화 ID를 보내면 `views.py`에서 8개의 movie정보를 보내준다.

#### Vue

1. Home에 접속할 때마다 기본페이지에 요청을 보내 DataFrame을 생성을 시도함

 	2. DataFrame이 생성되어있다면 더 이상 생성하지 않음

### Design

* bootstrap을 이용한 반응형 웹 구현

### 배포

#### Django

Django는 Heroku를 이용하여 DRF구성

배포과정은 블로그를 참조함 - [Django 배포, Heroku](https://blog.naver.com/ice2745/221717831480)

1차 배포에서 생긴 문제 및 해결

* Heroku는 db.sqlite3를 사용하지 않음.

* 추천 알고리즘을 만들기 위해 아래의 코드처럼 전체 DB에서 필요한 필드값만 뽑아오는 작업을 해야하는데 할 수 없었다.

  ``` python
  con = sqlite3.connect('db.sqlite3')  # DB를 읽어오는 과정에서 문제가 생김
  ```

* Heroku 공식문서에서 DB를 읽어오는 방법을 찾아냄 [[관련 공식문서]](https://devcenter.heroku.com/articles/heroku-postgresql#connecting-in-python)

  ```bash
  $ pip install psycopg2-binary
  ```

  ```python
  import os
  import psycopg2
  
  DATABASE_URL = os.environ['DATABASE_URL']
  
  con = psycopg2.connect(DATABASE_URL, sslmode='require')
  ```

  

#### Vue

Vue는 Netlify를 이용해 배포함

SERVER_URL을 Heroku에 배포한 주소로 설정해줌

1차 배포에서 생긴 문제 및 해결

* router.go() 혹은 다른 페이지로 새로고침되며 redirect되는 경우 또는 URL로 직접접근 하는경우 404에러 발생
* Netlify홈페이지에서 DB를 읽어오는 방법을 찾아냄 [[관련 문서]](https://www.netlify.com/blog/2019/01/16/redirect-rules-for-all-how-to-configure-redirects-for-your-static-site/)
* `index.html`과 같은 위치에 `_redirects`라는 파일을 만들고 내용에 `/* /index.html 200`를 입력해 주면된다.

완성된 홈페이지: [HONGFLIX](https://gifted-murdock-8a50bc.netlify.app/)

## 구현과정 중 어려웠던 점

1. 초기 DB를 구성하는 것이 어려웠다. TMDB에서 받은 자료를 가공하는 과정이 생각보다 오래 걸렸다.
2. 알고리즘을 pycharm으로 실행했을 때 실행이 되지만 Django의 views.py로 넘어와 형식에 맞게 변환하고 실행되게 만드는 것이 어려웠다. (예: views.py의 전역변수는 어떻게 인식되는가)
3. Vue 라이프싸이클이 정확하게 언제 적용되는지 알기 힘들다.
4. 자연어 처리 모듈 중 NLTK(natural language toolkit)이라는 유명한 모듈이 있지만, 영문을 기반으로 처리하기에 한국어를 처리하기어려웠고, konlpy라는 한국어 자연어 처리 모듈을 찾아 프로젝트를 수행하였다.
5. konlpy의 문제는 속도가 느리며, JVM(Java Virtual Machine)을 사용하기에 환경을 구성하여 Views.py에 적용하기 힘들었다. 따라서 초기 DB에 대하여 데이터 필드를 JSON 형식으로 구성하여 입력하는 하는 결정을 하였다.

## 아쉬웠던 점 or 추가하고 싶은 기능

1. 다 구현해보고 싶었지만 구현못한 기능(주로 시간부족)이 생각보다 많다.
   * Article 수정
   * 댓글 수정
   * Article 좋아요
   * User정보
   * 팔로우
   * 페이지
2. 검색 버튼을 누르면 밑에 select 태그에 값이 나오면 좋겠다.
3. 관리자 계정에 대한 인증을 쿠키로 했는데 보안에 취약한 것 같다. 예를들면 쿠키에 적절한 값만 넣으면 관리자만 할 수 있는 영화를 추가할 수 있게된다.
4. 몇몇 사용자들이 검색을 할 때 띄어쓰기를 하지 않으면 검색이 되지 않는 것에 대해 불편해 했다.
5. 코드정리 + 간결화를 하고싶었지만 진행하지 못함.
6. 메인 method를 App.vue에 모아 놓은 것이 옳은 것인지 모르겠다. 각 페이지에 분리해서 했다면 조금 더 편했을까?

## 느낀 점

팀원과 밤을 새가며 함께 만들었다. 배포된 홈페이지를 보며 뿌듯했고 몇몇 글들을 사람들이 작성하는걸 보고 즐거웠다. 특히 좋아하는 영화를 바꾸면서 추천영화를 확인해 볼 때 신기하고 뿌듯했다. Vue와 Django의 전반적인 사용법에 대해 익힌 것 같다.  1학기의 학습내용을 전부 사용할 수 있는 좋은 시간이었다.