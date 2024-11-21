<template>
    <div class="movie-list">
        <div class="movie-card">
                <div class="movie-details-link" @click="goMovieDetail(movie.id)">
                    <img :src="`https://image.tmdb.org/t/p/w500${movie.poster_path}`" :alt="movie.title"
                        class="movie-poster" />
                </div>
            <div class="movie-info">
                <h3>{{ movie.title }}</h3>
                <p>평점 {{ movie.vote_average.toFixed(1) }}</p>
            </div>
        </div>
    </div>

    <RouterView />
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

<style scoped>
.movie-list {
    display: flex;
    /* Flexbox를 사용하여 가로로 배치 */
    grid-template-columns: repeat(6, 1fr);
    flex-wrap: wrap;
    /* 화면 크기에 따라 줄 바꿈 */
    justify-content: flex-start;
    /* 카드들을 왼쪽 정렬 */
    gap: 16px;
    /* 카드들 사이의 간격 */
    padding: 10px;
}

.movie-card {
    flex: 0 0 calc(16.66% - 16px);
    /* 한 줄에 6개씩 보이도록 너비 설정 (16.66%는 100%를 6으로 나눈 값) */
    box-sizing: border-box;
    /* 카드 크기 계산에 padding, border 포함 */
}

.movie-info {
    padding: 10px;
    text-align: center;
}

.movie-poster {
    display: block;
    width: 100%;
    height: auto;
    border-radius: 4px;
}

.movie-details-link {
    display: block;
    cursor: pointer;
}

.movie-details-link:hover {
    background-color: #c6c3c3;
}
</style>