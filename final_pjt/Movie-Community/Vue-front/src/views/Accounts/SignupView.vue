<template>
  <div>
    <h1 class="text-center text-white font-weight-bold">회 원 가 입</h1>
    <form>
      <div class="form-group">
        <label for="username" class="text-white">Username</label>
        <input
          v-model="signupData.username"
          type="email"
          class="form-control"
          id="username"
          aria-describedby="emailHelp"
        />
        <small id="emailHelp" class="form-text text-muted">Username을 입력하세요.</small>
      </div>
      <div class="form-group">
        <label for="Password1" class="text-white">Password</label>
        <input v-model="signupData.password1" type="password" class="form-control" id="Password1" />
        <small id="emailHelp" class="form-text text-muted">비밀번호를 8자리 이상의 숫자와 문자를 조합해서 입력하세요.</small>
      </div>
      <div class="form-group">
        <label for="password2" class="text-white">Password Confirm</label>
        <input v-model="signupData.password2" @keyup.enter="signup" type="password" class="form-control" id="password2" />
        <small id="emailHelp" class="form-text text-muted">위의 Password와 똑같이 입력하세요.</small>
      </div>
    </form>
    <div class="d-flex justify-content-center">
      <button @click="signup" type="submit" class="btn btn-primary">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      signupData: {
        username: null,
        password1: null,
        password2: null
      }
    };
  },
  methods: {
    signup() {
      this.$emit("send-signupdata", this.signupData);
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