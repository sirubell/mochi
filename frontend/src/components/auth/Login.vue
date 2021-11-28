<template>
  <div class="container m-5">
    <form @submit.prevent="userLogin">
      <h1 class="h3 mb-3 fw-normal">Please Sign In</h1>

      <div class="form-floating">
        <input type="email" class="form-control" id="floatingInput" placeholder="email" v-model="user.email">
        <label for="floatingInput">User Email</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="floatingPassword" placeholder="Password" v-model="user.password">
        <label for="floatingPassword">Password</label>
      </div>

      <div class="checkbox mb-3">
        <label>
          <input type="checkbox" value="remember-me"> Remember me
        </label>
      </div>
      <button class="btn btn-primary btn-block" type="submit">
        <router-link to="/">
          Log in
        </router-link>
      </button>
      <button class="btn btn-primary btn-block" type="submit">
        <router-link to="/register">
          Register
        </router-link>
      </button>
      <button class="btn btn-primary btn-block" type="submit">
        <router-link to="/forgot-password">
          Forgot password
        </router-link>
      </button>
    </form>
  </div>
</template>


<script>
import { firebaseAuth } from "@firebase/auth";

export default {
  name: 'Login',
  data() {
    return {
      user: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    userLogin() {
      firebaseAuth
        .signInWithEmailAndPassword(this.user.email, this.user.password)
        .then(() => {
          this.$router.push("/admin");
        })
        .catch((error) => {
          alert(error.message);
        });
    },
  },
};
</script>

<style scoped>
  a{
    text-decoration: none;
    color: aliceblue;
  }
  
</style>
