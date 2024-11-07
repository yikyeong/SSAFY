<template>
  <div class="justify-content-center p-5">
    <div class="text-center">
      <h1 class="fw-bold">가수 정보 페이지에 오신 것을 환영합니다.</h1>
      <br>
      <p>여러분이 좋아하는 가수와 아티스트에 대한 정보를 탐색해보세요</p>
      <img style="width: 200px;" src="@/assets/microphone.jpg" alt="">
    </div>
    <br><br>
    <div class="text-center">
      <h1 class="fw-bold">가수 목록</h1>
    </div>
  </div>
  <div>

  </div>
  <SingerDetail/>
</template>

<script setup>
  import SingerDetail from './singers/SingerDetail.vue';
</script>

<style lang="scss" scoped>

</style>