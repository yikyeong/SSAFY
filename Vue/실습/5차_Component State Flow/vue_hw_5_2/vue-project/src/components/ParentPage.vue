<template>
  <div class="border p-3">
    <br>
    <h1>부모 페이지입니다.</h1>
    <br>
    <div v-for="child in children" :key="child.name">
      <ChildPage :child="child"/>
    </div>
  </div>
</template>

<script setup>
  import {ref} from 'vue' 
  import ChildPage from './ChildPage.vue';

  const children = ref([
    {name: '김하나', age: 30},
    {name: '김두리', age: 20},
    {name: '김서이', age: 10}
  ])
</script>

<style scoped>

</style>