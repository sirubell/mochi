<template>
  <div class="home">
    
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->

    <!-- <div class="position-relative overflow-hidden p-3 p-md-5 m-md-3 text-center bg-light"> -->
      <h3 v-if="userInfo">Hi, user = {{userInfo.name}}</h3>
      <h3 v-if="!userInfo">You are not logged in!</h3>

      <div class="col-md-8 p-lg-5 mx-auto my-5">
        <h1>Hello, this is mochi online judge!</h1>
        <p class="lead fw-normal">This is a nice cool place for you to learn~</p>
        <a class="btn btn-outline-secondary" href="#">Have fun</a>
      </div>
      <div class="product-device shadow-sm d-none d-md-block"></div>
      <div class="product-device product-device-2 shadow-sm d-none d-md-block"></div>
    <!-- </div> -->


    <div class="col-8 mx-auto col-md-4 order-md-2 col-lg-5">
      <h2>最新消息</h2>
      <img alt="Vue logo" src="../assets/mochi.png">
    </div>


    <div class="footer">
      <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
        <p class="col-md-4 mb-0 text-muted">&copy; 2022 Mochi</p>

        <a href="/" class="col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
          <svg class="bi me-2" width="40" height="32"><use xlink:href="#bootstrap"/></svg>
        </a>

        <ul class="nav col-md-4 justify-content-end">
          <li class="nav-item"><router-link to="/home" class="nav-link px-3 text-muted">Home</router-link></li>
          <li class="nav-item"><a href="#" class="nav-link px-3 text-muted">Features</a></li>
          <li class="nav-item"><a href="https://sites.google.com/view/ntpuprog" class="nav-link px-3 text-muted">Website</a></li>
          <li class="nav-item"><a href="https://www.facebook.com/NTPUProgClub" class="nav-link px-3 text-muted">FB</a></li>
        </ul>
      </footer>
    </div>
  </div>


</template>

<script>
// @ is an alias to /src
import {mapGetters} from 'vuex'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  components: {
    //  HelloWorld
  },
  computed: {
    ...mapGetters(['userInfo'])
  }
}
</script>

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
    color:#b0dac0;
    font-weight:bold;
    /* background-color:#cecece; */
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
  .home {
    /* background: #f6fff6; */
    background-position: center;
    /* height: 100%; */
    /* width: 100%; */
    background-size: cover;
    /* position: fixed; */
  }

</style>
