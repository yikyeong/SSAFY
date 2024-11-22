import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import moviesData from '@/assets/movies_data.json'

export const useMovieStore = defineStore('movie', () => {
  // 영화 상세 정보 변수 선언
  const movie = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  // 영화검색 변수 선언
  const query = ref('')
  const videos = ref([])
  const VideoId = ref(null)
  const isModalVisible = ref(false)

  const getMovieList = function () {
    axios({
      method: 'get',
      url: ''
    })
  }

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

  const getComments = function (movieId) {
    axios({
      method:'get',
      url:`${API_URL}/movies/${movieId}/comment/`,
      headers: {
        Authorization: `Token ${token.value}`,
      }
    })
      .then((res) => {
        console.log(res.data)
        comment.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const searchReviews = function () {
    if (query.value) {
      const searchQuery = `${query.value} 영화 리뷰`
      const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${searchQuery}&key=YOUR_YOUTUBE_API_KEY`
      
      axios({
        method: 'get',
        url: url
      }).then(res => {
        // videos.value = res.data. // 
      }).catch(err => {
        console.log(err)
      })
    }
  }

  // test
  // ------------------------------------------------------------------------------------
  const movies = ref([moviesData])

  return { movie, API_URL, getMovieDetail, movies, getComments }
})
