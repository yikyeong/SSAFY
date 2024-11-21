import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

// Pinia store 설정
export const useApiStore = defineStore('movieList', () => {
    const movies = ref([])  // movies를 담을 상태
    const API_KEY = import.meta.env.VITE_TMDB_API_KEY  // API 키
    const BASE_URL = 'https://api.themoviedb.org/3'  // 기본 URL
    
    const TopRatedMovies = () => {
        axios({
            method: 'get',
            url: `${BASE_URL}/movie/top_rated?api_key=${API_KEY}`,  // API_KEY 포함
            params: {
                language: 'ko-KR'
            }
        })
        .then(res => {
            console.log('데이터 가져오기 성공')
            movies.value = res.data.results  // 데이터를 movies 배열에 저장
        })
        .catch(err => {
            console.error('Error fetching top rated movies', err)  // 오류 처리
        })
    }

    return { movies, TopRatedMovies, BASE_URL }
}, { persist: true})
