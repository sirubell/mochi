<template>
  <NavBar :is-login="isLogin"/>
  <button class="btn btn-primary" @click="changeLoginStatus">change login status</button>
  <p>is login? {{ isLogin }}</p>
  <router-view/>
</template>

<script>
import NavBar from './components/navbar.vue'

export default {
  name: 'App',
  data() {
    return {
      isLogin: false
    }
  },
  methods: {
    changeLoginStatus() {
      this.isLogin = !this.isLogin
    }
  },
  components: {
    NavBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
