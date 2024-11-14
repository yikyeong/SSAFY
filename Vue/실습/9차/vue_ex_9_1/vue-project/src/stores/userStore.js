import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios";

export const useUserStore = defineStore('user', () => {
  const BASE_URL = 'http://localhost:8000/accounts'
  const signUp = function (userData){
    axios({
      method: 'POST',
      url:`${BASE_URL}/signup/`,
      data:{
        // 사용자 이름, 비밀번호, 비밀번호 확인
        username : userData.username,
        password1 : userData.password1,
        password2 : userData.password2
      }
    }).then((res) => {
      console.log(res.data)
    }).catch((err) => {
      console.log(err)
    })
  }

  return {
    signUp
  }
}, { persist: true })
