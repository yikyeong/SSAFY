<template>
  <div class="movie-list">
    <h1>Top Rated Movies</h1>
    <div class="movie-grid">
      <div
        v-for="movie in movies"
        :key="movie.id"
        class="movie-card"
      >
        <img
          :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
          :alt="movie.title"
          class="movie-poster"
        />
        <div class="movie-info">
          <h3>{{ movie.title }}</h3>
          <p>Rating: {{ movie.vote_average }}</p>
          <router-link :to="`/movies/${movie.id}`" class="movie-details-link">View Details</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { fetchTopRatedMovies } from '../stores/tmdb'; // TMDB API에서 영화 목록을 가져오는 함수

export default {
  name: 'MovieListView',
  data() {
    return {
      movies: [], // 영화 데이터를 저장할 배열
    };
  },
  async created() {
    try {
      this.movies = await fetchTopRatedMovies(); // TMDB에서 영화 목록 가져오기
    } catch (error) {
      console.error('Failed to fetch top rated movies:', error);
    }
  },
};
</script>

<style scoped>
.movie-list {
  padding: 2rem;
  text-align: center;
}

.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* 여러 열로 구성 */
  gap: 1.5rem;
  justify-items: center;
}

.movie-card {
  background-color: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 250px;
  text-align: left;
}

.movie-poster {
  width: 100%;
  height: auto;
}

.movie-info {
  padding: 1rem;
}

.movie-info h3 {
  font-size: 1.2rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.movie-info p {
  font-size: 1rem;
  margin-bottom: 1rem;
}

.movie-details-link {
  display: inline-block;
  padding: 8px 16px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 4px;
}

.movie-details-link:hover {
  background-color: #0056b3;
}
</style>
  