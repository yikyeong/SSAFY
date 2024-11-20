import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import StartView from '@/views/StartView.vue'
import SearchReviewView from '@/views/SearchReviewView.vue'
import SearchMovieView from '@/views/SearchMovieView.vue'
import MovieRecommendView from '@/views/MovieRecommendView.vue'

// User 관련
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'start',
      component: StartView,
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/searchReview',
      name: 'searchReview',
      component: SearchReviewView,
    },
    {
      path: '/searchMovie',
      name: 'searchMovie',
      component: SearchMovieView,
    },
    {
      path: '/movieRecommend',
      name: 'movieRecommend',
      component: MovieRecommendView,
    },
    {
      path: '/profile/:id',
      name: 'profile',
      component: ProfileView,
      // 5번 강의 참고
    },


    //User 관련

    {
      path: '/signUp',
      name: 'signUp',
      component: SignUpView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
  ],
})

export default router