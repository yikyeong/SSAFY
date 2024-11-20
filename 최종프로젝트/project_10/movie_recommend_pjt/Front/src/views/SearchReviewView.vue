<template>
  <div>
    <div class="search-container">
      <input 
        v-model="query" 
        placeholder="영화 제목을 입력하세요" 
        @input="searchReviews" 
        class="search-input"
      />
      <button @click="searchReviews" class="search-button">검색</button>
    </div>

    <div v-if="videos.length">
      <div 
        v-for="video in videos" 
        :key="video.id.videoId" 
        class="video-card" 
        @click="openModal(video.id.videoId)"
      >
        <div class="video-thumbnail">
          <img :src="video.snippet.thumbnails.medium.url" alt="video thumbnail" />
        </div>
        <div class="video-details">
          <p class="video-title">{{ video.snippet.title }}</p>
          <p class="video-description">{{ video.snippet.description.slice(0, 100) }}...</p>
        </div>
      </div>
    </div>
    <p v-else>Loading...</p>

    <YouTubeReviewModal 
      :videoId="selectedVideoId" 
      :isVisible="isModalVisible" 
      @close="closeModal" 
    />
  </div>
</template>

<script setup>
import { useMovieStore } from '../stores/movie'
// import YouTubeReviewModal from './YouTubeReviewModal.vue'

// Pinia store 사용
const {
  query,
  videos,
  selectedVideoId,
  isModalVisible,
  searchReviews,
  openModal,
  closeModal
} = useMovieStore()
</script>

<style scoped>
.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.search-input {
  width: 300px;
  padding: 10px;
  font-size: 16px;
  margin-right: 10px;
  border: 3px solid #76c7c0; /* 밝은 색으로 테두리 설정 */
  border-radius: 5px;
  outline: none; /* 포커스 시 외곽선 제거 */
  transition: all 0.3s ease; /* 부드러운 트랜지션 효과 */
  color: white; /* 마우스 hover 상태와 관계없이 텍스트 흰색 */
  background-color: #333; /* 어두운 배경색 */
}

/* 마우스 hover 시 무지개 색 그라데이션 효과 */
.search-input:hover {
  background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);
  background-size: 300% 100%; /* 그라데이션 애니메이션을 더 부드럽게 하기 위한 크기 조정 */
  background-position: right center;
  border: 3px solid #f9c92e; /* 마우스 hover 시 테두리 색상 */
}

/* 포커스 시 테두리 색상 변경 */
.search-input:focus {
  border: 3px solid #f9c92e; /* 포커스 시 테두리 색상 변경 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* 포커스 시 그림자 추가 */
}

/* 버튼 스타일 */
.search-button {
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
  background-color: #f9c92e; /* 버튼 배경색 */
  border: none;
  border-radius: 5px;
  color: white;
  transition: background-color 0.3s ease; /* 버튼 색상 트랜지션 */
}

.search-button:hover {
  background-color: #76c7c0; /* 버튼 hover 시 색상 변경 */
}

.video-card {
  display: flex;
  width: 100%;
  max-width: 800px;
  margin: 10px auto;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.video-card:hover {
  background-color: #f0f0f0;
}

.video-thumbnail {
  flex: 1;
  max-width: 20%;
  margin-right: 10px;
}

.video-thumbnail img {
  width: 100%;
  height: auto;
  border-radius: 5px;
}

.video-details {
  flex: 4;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.video-title {
  font-weight: bold;
  margin-bottom: 5px;
}

.video-description {
  color: #555;
  font-size: 14px;
}

/* Loading 텍스트를 가운데로 정렬 */
.loading {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh; /* 화면 전체 높이를 차지 */
  font-size: 24px;
  color: #333; /* 텍스트 색상 */
}
</style>

