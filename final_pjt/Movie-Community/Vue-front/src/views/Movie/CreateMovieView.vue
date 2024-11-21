<template>
  <div>
    <table class="table table-hover table-borderless table-dark">
      <thead>
        <tr>
          <th scope="col">
            <h1 class="font-weight-bold">검색된 결과</h1>
          </th>
          <th scope="col"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="searchedMovie in searchedMovies" :key="searchedMovie.id">
          <td scope="row">{{searchedMovie.title}}</td>

          <td>
            <button @click="createMovie(searchedMovie)" class="btn btn-primary">등록</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "CreateMovieview",
  props: {
    searchedMovies: Array
  },
  methods: {
    createMovie(searchedMovie) {
      console.log(searchedMovie);
      this.$emit("create-movie", searchedMovie);
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