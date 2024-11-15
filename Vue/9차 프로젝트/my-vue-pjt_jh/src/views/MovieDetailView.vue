<template>
  <div class="movie-detail">
    <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Movie Poster" class="movie-poster" style="width: 200px;" />
    <h2>{{ movie.title }}</h2>
    <p>개봉일: {{ movie.release_date }}</p>
    <p>TDMB 평점: {{ movie.vote_average }}</p>
    <h2>장르</h2>
    <p>{{ movie.genres.map(genre => genre.name).join(', ') }}</p>
    <h2>줄거리</h2>
    <p>Overview: {{ movie.overview }}</p>
    <h2>공식 예고편</h2>


    <button @click="showTrailer">Watch Trailer</button>

    <!-- 예고편 모달 -->
    <div v-if="showTrailerModal" class="trailer-modal">
      <iframe :src="`https://www.youtube.com/embed/${trailerId}`" frameborder="0" allowfullscreen></iframe>
      <button @click="closeTrailerModal">Close</button>
    </div>
  </div>
</template>

<script>
import { fetchMovieDetails } from '../stores/tmdb';
import { searchYouTubeVideos } from '../stores/youtube';  // YouTube API 요청 추가

export default {
  data() {
    return {
      movie: {},
      showTrailerModal: false,
      trailerId: ''
    };
  },
  async created() {
    const movieId = this.$route.params.movieId;
    this.movie = await fetchMovieDetails(movieId);
  },
  methods: {
    async showTrailer() {
      // 영화 제목을 기반으로 유튜브 예고편 검색
      const videos = await searchYouTubeVideos(this.movie.title + ' trailer');
      const trailer = videos.find(video => video.snippet.title.toLowerCase().includes('trailer'));

      if (trailer) {
        this.trailerId = trailer.id.videoId;
        this.showTrailerModal = true;
      } else {
        alert('Trailer not found!');
      }
    },
    closeTrailerModal() {
      this.showTrailerModal = false;
    }
  }
};
</script>

<style scoped>
.movie-poster {
  width: 100%;
  max-width: 400px;
  margin-top: 20px;
  border-radius: 8px;
}

.trailer-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
}

.trailer-modal iframe {
  width: 80%;
  height: 80%;
  border-radius: 8px;
}

.trailer-modal button {
  position: absolute;
  top: 20px;
  right: 20px;
  background: red;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 50%;
}
</style>
