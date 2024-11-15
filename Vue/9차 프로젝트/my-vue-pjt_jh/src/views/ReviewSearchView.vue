<template>
  <div>
    <h1>Search for Movie Reviews</h1>
    <input v-model="query" placeholder="Search reviews" @input="searchReviews" />
    <div v-if="videos.length">
      <div v-for="video in videos" :key="video.id.videoId">
        <p>{{ video.snippet.title }}</p>
        <iframe
          :src="`https://www.youtube.com/embed/${video.id.videoId}`"
          frameborder="0"
          allowfullscreen
        ></iframe>
      </div>
    </div>
    <p v-else>Loading...</p>
  </div>
</template>

<script>
// YouTube API에서 영화를 검색하는 함수를 임포트
import { searchYouTubeVideos } from '../stores/youtube';

export default {
  data() {
    return {
      query: '',  // 검색어
      videos: []  // 유튜브 영상 목록을 저장할 배열
    };
  },
  methods: {
    async searchReviews() {
      // 검색어가 있으면 YouTube API에서 영상을 검색
      if (this.query) {
        this.videos = await searchYouTubeVideos(this.query);
      } else {
        this.videos = [];
      }
    }
  }
};
</script>

<style scoped>
/* 스타일 추가 */
</style>
