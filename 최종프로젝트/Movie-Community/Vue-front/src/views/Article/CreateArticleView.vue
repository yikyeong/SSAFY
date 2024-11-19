<template>
  <div>
    <h1 class="text-center text-white font-weight-bold">새 글쓰기</h1>
    <form>
      <div class="form-group">
        <label for="title" class="text-white d-inline mr-3">제목</label>
        <small id="emailHelp" class="form-text text-muted d-inline">제목은 100자 이내로 써주세요.</small>

        <input
          v-model="articleData.title"
          type="text"
          class="form-control"
          id="title"
          aria-describedby="emailHelp"
        />
      </div>
      <div class="form-group">
        <label for="like-movie" class="text-white d-inline mr-3">영화</label>
        <small id="emailHelp" class="form-text text-muted d-inline">영화는 검색 후 선택해 주세요.</small>
        <input
          type="text"
          class="form-control"
          id="like-movie"
          aria-describedby="emailHelp"
          v-model="searchKeyword"
        />
      </div>
    </form>
    <div class="d-flex justify-content-end">
      <button @click="searchMovieInDatabase" class="btn btn-danger">검색</button>
    </div>
    <form class="mt-2 form-group">
      <label for="movie" class="text-white d-inline mr-3">검색된 영화</label>
        <small id="emailHelp" class="form-text text-muted d-inline">화살표를 눌러 영화를 선택해 주세요.</small>

      <select class="form-control" id="movie" v-model="articleData.movie">
        <option
          v-for="searchMovie in searchedMoviesInDatabase"
          :key="searchMovie.id"
          :value="searchMovie.id"
        >{{searchMovie.title}}</option>
      </select>
    </form>
    <form>
      <div class="form-group">
        <label for="rank" class="text-white d-inline mr-3">평점</label>
        <small id="emailHelp" class="form-text text-muted d-inline">평점은 0~5점 사이입니다. (소수점 입력가능)</small>
        <input v-model="articleData.rank" type="text" class="form-control" id="rank" />
      </div>
      <div class="form-group">
        <label for="content" class="text-white d-inline mr-3">내용</label>
        
        <small id="emailHelp" class="form-text text-muted d-inline">욕설 및 비방글은 제재합니다.</small>
        <textarea v-model="articleData.content" class="form-control" id="content" cols="3"></textarea>
      </div>
    </form>
    <div class="d-flex justify-content-end mb-3">
      <button @click="createArticle" class="btn btn-primary">글 작성</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CreateArticleView",
  props: {
    searchedMoviesInDatabase: Array,
    movies: Array
  },
  data() {
    return {
      articleData: {
        title: null,
        rank: null,
        content: null,
        movie: null
      },
      searchKeyword: null
    };
  },
  methods: {
    readMovies() {
      this.$emit("read-movies");
    },
    createArticle() {
      console.log(this.articleData);
      this.$emit("create-article", this.articleData);
    },
    searchMovieInDatabase() {
      this.$emit("search-movie-in-database", this.searchKeyword);
    }
  },
  created() {
    if (!this.$cookies.get("username")) {
      this.$router.push({ name: "Login" });
    }
  }
};
</script>

<style>
</style>