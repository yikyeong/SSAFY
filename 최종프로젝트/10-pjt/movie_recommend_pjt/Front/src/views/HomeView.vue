<template>
  <div>
    <h1>Homepage</h1>
    <MovieList />
    
  </div>
</template>

<script setup>
import MovieList from '@/components/MovieList.vue';
import { onMounted } from 'vue';
import { useApiStore } from '@/stores/api';

const apiStore = useApiStore()

onMounted(() => {
  apiStore.TopRatedMovies()  // TopRatedMovies 함수 호출
})

</script>

<style scoped>

</style>