<template>
  <div>
    <h1>로그인</h1>
    <form>
      <div>
        <label for="username">username</label>
        <input type="text" id="username" v-model.trim="username">
      </div>
      <div>
        <label for="password">password</label>
        <input type="password" id="password" v-model.trim="password">
      </div>
      <button type="submit">Log In</button>
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useUserStore } from '@/stores/userStore'; 
</script>

<style scoped>

</style>