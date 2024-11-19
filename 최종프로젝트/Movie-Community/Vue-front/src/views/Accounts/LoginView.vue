<template>
  <div>
    <h1 class="text-center text-white font-weight-bold">로 그 인</h1>
    <form>
      <div class="form-group">
        <label for="username" class="text-white">Username</label>
        <input
          v-model="loginData.username"
          type="text"
          class="form-control"
          id="username"
          aria-describedby="emailHelp"
        />
        <small id="emailHelp" class="form-text text-muted">Username을 입력하세요.</small>
      </div>
      <div class="form-group">
        <label for="password" class="text-white">Password</label>
        <input v-model="loginData.password" type="password" @keyup.enter="login" class="form-control" id="password" />
        <small id="emailHelp" class="form-text text-muted">Password를 입력하세요.</small>
      </div>
    </form>
    <div class="d-flex justify-content-center">
      <button @click="login" type="submit" class="btn btn-primary">LOGIN</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginData: {
        username: null,
        password: null
      }
    };
  },
  methods: {
    login() {
      this.$emit("send-logindata", this.loginData);
    }
  },
  created() {
    if (this.$cookies.get("username")) {
      this.$router.push({ name: "Home" });
    }
  }
};
</script>

<style>
</style>