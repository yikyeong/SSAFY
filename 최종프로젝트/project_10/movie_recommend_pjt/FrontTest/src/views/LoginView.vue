<template>
  <div class="login-container">
    <div class="login-box">
      <h1>로그인</h1>
      <form @submit.prevent="logIn">
        <div class="input-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model.trim="username">
        </div>
        
        <div class="input-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model.trim="password">
        </div>

        <input type="submit" value="로그인" class="submit-btn">
      </form>
    </div>
  </div>
</template>

<script setup>

import { ref } from 'vue'
import { useUserStore } from '@/stores/user'

const username = ref(null)
const password = ref(null)

const store = useUserStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
/* 페이지 전체를 중앙 정렬 */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f4f4; /* 배경 색 */
}

/* 로그인 박스 스타일 */
.login-box {
  background-color: #333; /* 어두운 회색 */
  color: #fff;
  padding: 30px;
  border-radius: 15px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

/* 제목 스타일 */
.login-box h1 {
  font-size: 2rem;
  margin-bottom: 20px;
}

/* input-group (라벨과 입력 필드) */
.input-group {
  margin-bottom: 15px;
  text-align: left;
}

.input-group label {
  display: block;
  font-size: 1rem;
  margin-bottom: 5px;
}

.input-group input {
  width: 100%; /* 입력 필드 가로 길이 */
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
  background-color: #444;
  color: #fff;
  font-size: 1rem;
}

.input-group input:focus {
  border-color: #007BFF;
  outline: none;
}

/* 제출 버튼 스타일 */
.submit-btn {
  width: 100%; /* 버튼 가로 길이 */
  padding: 10px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
  margin-top: 15px; /* 버튼과 입력 필드 사이에 공간 추가 */
}

.submit-btn:hover {
  background-color: #0056b3;
}
</style>
