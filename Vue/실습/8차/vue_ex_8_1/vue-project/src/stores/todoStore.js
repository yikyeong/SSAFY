import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
export const useTodoStore = defineStore('todo', () => {
  // state
  const todos = ref([])

  // gatters

  //actions
  const getTodos = function(){
    axios({
      method: 'GET',
      url: `${BASE_URL}/api/v1/todos/`
    }).then((response) =>{
      todos.value=response.data
    }).catch((error)=>{
      console.log(error)
    })
  }

  // 백엔드 서버의 기본 URL
  const BASE_URL = "http://localhost:8000"

  return { todos, getTodos }
}, { persist: true })
