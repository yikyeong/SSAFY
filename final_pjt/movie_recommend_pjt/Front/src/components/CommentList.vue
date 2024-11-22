<template>
  <div>
    <h1>댓글</h1>
    <ul>
      <li>작성자 : </li>
    </ul>
  </div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import { useMovieStore } from '@/stores/movie'
  
  const store = useMovieStore()

  onMounted(() => {
    const movieId = 1
    store.getComments(movieId)
    console.log(res)
  })
</script>

<style scoped>

</style>