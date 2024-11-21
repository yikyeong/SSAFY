import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
// import { c } from 'vite/dist/node/types.d-aGj9QkWt'

export const useUserStore = defineStore('user', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(localStorage.getItem('token'))
  const user = ref(localStorage.getItem('user'))
  const router = useRouter()

  const isLogin = computed(() => {
    if (token.value === null) {
      return false // 로그아웃
    } else {
      return true // 로그인
    }
  })

  // 회원가입 요청 액션
  const signUp = function (payload) {
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/dj-rest-auth/signup/`,
      data: {
        username, password1, password2
      }
    })
      .then((res) => {
        // console.log(res)
        // console.log(res.data)
        // const password = password1
        // logIn({ username, password })
        router.push({ name: 'login' })
        alert('회원가입이 성공적으로 완료되었습니다!')
      })
      .catch((err) => {
        if (err.response) {
          // 서버 에러 메시지 처리
          const errorData = err.response.data

          // 비밀번호 관련 에러 메시지 처리
          if (errorData.password1) {
            alert(`비밀번호 오류: ${errorData.password1[0]}`)
          } else if (errorData.non_field_errors) {
            alert(`오류: ${errorData.non_field_errors[0]}`)
          } else {
            alert('회원가입에 실패했습니다. 다시 시도해주세요.')
          }

          console.log('서버 오류:', errorData) // 서버에서 반환된 전체 에러 데이터
          console.log('상태 코드:', err.response.status) // 상태 코드 출력
        } else if (err.request) {
          // 요청이 보내졌으나 응답을 받지 못한 경우
          alert('서버로부터 응답이 없습니다. 네트워크 상태를 확인해주세요.')
          console.log('요청 오류:', err.request)
        } else {
          // 그 외의 에러
          alert(`알 수 없는 오류 발생: ${err.message}`)
          console.log('에러 발생:', err.message)
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
      url: `${API_URL}/dj-rest-auth/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        // console.log(username)
        localStorage.setItem('token', token.value)
        router.push({ name: 'home' })
        user.value = username
        localStorage.setItem('user', user.value)
        console.log(user.value)
        console.log(token.value)
        alert('로그인 성공')
      })
      .catch((err) => {
        if (err.response) {
          console.log('서버 오류:', err.response.data)  // 서버에서 반환된 에러 메시지 출력
          console.log('상태 코드:', err.response.status)  // 상태 코드 출력

          const errors = err.response.data
          let errorMessage = ''

          if (errors.non_field_errors) {
            errorMessage = '아이디나 비밀번호가 올바르지 않습니다. 다시 시도해주세요.'
          } else if (errors.username) {
            errorMessage = `아이디 오류: ${errors.username[0]}`
          } else if (errors.password) {
            errorMessage = `비밀번호 오류: ${errors.password[0]}`
          } else {
            errorMessage = '로그인에 실패했습니다. 입력 정보를 다시 확인해주세요.'
          }
    
          alert(`로그인 실패: ${errorMessage}`)
        } else if (err.request) {
          console.log('요청 오류:', err.request)  // 요청이 보내졌으나 응답을 받지 못한 경우
          alert('요청이 처리되지 않았습니다. 인터넷 연결을 확인해주세요.');
        } else {
          console.log('에러 발생:', err.message)  // 그 외의 에러
          alert('알 수 없는 오류가 발생했습니다.')
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
      url: `${API_URL}/dj-rest-auth/logout/`,
      headers: {
        Authorization: `Token ${token.value}`, // 토큰을 헤더에 포함
      }
    })
      .then((res) => {
        console.log("로그아웃 성공:", res.data)
        alert('로그아웃 되었습니다!')
        token.value = null
        localStorage.removeItem('token');  
        // console.log(token.value);
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

  // const profile = function () {
  //   axios({
  //     method: 'get',
  //     url : `${URL}/accounts/profile/${user.value}`,
  //     headers: {
  //       Authorization: `Token ${token.value}`, // 토큰을 헤더에 포함
  //     }
  //   })
  //     .then((res) => {
  //       userdata.value = {
  //         username : res.data.username,
  //         password1 : res.data.password1,
  //         password2 : res.data.password2,
  //       }
  //       console.log('프로필 데이터:', userdata.value);
  //   })
  //     .catch((err) => {
  //       if (err.response) {
  //         console.error('서버 오류:', err.response.data);
  //         console.error('상태 코드:', err.response.status);
  //       } else if (err.request) {
  //         console.error('요청 오류:', err.request);
  //       } else {
  //         console.error('에러 발생:', err.message);
  //       }
  //     })
  //   }
  }
  return { API_URL, token, isLogin, signUp, logIn, logOut, user}
}, { persist: true })
