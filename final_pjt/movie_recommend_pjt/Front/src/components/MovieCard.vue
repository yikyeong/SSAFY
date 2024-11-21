<template>
    <v-card 
        class="shadow-sm word-keep-all ma-3"
        variant="tonal"
        @click="goMovieDetail(movie.id)"
        width="100%"
        style="border: 5px solid "
    >
    <!-- <img :alt="movie.title" class="movie-poster" /> -->
        <v-img
            height="500px"
            :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
            cover
            class="text-white"
            :alt="movie.title"
        />
        <v-divider :thickness="2" color="lighty"></v-divider>
        <v-card-title class="text-h5 mt-2 font-weight-black">{{ movie.title }}</v-card-title>
        <v-card-subtitle class="text-h6 mb-5">
            <!-- <div class="mb-1">{{ movie.title }}</div> -->
            <div>Rating: {{ movie.vote_average.toFixed(1) }}</div>
        </v-card-subtitle>
    </v-card>
</template>

<script setup>
import { defineProps } from 'vue'
import { useRouter, RouterLink, RouterView } from 'vue-router'

const router = useRouter()
const props = defineProps({
    movie: Object, // 외부에서 영화 목록을 받음
})

const goMovieDetail = (id) => {
    const to = { 
        name: 'movieDetail', 
        params: { id: id }
    };
    router.push(to);
}
</script>