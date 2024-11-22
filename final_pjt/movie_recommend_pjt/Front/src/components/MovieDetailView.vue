<template>
    <div class="movie-detail" v-if="movie">
        <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" alt="Movie Poster" class="movie-poster"
            style="width: 200px;" />
        <h2>{{ movie.title }}</h2>
        <p>개봉일: {{ movie.release_date }}</p>
        <p>TDMB 평점: {{ movie.vote_average }}</p>
        <h2>장르</h2>
        <p>{{ genreContent }}</p>
        <h2>줄거리</h2>
        <p>Overview: {{ movie.overview }}</p>
        <h2>공식 예고편</h2>

        <button @click="showTrailer">
            <img src="@/img/logo/youtubelogo.png" style="width: 30px" />
        </button>
        
        <!-- 예고편 모달 -->
        <div v-if="showTrailerModal" class="trailer-modal">
            <iframe :src="`https://www.youtube.com/embed/${trailerId}`" frameborder="0" allowfullscreen></iframe>
            <button @click="closeTrailerModal">Close</button>
        </div>
        <div>
            <CommentList/>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import CommentList from './CommentList.vue';

const props = defineProps({
    id: Number,  // 라우터에서 전달되는 movie id
})

const movie = ref(null)  // 영화 상세 정보를 저장할 변수
const genreContent = ref('')  // 장르 내용
const showTrailerModal = ref(false)  // 예고편 모달 상태
const trailerId = ref('')  // 예고편 ID

// 영화 상세 정보 API 호출
const fetchMovieDetails = (id) => {
    axios.get(`https://api.themoviedb.org/3/movie/${id}`, {
        params: {
            api_key: import.meta.env.VITE_TMDB_API_KEY, // 환경변수로 API_KEY
            language: 'ko-KR', // 한국어
        }
    })
        .then((response) => {
            movie.value = response.data  // 영화 상세 정보를 movie에 저장
            genreContent.value = response.data.genres.map(genre => genre.name).join(', ')  // 장르들 연결
        })
        .catch((error) => {
            console.error('영화 정보를 가져오는 데 실패했습니다:', error)
        })
}

// 컴포넌트가 마운트되었을 때 영화 상세 정보 로드
onMounted(() => {
    fetchMovieDetails(props.id)
})

// 예고편 모달 열기
const showTrailer = () => {
    trailerId.value = '영상 ID 넣기';  // 여기에 실제 영상 ID 넣기
    showTrailerModal.value = true
}

// 예고편 모달 닫기
const closeTrailerModal = () => {
    showTrailerModal.value = false
}
</script>

<style scoped>
.movie-poster {
    width: 100%;
    max-width: 400px;
    margin-top: 20px;
    border-radius: 8px;
}

.trailer-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
}

.trailer-modal iframe {
    width: 80%;
    height: 80%;
    border-radius: 8px;
}

.trailer-modal button {
    position: absolute;
    top: 20px;
    right: 20px;
    background: red;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 50%;
}
</style>