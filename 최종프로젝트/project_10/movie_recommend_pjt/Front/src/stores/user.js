import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(localStorage.getItem('token'))
  const username = ref("")
  const isLogin = computed(() => {
    if (token.value === null) {
      return false // 로그아웃
    } else {
      return true // 로그인
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
          // 서버 에러 메시지 처리
          const errorData = err.response.data;

          // 비밀번호 관련 에러 메시지 처리
          if (errorData.password1) {
            alert(`비밀번호 오류: ${errorData.password1[0]}`);
          } else if (errorData.non_field_errors) {
            alert(`오류: ${errorData.non_field_errors[0]}`);
          } else {
            alert('회원가입에 실패했습니다. 다시 시도해주세요.');
          }

          console.log('서버 오류:', errorData); // 서버에서 반환된 전체 에러 데이터
          console.log('상태 코드:', err.response.status); // 상태 코드 출력
        } else if (err.request) {
          // 요청이 보내졌으나 응답을 받지 못한 경우
          alert('서버로부터 응답이 없습니다. 네트워크 상태를 확인해주세요.');
          console.log('요청 오류:', err.request);
        } else {
          // 그 외의 에러
          alert(`알 수 없는 오류 발생: ${err.message}`);
          console.log('에러 발생:', err.message);
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
        localStorage.setItem('token', token.value)
        router.push({ name: 'home' })
        console.log(res.data)
        alert('로그인 성공')
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
  return { API_URL, token, isLogin, signUp, logIn, logOut, username }
}, { persist: true })
