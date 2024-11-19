<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light">
      <a class="navbar-brand text-danger font-weight-bold title">
        <router-link class="text-danger font-weight-bold title" to="/">HONGFLIX</router-link>
      </a>

      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li v-if="!nowUser" class="nav-item">
            <a class="nav-link">
              <router-link class="text-white" :to="{name: 'Signup'}">Signup</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a v-if="!nowUser" class="nav-link">
              <router-link class="text-white" :to="{name: 'Login'}">Login</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a v-if="nowUser" class="nav-link">
              <router-link class="text-white" :to="{name: 'ChooseLikeMovieView'}">Choose Like Movie</router-link>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link">
              <router-link class="text-white" :to="{name: 'Articles'}">Articles</router-link>
            </a>
          </li>
          <li v-if="nowUser" class="nav-item">
            <a class="nav-link">
              <router-link class="text-white" :to="{name: 'CreateArticle'}">New Article</router-link>
            </a>
          </li>
          <li v-if="isSuperUser" class="nav-item">
            <a class="nav-link">
              <router-link class="text-white" :to="{name: 'SearchMovie'}">New Movie</router-link>
            </a>
          </li>
        </ul>
        <a class="navbar-brand text-info mr-0">
          <span v-if="nowUser">{{nowUser}}님   </span>안녕하세요
        </a>
        <ul class="navbar-nav mr-0">
          <li v-if="nowUser" class="nav-item">
            <a class="nav-link">
              <router-link class="text-white" :to="{name: 'Logout'}">LOGOUT</router-link>
            </a>
          </li>
        </ul>
      </div>
    </nav>
    <router-view
      class="container"
      @send-logindata="login"
      @logout="logout"
      @send-signupdata="signup"
      @read-user="readUser"
      @read-movies="readMovies"
      @read-articles="readArticles"
      @read-article="readArticle"
      @search-movie="searchMovie"
      @search-movie-in-database="searchMovieInDatabase"
      @create-movie="createMovie"
      @create-article="createArticle"
      @delete-article="deleteArticle"
      @send-commentdata="createComment"
      @read-comments="readComments"
      @delete-comment="deleteComment"
      @register-like-movie="registerLikeMovie"
      @init-data="initData"
      :articles="articles"
      :movies="movies"
      :selectedArticle="selectedArticle"
      :comments="comments"
      :searchedMovies="searchedMovies"
      :selectedMovie="selectedMovie"
      :isSuperUser="isSuperUser"
      :nowUser="nowUser"
      :searchedMoviesInDatabase="searchedMoviesInDatabase"
      :likeMovie="likeMovie"
      :likeMovieID="likeMovieID"
      :recommendMovies="recommendMovies"
    />
  </div>
</template>

<script>
import axios from "axios";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;
const TMDB_API_KEY = process.env.VUE_APP_TMDB_API_KEY;

