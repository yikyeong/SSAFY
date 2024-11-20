import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()

  // 회원가입 요청 액션
  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/djaccounts/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        // console.log(res)
        // console.log(res.data)
        // const password = password1
        // logIn({ username, password })
        alert('회원가입이 성공적으로 완료되었습니다!')
        router.push({ name: 'home' })
      })
      .catch((err) => {
        if (err.response) {
          console.log('서버 오류:', err.response.data);  // 서버에서 반환된 에러 메시지 출력
          console.log('상태 코드:', err.response.status);  // 상태 코드 출력
        } else if (err.request) {
          console.log('요청 오류:', err.request);  // 요청이 보내졌으나 응답을 받지 못한 경우
        } else {
          console.log('에러 발생:', err.message);  // 그 외의 에러
        }
      })
  }

  // 로그인 요청 액션
  const logIn = function (payload) {
    // const email = payload.email
    // const password1 = payload.password
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/djaccounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'home' })
        console.log(res.data)
        // console.log('로그인 성공')
      })
      .catch((err) => {
        if (err.response) {
          console.log('서버 오류:', err.response.data);  // 서버에서 반환된 에러 메시지 출력
          console.log('상태 코드:', err.response.status);  // 상태 코드 출력
        } else if (err.request) {
          console.log('요청 오류:', err.request);  // 요청이 보내졌으나 응답을 받지 못한 경우
        } else {
          console.log('에러 발생:', err.message);  // 그 외의 에러
        }
      })
  }
  
  const logOut = function () {
    if (!token.value) {
      console.error("로그아웃할 토큰이 없습니다.");
      return;
    }
    axios({
      method: 'post',
      url: `${API_URL}/djaccounts/logout/`,
      headers: {
        Authorization: `Token ${token.value}`, // 토큰을 헤더에 포함
      }
    })
      .then((res) => {
        console.log("로그아웃 성공:", res.data)
        token.value = null
        localStorage.removeItem('token');  
        console.log('--');
        console.log(token.value);
        router.push({ name: 'home' })
      })
      .catch((err) => {
        if (err.response) {
          console.log('서버 오류:', err.response.data);  // 서버에서 반환된 에러 메시지 출력
          console.log('상태 코드:', err.response.status);  // 상태 코드 출력
        } else if (err.request) {
          console.log('요청 오류:', err.request);  // 요청이 보내졌으나 응답을 받지 못한 경우
        } else {
          console.log('에러 발생:', err.message);  // 그 외의 에러
        }
      })
  }
  return { API_URL, token, isLogin, signUp, logIn, logOut }
}, { persist: true })
