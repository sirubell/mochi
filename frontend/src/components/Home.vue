<template>
  <div class="home">
    <h3 v-if="userInfo">Hi, user = {{userInfo.name}}</h3>
    <h3 v-if="!userInfo">You are not logged in!</h3>

    <h3>Hello, this is mochi online judge!</h3>
    
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>

    
    <div class="footer">
      <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
        <p class="col-md-4 mb-0 text-muted">&copy; 2022 Mochi</p>

        <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
          <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
        </a>

        <ul class="nav col-md-4 justify-content-end">
          <li class="nav-item"><router-link to="/home" class="nav-link px-2 text-muted">Home</router-link></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Features</a></li>
          <li class="nav-item"><a href="https://sites.google.com/view/ntpuprog" class="nav-link px-2 text-muted">Website</a></li>
          <li class="nav-item"><a href="https://www.facebook.com/NTPUProgClub" class="nav-link px-2 text-muted">FB</a></li>
        </ul>
      </footer>
    </div>
  </div>


</template>

<script>
// @ is an alias to /src
import {mapGetters} from 'vuex'
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
     HelloWorld
  },
  computed: {
    ...mapGetters(['userInfo'])
  }
}
</script>

<style>
  .footer{
    clear: both;
    position: relative;
    height: 100px;
    margin-bottom: -200px;
  }
</style>
