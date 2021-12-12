<template>
  <NavBar/>
  <button class="btn btn-primary" @click="changeLoginStatus">change login status</button>
  <router-view/>
</template>

<script>
import NavBar from './components/navbar.vue'

export default {
  name: 'App',
  data() {
    return {
    }
  },
  methods: {
    changeLoginStatus() {
      console.log(this.$store.getters.loginStatus)
      this.$store.dispatch('login', true)
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
