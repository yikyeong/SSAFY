import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import moviesData from '@/assets/movies_data.json'

export const useMovieStore = defineStore('movie', () => {
  const movie = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  // DRF로 영화 상세 페이지 요청을 보내고 응답을 받아 movie에 저장하는 함수
  const getMovieDetail = function () {
    axios({
      method: 'get',
      // url: `${API_URL}/api/v1/articles/`, -> DRF movie detail 주소
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        movie.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }
  // test
  // ------------------------------------------------------------------------------------
  const movies = ref([moviesData])

  return { movie, API_URL, getMovieDetail, movies }
})
