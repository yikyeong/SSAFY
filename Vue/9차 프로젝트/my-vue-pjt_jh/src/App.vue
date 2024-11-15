<template>
  <div id="app">
    <!-- 네비게이션 바 포함 -->
    <Navbar />
    <!-- 페이지 내용이 여기에 렌더링됨 -->
    <router-view />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'; // Navbar 컴포넌트 임포트

export default {
  name: 'App',
  components: {
    Navbar, // 네비게이션 바 컴포넌트 등록
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}
</style>
