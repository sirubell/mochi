<template>
  <div class="contain-fluid-navbar">
    <header class="d-flex flex-wrap align-items-center justify-content-md-between py-2 mb-4 border-bottom">
      <router-link to="/home" class="fs-2 nav-link link-dark col-md-2 text-start" style="color: #ffff">
      <img alt="Vue logo" src="../assets/display.svg">
      Mochi
      </router-link>
      <ul class="fs-5 nav col-md-auto mb-2 justify-content-center mb-md-0">
        <li><router-link to="/problem" class="nav-link px-3 link-light">Problem</router-link></li>
        <li><router-link to="/status" class="nav-link px-3 link-light">Status</router-link></li>
        <li><router-link to="/class/homework/all" class="nav-link px-3 link-light">Homework</router-link></li>
        <li><router-link to="/class/exam" class="nav-link px-3 link-light">Exam</router-link></li>
        <li><router-link to="/test-new-problem" class="nav-link px-3 link-light">New-Problem</router-link></li>
        <li><router-link to="/test-new-exam" class="nav-link px-3 link-light" >New-Exam</router-link></li>
        <li><router-link to="/test-new-homework" class="nav-link px-3 link-light">New-Homework</router-link></li>
      </ul>

      <div class="fs-5 col-md-2">
        <div v-if="userInfo">
          <ul class="nav mb-2 justify-content-end mb-md-0">
            <li class="nav-item dropdown">
              <a href="#" class="text-end nav-link dropdown-toggle px-2 link-dark" data-bs-toggle="dropdown" aria-expanded="false" style="color: #ffff">User</a>
              <ul class="dropdown-menu" aria-labelledby="dropdown03">
                <li><router-link to="/user"  class="dropdown-item">My profile</router-link></li>
                <!-- <li><a class="dropdown-item" href="#">personal</a></li> -->
                <li><router-link to="/change_email" class="dropdown-item">Change Profile</router-link></li>
              </ul>
            </li>
            <li class="nav-item">
              <a href="javascript:void(0)" @click="handleClick" class="text-end nav-link px-2 link-dark" style="color: #ffff">Logout</a>
            </li>
          </ul>
        </div>
        <div v-else>
          <ul class="nav mb-2 justify-content-end mb-md-0">
            <li><router-link to="/login" class="nav-link px-2 link-dark">Login</router-link></li>
            <li><router-link to="/signup" class="nav-link px-2 link-dark">Sign up</router-link></li>
          </ul>
        </div>
      </div>
    </header>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'NavBar',
  methods: {
    handleClick() {
      axios.get('logout')
      this.$store.dispatch('login', null);
      this.$router.push('/');
    }
  },
  computed: {
    ...mapGetters([
      'userInfo'
    ])
  },

}
</script>

<style>
  .contain-fluid-navbar{
    background-color:rgb(30, 124, 68)
  }
</style>
