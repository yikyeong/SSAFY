import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import LoginView from '@/views/Accounts/LoginView.vue'
import LogoutView from '@/views/Accounts/LogoutView.vue'
import SignupView from '@/views/Accounts/SignupView.vue'
import ChooseLikeMovieView from '@/views/Accounts/ChooseLikeMovieView.vue'
import ArticlesView from '@/views/Article/ArticlesView.vue'
import AritcleView from '@/views/Article/ArticleView.vue'
import CreateArticleView from '@/views/Article/CreateArticleView.vue'
import SearchMovieView from '@/views/Movie/SearchMovieView.vue'
import CreateMovieView from '@/views/Movie/CreateMovieView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'Logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'Signup',
    component: SignupView
  },
  {
    path: '/articles',
    name: 'Articles',
    component: ArticlesView
  },
  {
    path: '/create/article',
    name: 'CreateArticle',
    component: CreateArticleView,
  },
  {
    path: '/search/movie',
    name: 'SearchMovie',
    component: SearchMovieView,
  },
  {
    path: '/article/:id',
    name: 'ArticleView',
    component: AritcleView,
  },
  {
    path: '/create/movie',
    name: 'CreateMovie',
    component: CreateMovieView,
  },
  {
    path: '/choose/likemovie',
    name: 'ChooseLikeMovieView',
    component: ChooseLikeMovieView,
  }  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
