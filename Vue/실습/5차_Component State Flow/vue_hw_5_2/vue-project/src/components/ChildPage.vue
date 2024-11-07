<template>
  <div class="border p-3 mb-3">
    <h3>자식 페이지입니다.</h3>
    <br>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>
  defineProps({
    child : Object
  })
</script>

<style scoped>

</style>