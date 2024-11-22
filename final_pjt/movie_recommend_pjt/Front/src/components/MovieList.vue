<template>
    <carousel class="mt-16" :itemsToShow="carouselViewCnt" :autoplay="2000" :transition="2000" :wrap-around="true" style="height: auto;">
        <slide v-if="moviesLoading" v-for="i in 10" :key="i">
            <v-skeleton-loader
            class="shadow-sm word-keep-all product-card-inner ma-3 carousel__item"
            width="100%"
            type="image, image, article"
            >
            </v-skeleton-loader>
        </slide>
        <slide v-if="!moviesLoading" v-for="movie in movies" :key="movie.idx">
            <MovieCard :movie="movie"/>
        </slide>
    </carousel>
    <MovieListAll :allMovies="allMovies" style="background-color: #353535;" />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import 'vue3-carousel/dist/carousel.css';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel';
import { useDisplay } from 'vuetify';
import { useRouter } from 'vue-router'
import { httpGetAxios } from '@/assets/js/CommonAPI.js';
import MovieCard from '@/components/MovieCard.vue'
import MovieListAll from '@/components/MovieListAll.vue'

const { xs, sm, md, lg, xl, width } = useDisplay();
const carouselViewCnt = ref(5);
if(xl.value) {
    carouselViewCnt.value = 5;
} else if(lg.value) {
    carouselViewCnt.value = 3.3;
} else if(md.value) {
    carouselViewCnt.value = 5;
} else if(sm.value) {
    carouselViewCnt.value = 1.95;
} else if(xs.value && width.value >= 300) {
    carouselViewCnt.value = 1.3;
} else {
    carouselViewCnt.value = 1;
}
console.log(carouselViewCnt.value);

const movies = ref([]);
onMounted(() => {
    getTopRatedMovies();  // TopRatedMovies 함수 호출
    getTopAllMovies();
})

const moviesLoading = ref(true);
const getTopRatedMovies = () => {
    const API_KEY = import.meta.env.VITE_TMDB_API_KEY
    const BASE_URL = 'https://api.themoviedb.org/3'
    const endpoints = BASE_URL + '/discover/movie'
    const param = {
        include_adult: false,
        include_video: false,
        page: 1,
        sort_by: 'vote_average.desc',
        'vote_count.gte': 300,
        with_original_language: 'ko',
        api_key: API_KEY,
        language: 'ko-KR'
    }
    httpGetAxios(endpoints, param).then(res => {
        console.log(res);
        if(res.status === 200) {
            moviesLoading.value = false;
            movies.value = res.data.results.slice(0, 10)
        } else {
            alert(res.statusText);
        }
    });
}

const allMovies = ref([]);
const getTopAllMovies = () => {
    const API_KEY = import.meta.env.VITE_TMDB_API_KEY
    const BASE_URL = 'https://api.themoviedb.org/3'
    const endpoints = BASE_URL + '/discover/movie'
    for(let i = 1; i <= 5; i++) {
        const param = {
            include_adult: false,
            include_video: false,
            page: i,
            sort_by: 'vote_average.desc',
            'vote_count.gte': 300,
            with_original_language: 'ko',
            api_key: API_KEY,
            language: 'ko-KR'
        }
        httpGetAxios(endpoints, param).then(res => {
            if(res.status === 200) {
                for(let q in res.data.results) {
                    allMovies.value.push(res.data.results[q])
                }
            } else {
                alert(res.statusText);
            }
        });
    }
}
</script>