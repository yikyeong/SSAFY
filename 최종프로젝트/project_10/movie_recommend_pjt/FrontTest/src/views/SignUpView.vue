<template>
  <div class="page-container">
    <div class="left-side"></div>
    <div class="right-side">
      <div class="form-container">
        <h1>회원가입</h1>
        <form @submit.prevent="signUp" class="sign-up-form">
          <label for="username">ID : </label>
          <input type="text" id="username" v-model.trim="username"><br>

          <label for="password1">P/W : </label>
          <input type="password" id="password1" v-model.trim="password1"><br>
          
          <label for="password2">P/W 확인 : </label>
          <input type="password" id="password2" v-model.trim="password2"><br>

          <input type="submit" value="회원가입" class="submit-btn">
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const store = useUserStore()

const signUp = function () {
  const payload = {
    username : username.value,
    password1 : password1.value,
    password2 : password2.value,
  }
  store.signUp(payload)
}
</script>

<style scoped>
/* 전체 페이지 레이아웃 */
.page-container {
  display: flex;
  width: 100%;
  height: 100vh;
}

/* 왼쪽 영역 - 더 어두운 회색 배경 */
.left-side {
  background-color: #808080; /* 어두운 회색 배경 */
  flex: 2; /* 화면의 2/3 크기 */
}

/* 오른쪽 영역 - 검정색 배경 */
.right-side {
  background-color: #333; /* 어두운 배경 */
  flex: 1; /* 화면의 1/3 크기 */
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

/* 폼 컨테이너: 제목과 폼을 감싸는 박스 */
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 400px;
  background-color: #e0e0e0; /* 연한 회색 배경 */
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

/* 폼 제목 스타일 */
.form-container h1 {
  font-size: 24px;
  font-weight: 700;
  color: #333;
  margin-bottom: 20px; /* 제목과 폼 사이에 간격 추가 */
}

/* 폼 스타일 */
.sign-up-form {
  display: flex;
  flex-direction: column;
  gap: 15px; /* 항목 간의 간격 */
  width: 100%;
}

/* 폼 안의 label */
.sign-up-form label {
  font-size: 14px;
  font-weight: 600;
  color: #333; /* 진한 색 */
}

/* 폼 안의 input */
.sign-up-form input[type="text"],
.sign-up-form input[type="password"] {
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 4px;
  color: #333; /* 진한 색 */
  background-color: #fff;
}

/* 제출 버튼 스타일 */
.submit-btn {
  background-color: #4CAF50; /* 녹색 */
  color: white;
  padding: 10px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

/* 버튼 호버 효과 */
.submit-btn:hover {
  background-color: #45a049;
}
</style>
