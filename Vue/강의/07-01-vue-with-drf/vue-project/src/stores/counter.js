import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수 
  const getArticles = function(){
    axios({
      method: 'GET',
      url: `${API_URL}/api/vi/articles/`
    })
    .then((res) => {
      // console.log(res.data)
      articles.value=res.data 
    })
    .catch((err) => {
      console.log(err)

    })
  }
  return { articles, API_URL, getArticles }
}, { persist: true })
