import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 객체 하나당 페이지 하나
    {
      // 홈페이지 router
      path : "/",
      name : "home",
      component : HomeView
    },
    {
      // About router
      path : "/about",
      name : "about",
      component : AboutView
    }
  ]
})

export default router
