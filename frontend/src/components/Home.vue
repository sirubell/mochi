<template>
  <div>
    <h3 v-if="userInfo">Hi, user = {{userInfo.name}}</h3>
    <h3 v-if="!userInfo">You are not logged in!</h3>

    <h3>Hello, this is mochi online judge!</h3>
    
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
<<<<<<< HEAD

    <!-- <div class="sidebar">
      <h1>News Update</h1>
    </div>
    <div class="body">
      <h1>cool</h1>
    </div> -->

    
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
=======
>>>>>>> f17a02ec6179e58700ac058746cd0d0b49ac6ac5
  </div>
</template>

<script>
// @ is an alias to /src
import {mapGetters} from 'vuex'
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  meta: {
    isLogin: true
  },
  components: {
    HelloWorld
  },
  computed: {
    ...mapGetters(['userInfo'])
  }
}
</script>
<<<<<<< HEAD

<style>
  /* .home {
    width:200px;
    text-align: center;
  } */
  .footer{
    clear: both;
    position: relative;
    height: 100px;
    margin-bottom: -200px;
  }
  .sidebar{
    width:200px;
    float:left;
    height:280px;
    text-align:center;
    line-height:280px;
    font-size:15px;
    color:#ffffff;
    font-weight:bold;
    background-color:#cecece;
  }
  .body{
    width:700px;
    height:280px;
    text-align:center;
    line-height:280px;
    font-size:15px;
    color:#f9c81e;
    font-weight:bold;
    background-color:#fffaf3;
    float:left;
  }
</style>
=======
>>>>>>> f17a02ec6179e58700ac058746cd0d0b49ac6ac5
