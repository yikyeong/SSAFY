import requests
import json
import sqlite3

con = sqlite3.connect("example.db")

api_key = "2103434b666fc1533fbb046838915b7c"
api_access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMTAzNDM0YjY2NmZjMTUzM2ZiYjA0NjgzODkxNWI3YyIsIm5iZiI6MTczMjAxMzg2Mi45MjA1Mzg0LCJzdWIiOiI2NzM2ZDdiZmQ2M2ZlZDU4MjZjZjQ1MzAiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.YwgWVOa6yqwxWB6AppFNHTXe4bMPpgxgBbPPgWCw7Vk"
host = "https://api.themoviedb.org"


def api_call_movie_list():
    path = "/3/movie/popular"
    params = "api_key=2103434b666fc1533fbb046838915b7c&region=KR&language=ko&page="
    for i in range(1, 6):
        uri = host + path + "?" + params + str(i)
        response = requests.get(uri)
        if response.status_code == 200:
            # json_parser_default(response.text)
            json_object = json.loads(response.text)
            arr = json_object["results"]
            for obj in arr:
                movie_id = obj["id"]
                movie_title = obj["title"]
                movie_content = obj["overview"]
                movie_open_date = obj["release_date"]
                movie_vote = f"{obj['vote_average']:.1f}"
                movie_poster_url = obj["poster_path"]
                print(movie_id)
                # detail
                detail_path = (
                    "/3/movie/"
                    + str(movie_id)
                    + "?api_key=2103434b666fc1533fbb046838915b7c&region=KR&language=ko"
                )
                response_detail = requests.get(host + detail_path)
                if response_detail.status_code == 200:
                    json_object_detail = json.loads(response_detail.text)
                    movie_runtime = json_object_detail["runtime"]  # detail
                    movie_country = 0
                    origin_country = json_object_detail.get("origin_country", [])  # detail
                    if origin_country:  # 리스트가 비어있지 않으면
                        movie_country = origin_country[0]  # 첫 번째 값 가져오기
                    else:
                        movie_country = "정보 없음"  # 리스트가 비어있을 경우 기본값 설정
                    movie_genres = []
                    for genre in json_object_detail.get('genres', []):
                        genre_id = genre["id"]
                        genre_name = genre["name"]
                        movie_genres.append({"id": genre_id, "name": genre_name})
                    # print(movie_country)

                # credit
                detail_path = (
                    "/3/movie/"
                    + str(movie_id)
                    + "/credits?api_key=2103434b666fc1533fbb046838915b7c&region=KR&language=ko"
                )
                response_credit = requests.get(host + detail_path)
                if response_credit.status_code == 200:
                    json_object_credit = json.loads(response_credit.text)
                    arr1 = json_object_credit["cast"]
                    arr2 = json_object_credit["crew"]
                    movie_director = ""
                    movie_actor = ""

                    for obj in arr1:
                        if "order" in obj and int(obj["order"]) < 5:
                            movie_actor += obj["name"] + ", "  # credit department:
                        else:
                            continue

                    for obj in arr2:
                        if "department" in obj:
                            # print(obj['department'])
                            if obj["department"] == "Directing":  # 감독일 경우
                                movie_director = obj["name"]  # 감독 이름 저장 # yet
                        else:
                            continue

                    # print(movie_title)


def json_parser_default(response_body):
    json_object = json.loads(response_body)
    arr = json_object["results"]
    for obj in arr:
        movie_title = obj["title"]
        movie_content = obj["overview"]
        movie_director = obj["movie_director"]  # yet
        movie_actor = obj["poster_path"]  # credit department:
        movie_open_date = obj["release_date"]
        movie_vote = f"{obj['vote_average']:.1f}"
        movie_runtime = obj["poster_path"]  # detail
        movie_country = obj["poster_path"]  # detail
        movie_poster_url = obj["poster_path"]
        # print(movie_title)


def insert_movie_data():
    cur = con.cursor()


api_call_movie_list()

# Genre = {
#     "genres": [
#         {"id": 28, "name": "액션"},
#         {"id": 12, "name": "모험"},
#         {"id": 16, "name": "애니메이션"},
#         {"id": 35, "name": "코미디"},
#         {"id": 80, "name": "범죄"},
#         {"id": 99, "name": "다큐멘터리"},
#         {"id": 18, "name": "드라마"},
#         {"id": 10751, "name": "가족"},
#         {"id": 14, "name": "판타지"},
#         {"id": 36, "name": "역사"},
#         {"id": 27, "name": "공포"},
#         {"id": 10402, "name": "음악"},
#         {"id": 9648, "name": "미스터리"},
#         {"id": 10749, "name": "로맨스"},
#         {"id": 878, "name": "SF"},
#         {"id": 10770, "name": "TV 영화"},
#         {"id": 53, "name": "스릴러"},
#         {"id": 10752, "name": "전쟁"},
#         {"id": 37, "name": "서부"},
#     ]
# }

    # movieTitle 
    # movieContent
    # movieDirector
    # movieActor
    # movieOpenDate 
    # movieVote
    # movieRunTime
    # movieCountry
    # moviePoster
    # genres