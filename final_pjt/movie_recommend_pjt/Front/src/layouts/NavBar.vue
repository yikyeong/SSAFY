<template>
    <header>
        <nav class="navbar navbar-expand-lg">
            <div class="container">
                <!-- 로고에 왼쪽 간격 추가 -->
                <img src="@/img/logo/ssafy_logo.png" alt="logo" class="logo">
                <!-- 네비게이션 항목들을 오른쪽으로 정렬 -->
                <div class="ms-auto nav-links">
                    <p v-if="isLogin" class="nav-link">{{ userStore.user }}님 환영합니다!</p>
                    <RouterLink :to="{ name: 'home' }" class="nav-link" active-class="active-link">홈</RouterLink>
                    <RouterLink :to="{ name: 'searchReview' }" class="nav-link" active-class="active-link">리뷰검색
                    </RouterLink>
                    <RouterLink v-if="!isLogin" :to="{ name: 'signUp' }" class="nav-link" active-class="active-link">
                        회원가입</RouterLink>
                    <RouterLink v-if="!isLogin" :to="{ name: 'login' }" class="nav-link" active-class="active-link">로그인
                    </RouterLink>
                    <form v-if="isLogin" @submit.prevent="logOut">
                        <input type="submit" value="로그아웃" class="nav-link">
                    </form>
                    <!-- <RouterLink :to="{ name: 'searchMovie' }" class="nav-link" active-class="active-link">
                <img src="./img/search_icon/white_search_icon2-removebg-preview.png" alt="search_icon" class="nav-img">
            </RouterLink> -->
                    <RouterLink :to="{ name: 'movieRecommend' }" class="nav-link" active-class="active-link">영화추천
                    </RouterLink>
                    <RouterLink v-if="isLogin" :to="{ name: 'profile' }" class="nav-link" active-class="active-link">프로필
                    </RouterLink>
                </div>
            </div>
        </nav>
    </header>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue'
import { useUserStore } from '@/stores/user'


const userStore = useUserStore()

const isLogin = computed(() => userStore.isLogin)

const logOut = function () {
  userStore.logOut()
}
</script>