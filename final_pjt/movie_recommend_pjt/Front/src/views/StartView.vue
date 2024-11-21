<template>
  <div class="container">
    <h1 class="start-text">
      <RouterLink :to="{ name: 'home' }">Start</RouterLink>
    </h1>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
/* 전체 화면을 중앙 정렬 */
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #1a1a1a; /* 어두운 배경색 */
}

/* Start 텍스트 스타일 */
.start-text {
  font-family: 'Impact', sans-serif; /* 강렬한 폰트 */
  font-size: 5rem; /* 폰트 크기 */
  font-weight: bold;
  color: #ff4500; /* 주황색 계열의 강렬한 색상 */
  text-align: center;
  position: relative;
  animation: glowing 1.5s infinite ease-in-out;
  text-shadow: 2px 2px 5px rgba(255, 255, 255, 0.4), /* 흰색 윤곽 */
               -2px -2px 5px rgba(255, 255, 255, 0.4), /* 반대 방향 흰색 윤곽 */
               0 0 20px #ff6347, 0 0 30px #ff6347, /* 빛 퍼지는 효과 */
               0 0 40px #ff7f50;
}

/* 빛이 모이는 효과 */
@keyframes glowing {
  0% {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.4), 0 0 10px rgba(255, 255, 255, 0.4),
                 0 0 15px rgba(255, 255, 255, 0.4), 0 0 20px #ff6347, 0 0 30px #ff6347;
    transform: scale(1);
  }
  50% {
    text-shadow: 0 0 10px rgba(255, 255, 255, 0.4), 0 0 20px rgba(255, 255, 255, 0.4),
                 0 0 30px #ff6347, 0 0 40px #ff7f50, 0 0 50px #ff7f50;
    transform: scale(1.1);
  }
  100% {
    text-shadow: 0 0 5px rgba(255, 255, 255, 0.4), 0 0 10px rgba(255, 255, 255, 0.4),
                 0 0 15px rgba(255, 255, 255, 0.4), 0 0 20px #ff6347, 0 0 30px #ff6347;
    transform: scale(1);
  }
}

/* RouterLink 기본 스타일 제거 */
.start-text a {
  text-decoration: none;
  color: inherit;
}

.start-text:hover {
  color: #ff6347; /* hover 시 색상 변경 */
  cursor: pointer;
}
</style>
