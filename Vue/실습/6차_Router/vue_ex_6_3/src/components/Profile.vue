<template>
  <div>
    <h3>상세 프로필</h3>
    <p>반갑습니다. {{ username }} 입니다.</p>
  </div>
</template>

<script setup>
  import {ref} from "vue"
  import {useRoute} from "vue-router"

  const route = useRoute()
  const username = ref(route.params.username)
</script>

<style scoped>

</style>