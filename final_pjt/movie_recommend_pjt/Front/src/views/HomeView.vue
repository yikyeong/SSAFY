<template>
  <div>
    <MovieList />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import MovieList from '@/components/MovieList.vue';
// import { useApiStore } from '@/stores/api';

// const apiStore = useApiStore()

onMounted(() => {
  // getTopRatedMovies()  // TopRatedMovies 함수 호출
})
</script>