<template>
    <div class="pt-16">
        <div class="text-h2 text-center font-weight-bold">한국 영화</div>
        <v-container class="mt-12">
            <v-row no-gutters>
                <v-col cols="2" v-for="movie in allMovies">
                    <v-card 
                    class="shadow-sm word-keep-all ma-3"
                    variant="tonal"
                    >
                        <v-img
                        height="400px"
                        :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`"
                        cover
                        class="text-white"
                        :alt="movie.title"
                        />
                        <v-divider :thickness="2" color="lighty"></v-divider>
                        <v-card-title class="text-h5 mt-2 font-weight-black">{{ movie.title }}</v-card-title>
                        <v-card-subtitle class="text-h6 mb-5">
                            <div>Rating: {{ movie.vote_average }}</div>
                        </v-card-subtitle>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script setup>
import { defineProps } from 'vue'
const props = defineProps({
    allMovies: Array, // 외부에서 영화 목록을 받음
})
</script>

<style scoped>
movie-whole-list-bg {
    background: #424242;
}
</style>