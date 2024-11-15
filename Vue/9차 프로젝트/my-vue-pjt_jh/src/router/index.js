import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import MovieListView from '../views/MovieListView.vue';
import MovieDetailView from '../views/MovieDetailView.vue';
import ReviewSearchView from '../views/ReviewSearchView.vue';
import RecommendedView from '../views/RecommendedView.vue';

const routes = [
  { path: '/', component: HomeView },
  { path: '/movies', component: MovieListView },
  { path: '/movies/:movieId', component: MovieDetailView },
  { path: '/review-search', component: ReviewSearchView },
  { path: '/recommended', component: RecommendedView }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
