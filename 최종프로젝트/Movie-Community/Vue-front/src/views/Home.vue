<template>
  <div class="home">
    <h1 v-if="!recommendMovies" class="text-center">
      <div class="text-white font-weight-bold display-1 bg-danger mb-4">HONG JAE HO'S</div>
      <div class="text-white font-weight-bold display-4">MOVIE RECOMMEND</div>
      <div class="text-white font-weight-bold display-4">HOME PAGE</div>
      <div class="text-white font-weight-bold display-4">(made by hongjae jaeho, 20200617)</div>
    </h1>

    <div v-else>
      <h1 class="text-center text-white font-weight-bold">추 천 영 화</h1>
      <div class="row mt-4">
        <div v-for="recommendMovie in recommendMovies" :key="recommendMovie.poster" class="col-lg-3 col-sm-6">
          <img :src="recommendMovie.poster" class="img-fluid rounded mb-2" alt="movie-poster" />
          <h5 class="text-center text-white">{{recommendMovie.title}}</h5>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  props: {
    recommendMovies: Array,
    likeMovieID: Number,
    nowUser: String
  },
  methods: {
    initData() {
      this.$emit("init-data");
    },
    readUser() {
      this.$emit("read-user");
    }
  },
  created() {
    this.initData();
    if (this.$cookies.get("username") && !this.recommendMovies) {
      this.readUser();
    }
  }
};
</script>
<style scoped>
.home {
  height: 100wh;
}
</style>
