import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import StartView from '@/views/StartView.vue'
import SearchReviewView from '@/views/SearchReviewView.vue'
import SearchMovieView from '@/views/SearchMovieView.vue'
import MovieRecommendView from '@/views/MovieRecommendView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'

// User 관련
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: () => import('@/layouts/Default.vue'),
      children: [
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
          path: '/movie/:id',
          name: 'movieDetail',
          component: MovieDetailView,
          props: true
        },
        {
          path: '/profile',
          name: 'profile',
          component: ProfileView,
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
      ]
    },
  ],
})

export default router