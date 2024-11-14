import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useArticleStore = defineStore('article', () => {
  const articles = ref([])
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        title,
        content
      }
    })
    .then(res => console.log(res))
  }

  const signUp = function(payload){
    const {username, password1, password2} = payload

    axios({
      method : 'POST',
      url : 'http://127.0.0.1:8000/signup/',
      data : {
        username, password1, password2
      }
    }) .then((res) => {
      const password = password1
      logIn({username, password})
    }) .catch((err) => {
      console.log(err)
    })
  }
  return { articles, getArticles, createArticle }
})
