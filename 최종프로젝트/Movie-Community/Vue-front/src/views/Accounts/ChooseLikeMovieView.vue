<template>
  <div>
    <h1 class="text-white text-center font-weight-bold">
      좋아하는 영화를 설정해 주세요
      <span class="text-danger">♥</span>
    </h1>
    <h4 v-if="likeMovie" class="text-white mt-3">
      현재 설정된 영화:
      <span class="text-info">{{likeMovie}}</span>
    </h4>
    <form class="form-group mt-3 mb-0">
      <small id="emailHelp" class="form-text text-muted mb-0">좋아하는 영화를 검색해 주세요.</small>
    </form>
      <input
        type="text"
        class="form-control mt-0 mb-2"
        id="like-movie"
        aria-describedby="emailHelp"
        v-model="searchKeyword"
        @keyup.enter="searchMovieInDatabase"
      />
    <div class="d-flex justify-content-end">
      <button @click="searchMovieInDatabase" class="btn btn-danger">검색</button>
    </div>

    <form class="mt-4 form-group mb-2">
      <small class="form-text text-muted">원하는 결과를 선택해 주세요.</small>
      <select class="form-control" id="serchedmovie" v-model="likedMovieID">
        <option
          v-for="searchMovie in searchedMoviesInDatabase"
          :key="searchMovie.id"
          :value="searchMovie.id"
        >{{searchMovie.title}}</option>
      </select>
    </form>
    <div class="d-flex justify-content-end">
      <button @click="registerLikeMovie" class="btn btn-primary">등록</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchKeyword: null,
      likedMovieID: null
    };
  },
  props: {
    searchedMoviesInDatabase: Array,
    likeMovie: String
  },
  methods: {
    searchMovieInDatabase() {
      this.$emit("search-movie-in-database", this.searchKeyword);
    },
    registerLikeMovie() {
      this.$emit("register-like-movie", this.likedMovieID);
    },
    readUser() {
      this.$emit("read-user");
    }
  },
  created() {
    if (!this.$cookies.get("username")) {
      this.$router.push({ name: "Home" });
    } else {
      this.readUser();
    }
  }
};
</script>

<style>
</style>