export default {
  data() {
    return {
      articles: null,
      movies: null,
      selectedArticle: null,
      comments: null,
      searchedMovies: null,
      selectedMovie: null,
      nowUser: null,
      isSuperUser: null,
      searchedMoviesInDatabase: null,
      likeMovieID: null,
      likeMovie: null,
      recommendMovies: null
    };
  },
  methods: {
    signup(signupData) {
      axios
        .post(SERVER_URL + "/rest-auth/registration/", signupData)
        .then(res => {
          this.$cookies.set("auth-token", res.data.key);
          this.$cookies.set("username", signupData.username);
          this.nowUser = signupData.username;
          this.$router.push({ name: "ChooseLikeMovieView" });
        })
        .catch(() => alert("정보가 올바르지 않습니다."));
    },
    login(loginData) {
      axios
        .post(SERVER_URL + "/rest-auth/login/", loginData)
        .then(res => {
          this.$cookies.set("auth-token", res.data.key);
          this.$cookies.set("username", loginData.username);
          this.nowUser = loginData.username;
          this.$router.push({ name: "Home" });
        })
        .then(() => {
          if (this.$cookies.get("auth-token")) {
            const config = {
              headers: {
                Authorization: `Token ${this.$cookies.get("auth-token")}`
              }
            };
            axios
              .post(
                SERVER_URL + `/read/user/${this.$cookies.get("username")}/`,
                null,
                config
              )
              .then(res => {
                this.likeMovieID = res.data.like_movie;
                if (res.data.is_superuser) {
                  this.$cookies.set("superuser", "super");
                  this.isSuperUser = "super";
                }
              })
              .catch(err => console.log(err.response.data));
          }
        })
        .catch(() => alert("정보가 올바르지 않습니다."));
    },
    logout() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(SERVER_URL + "/rest-auth/logout/", null, config)
        .catch(err => console.log(err.response.data))
        .finally(() => {
          this.$cookies.remove("auth-token");
          this.$cookies.remove("username");
          this.$cookies.remove("superuser");
          this.nowUser = null;
          this.isSuperUser = null;
          this.likeMovieID = null;
          this.likeMovie = null;
          this.recommendMovies = null;
        });
    },
    readUser() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(
          SERVER_URL + `/read/user/${this.$cookies.get("username")}/`,
          null,
          config
        )
        .then(res1 => {
          axios
            .get(SERVER_URL + `/read/movie/${res1.data.like_movie}/`)
            .then(res2 => {
              this.likeMovie = res2.data.title;
              this.likeMovieID = res2.data.id;
            })
            .then(
              axios
                .get(SERVER_URL + `/recommend/movie/${res1.data.like_movie}/`)
                .then(res3 => (this.recommendMovies = res3.data))
                .catch(err => console.log(err.response.data))
            )
            .catch(err => console.log(err.response.data));
        })
        .catch(err => console.log(err.response.data));
    },
    registerLikeMovie(movieId) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(
          SERVER_URL +
            `/register/likemovie/${this.$cookies.get("username")}/${movieId}`,
          null,
          config
        )
        .then(() => {})
        .catch(err => console.log(err.response.data));
      this.$router.go();
    },
    readMovies() {
      axios
        .get(SERVER_URL + "/read/movies/")
        .then(res => (this.movies = res.data))
        .catch(err => console.log(err));
    },
    searchMovie(movieTitle) {
      axios
        .get("https://api.themoviedb.org/3/search/movie", {
          params: {
            api_key: TMDB_API_KEY,
            query: movieTitle,
            language: "ko-KR",
            page: 1,
            include_adult: false
          }
        })
        .then(res => (this.searchedMovies = res.data.results))
        .catch(err => console.log(err));
      this.$router.push({ name: "CreateMovie" });
    },
    searchMovieInDatabase(searchKeyword) {
      axios
        .get(SERVER_URL + `/search/movie/${searchKeyword}/`)
        .then(res => (this.searchedMoviesInDatabase = res.data))
        .catch(err => console.log(err.response.data));
    },
    createMovie(movieData) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(
          SERVER_URL + "/create/movie/",
          {
            id: movieData.id,
            title: movieData.title,
            release_date: movieData.release_date,
            vote_sum: movieData.vote_count,
            vote_avg: movieData.vote_average,
            overview: movieData.overview,
            poster: `https://image.tmdb.org/t/p/w500${movieData.poster_path}`,
            genres: movieData.genre_ids
          },
          config
        )
        .then(() => {
          alert(
            "영화가 등록되었습니다. 이미 등록된 영화이거나 적합하지 않은 영화는 등록이 취소됩니다."
          );
          this.$router.push({ name: "Home" });
        })
        .catch(() => {
          alert(
            "영화가 등록되었습니다. 이미 등록된 영화이거나 적합하지 않은 영화는 등록이 취소됩니다."
          );
          this.$router.push({ name: "Home" });
        });
    },
    readArticles() {
      axios
        .get(SERVER_URL + "/read/articles/")
        .then(res => (this.articles = res.data))
        .catch(err => console.log(err));
      this.selectedArticle = null;
      this.selectedMovie = null;
      this.comments = null;
    },
    createArticle(articleData) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(SERVER_URL + "/create/article/", articleData, config)
        .then(res => {
          this.$router.push({
            name: "ArticleView",
            params: { id: res.data.id }
          });
        })
        .catch(() => alert("올바르지 않은 정보입니다."));
    },
    async readArticle(id) {
      try {
        const res = await axios.get(SERVER_URL + `/read/article/${id}`);
        this.selectedArticle = res.data;
        axios
          .get(SERVER_URL + `/read/movie/${this.selectedArticle.movie}`)
          .then(res => (this.selectedMovie = res.data))
          .catch(err => console.log(err));
      } catch (err) {
        console.error(err);
      }
    },
    deleteArticle(articleID) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(SERVER_URL + `/delete/article/${articleID}/`, null, config)
        .then(() => {
          this.$router.push({name: 'Articles'})
        })
        .catch(() => {
          alert('본인글만 삭제할 수 있습니다.')
          this.$router.go()
        })
    },
    createComment(commentData) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(SERVER_URL + "/create/comment/", commentData, config)
        .then(() => {})
        .catch(err => console.log(err));
      this.$router.go();
    },
    async readComments(articleID) {
      try {
        const res = await axios.get(
          SERVER_URL + `/read/article/${articleID}/comments/`
        );
        this.comments = res.data;
      } catch (err) {
        console.error(err);
      }
    },
    deleteComment(commentData) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(SERVER_URL + `/delete/article/${commentData.articleID}/comment/${commentData.commentID}/`, null, config)
        .then(() => {
          this.$router.go()
        })
        .catch(() => {
          alert('본인의 댓글만 삭제할 수 있습니다.')
        })

    },
    initData() {
      axios
        .get(SERVER_URL + "/")
        .then(res => console.log(res.data))
        .catch(err => console.log(err));
    }
  },
  created() {
    this.nowUser = this.$cookies.get("username");
    this.isSuperUser = this.$cookies.get("superuser");
  }
};
</script>

<style>
.title {
  font-size: 2rem;
}
.title:hover {
  text-decoration: none;
}
</style>
