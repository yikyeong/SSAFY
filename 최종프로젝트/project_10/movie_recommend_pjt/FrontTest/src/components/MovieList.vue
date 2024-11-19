<template>
  <div>
    <v-row
      v-for="(genre, index) in movies"
      :key="index"
      class="mb-4"
      align="start"
      justify="center"
      position="relative"
    >
      <!-- 왼쪽 화살표 버튼 -->
      <v-btn
        v-if="startIndex > 0"
        @click="moveToPreviousGenre(index)"
        icon
        class="arrow-button left-arrow"
      >
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>

      <div class="movie-container">
        <!-- transition 태그로 모든 카드 감싸기 -->
        <transition
          name="fade"
          mode="out-in"
          @after-leave="onCardLeave"
          @before-enter="onCardEnter"
        >
          <div :key="startIndex">
            <!-- 한 장르의 영화 리스트를 v-for로 순회하면서 카드를 렌더링 -->
            <v-row
              v-for="(movie, movieIndex) in genre.slice(startIndex, endIndex)"
              :key="movie.movie_id"
              class="d-flex"
              align="center"
              justify="center"
              no-gutters
              :style="{ gap: '16px' }"
            >
              <v-col
                :key="movie.movie_id"
                cols="auto"
                class="d-flex justify-center"
                style="position: relative;"
              >
                <v-card class="card-fixed-size" raised>
                  <v-img :src="movie.image" class="image-card"></v-img>
                  <transition name="fade-text">
                    <v-card-title v-if="movie.title" class="text-h6">{{ movie.title }}</v-card-title>
                  </transition>
                  <transition name="fade-text">
                    <v-card-subtitle v-if="movie.release_date">{{ movie.release_date }}</v-card-subtitle>
                  </transition>
                </v-card>
              </v-col>
            </v-row>
          </div>
        </transition>
      </div>

      <!-- 오른쪽 화살표 버튼 -->
      <v-btn
        v-if="endIndex < genre.length"
        @click="moveToNextGenre(index)"
        icon
        class="arrow-button right-arrow"
      >
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-row>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import { ref } from 'vue'

const store = useMovieStore()

// Pagination state
const startIndex = ref(0)
const endIndex = ref(1) // 한 번에 보여줄 카드의 개수를 1개로 설정

// 영화 목록
const movies = store.movies

// 카드가 보이는지 여부
const showMovie = ref(true)

const moveToNextGenre = (index) => {
  const genre = movies[index]
  if (endIndex.value < genre.length) {
    startIndex.value += 1
    endIndex.value += 1
    showMovie.value = false // 카드가 사라지도록 설정
  }
}

const moveToPreviousGenre = (index) => {
  const genre = movies[index]
  if (startIndex.value > 0) {
    startIndex.value -= 1
    endIndex.value -= 1
    showMovie.value = false // 카드가 사라지도록 설정
  }
}

// 카드가 사라진 후에 다음 카드를 표시
const onCardLeave = () => {
  showMovie.value = true
}

// 새 카드가 등장하기 전에 실행될 동작
const onCardEnter = () => {
  // 여기에 애니메이션을 추가하거나 다른 처리를 할 수 있습니다.
}
</script>

<style scoped>
.v-row {
  padding: 10px;
  margin-left: 10px;
  margin-right: 10px;
  position: relative;
}

.v-card-title {
  font-size: 20px;
  font-weight: bold;
}

.v-card-subtitle {
  font-size: 16px;
}

/* 카드의 고정된 크기 (카드 크기 키움) */
.card-fixed-size {
  width: 350px;  /* 카드의 가로 길이를 키움 */
  height: 500px; /* 카드의 세로 길이를 키움 */
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

/* 이미지 크기 고정 및 비율 유지 */
.image-card {
  object-fit: cover; /* 이미지를 비율을 맞춰서 잘라서 카드에 맞춤 */
  height: 70%; /* 이미지가 카드의 70%를 차지하도록 */
  width: 100%; /* 폭을 카드에 맞추기 */
}

/* 화살표 버튼의 기본 스타일 */
.arrow-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%); /* 세로 중앙 정렬 */
  z-index: 10;
}

.left-arrow {
  left: 20px; /* 카드와 일정한 간격을 두고 배치 */
}

.right-arrow {
  right: 20px; /* 카드와 일정한 간격을 두고 배치 */
}

/* 카드 전환 애니메이션 (opacity fade in/out) */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.6s ease;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}

/* 제목과 부제목 애니메이션 (opacity fade in/out) */
.fade-text-enter-active, .fade-text-leave-active {
  transition: opacity 1s ease;
}

.fade-text-enter, .fade-text-leave-to {
  opacity: 0;
}
</style>
