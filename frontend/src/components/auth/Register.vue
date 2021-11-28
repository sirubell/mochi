<template>
  <div class="container m-5">
    <form @submit.prevent="userSignup">
      <h1 class="h3 mb-3 fw-normal">Register</h1>

      <div class="form-floating">
        <input type="name" class="form-control" id="floatingInput" placeholder="name" v-model="user.name">
        <label for="floatingInput">User's Name</label>
      </div>
      <div class="form-floating">
        <input type="password" class="form-control" id="floatingPassword" placeholder="password" v-model="user.password">
        <label for="floatingPassword">User's Password</label>
      </div>
      <div class="form-floating">
        <input type="comfirmpassword" class="form-control" id="floatingComfirmPassword" placeholder="comfirmpassword" v-model="user.comfirmpassword">
        <label for="floatingComfirmPassword">Comfirm Password</label>
      </div>
      <div class="form-floating">
        <input type="email" class="form-control" id="floatingEmail" placeholder="email" v-model="user.email">
        <label for="floatingEmail">User's Email</label>
      </div>
      <div class="form-floating">
        <input type="school" class="form-control" id="floatingSchool" placeholder="school" v-model="user.school">
        <label for="floatingSchool">School</label>
      </div>
      <div class="form-floating">
        <input type="studentID" class="form-control" id="floatingStudentID" placeholder="studentID" v-model="user.studentID">
        <label for="floatingStudentID">Student ID</label>
      </div>
      
      <button class="w-20 btn btn-md" type="submit" style="center;background: rgb(137, 161, 113)">
        <router-link to="/register">
          Register
        </router-link>
      </button>

      <p class="forgot-password text-right">
        Already Registered?
        <button class="w-20 btn btn-sm" type="submit" style="background: rgb(137, 161, 200)">
          <router-link to="/login">Log in</router-link>
        </button>
      </p>
    </form>
  </div>
</template>

<script>
import { firebaseAuth } from "@firebase/auth";

export default {
  data() {
    return {
      user: {
        name: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {
    userSignup() {
      firebaseAuth
        .createUserWithEmailAndPassword(this.user.email, this.user.password)
        .then((res) => {
          res.user
            .updateProfile({
              displayName: this.user.name,
            })
            .then(() => {
              this.$router.push("/login");
            });
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
    color: rgb(255, 255, 255);
  }
</style>
