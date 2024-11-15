<template>
  <div class="home">
    <h1 class="title">Welcome to the Movie Information App</h1>
    <p class="description">Discover the best-rated movies, watch trailers, and read reviews.</p>
    <router-link to="/movies" class="movie-link">View Top Rated Movies</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomeView',
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f0f0f0;
  text-align: center;
}

.title {
  font-size: 2.5rem;
  font-weight: bold;
  color: #333;
}

.description {
  margin-top: 1rem;
  font-size: 1.2rem;
  color: #666;
}

.movie-link {
  margin-top: 2rem;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  text-decoration: none;
  font-size: 1.1rem;
}

.movie-link:hover {
  background-color: #0056b3;
}
</style>
