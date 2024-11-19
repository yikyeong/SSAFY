<template>
  <div>
    <h1>로그아웃 중입니다.</h1>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      this.$emit('logout')      
    }
  },
  created() {
    if (this.$cookies.get('username')) {
      this.logout()
      this.$router.push({name: 'Home'})
    }else {
      this.$router.push({ name: "Home" })
    }
  }
}
</script>

<style>

</style>