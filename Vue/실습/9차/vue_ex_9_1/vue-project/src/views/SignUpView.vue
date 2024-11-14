<template>
  <div>
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">Username</label>
        <input type="text" id="username" v-model.trim="username">
      </div>
      <div>
        <label for="password1">Password</label>
        <input type="password" id="password1" v-model.trim="password1">
      </div>
      <div>
        <label for="password2">Password Confirm</label>
        <input type="password" id="password2" v-model.trim="password2">
      </div>
      <input type="submit" value="Sign Up">
    </form>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useUserStore } from '@/stores/userStore';

const userStore = useUserStore()
const username = ref('')
const password1 = ref('')
const password2 = ref('')

const signUp = function(){
  const userData = {
    username : username.value,
    password1 : password1.value,
    password2 : password2.value
  }
  userStore.signUp(userData)
}
</script>

<style scoped>

</style>