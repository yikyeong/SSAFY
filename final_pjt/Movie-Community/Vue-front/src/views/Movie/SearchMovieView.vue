<template>
  <div>
    <h1 class="text-white font-weight-bold mb-5">새로운 영화</h1>
    <form class="mb-0">
      <div class="form-group mb-0">
        <label for="movietitle" class="text-white d-inline mr-3">영화 제목</label>
        <small id="emailHelp" class="form-text text-muted d-inline">영화제목을 검색하면 결과가 나타납니다.</small>
      </div>
    </form>
        <input
          id="movietitle"
          v-model="movieTitle"
          type="text"
          class="form-control mb-2 mt-0"
          aria-describedby="emailHelp"
          @keyup.enter="searchMovie"
        />
    <div class="d-flex justify-content-end">
      <button @click="searchMovie" class="btn btn-danger">검색</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchMovieView",
  data() {
    return {
      movieTitle: null
    };
  },
  methods: {
    searchMovie() {
      this.$emit("search-movie", this.movieTitle);
    }
  },
  created() {
    if (!this.$cookies.get("superuser")) {
      this.$router.push({ name: "Home" });
    }
  }
};
</script>

<style>
</style>