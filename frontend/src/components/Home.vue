<template>
    
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    
    <div class="home" :style="home"> 
      <div class="p-md-3 ext-center" style="background:#e1f5e1bb">
        <h2 v-if="userInfo">Hi, user  {{userInfo.name}} ...</h2>
        <h3 v-if="!userInfo">You are not logged in!</h3>

        <div class="col-md-8 p-lg-5 mx-auto my-5">
          <h1>This is mochi online judge!</h1>
          <p class="lead fw-normal">This is a nice cool place for you to learn~</p>
          <div class="Information" style="margin-top:40px">
            <router-link to="/problem" class="btn btn-outline-secondary">Enjoy the programming world!</router-link>
          </div>
        </div>
        <div class="product-device shadow-sm d-none d-md-block"></div>
        <div class="product-device product-device-2 shadow-sm d-none d-md-block"></div>
      </div>
    </div>  

    <div class="row" style="margin:10px">
      <div class="col-md-3 col-md-push-9" style="text-align: center">
        <div class="card" style="width: 18rem">
          <img src="../assets/problem.png">
          <div class="card-body">
            <h2 class="card-title">Latest News</h2>
            <p class="card-text">Try to do some problems?</p>
            <router-link to="/problem" class="btn btn-primary">Go to problems</router-link>
          </div>
        </div>
      </div>

      <div class="col-md-9 col-md-pull-3" style="margin-top:30px">
        <h2>- Programming Information -</h2>
        <div class="Information" style="margin-top:30px">
          <h5><a href="https://ncpc.nsysu.edu.tw/" style="text-decoration:none;">NCPC 全國大專電腦軟體設計競賽</a></h5>
          <h5><a href="https://contest.cc.ntu.edu.tw/npsc2021/" style="text-decoration:none;">NPSC 網際網路程式設計全國大賽</a></h5>
          <h5><a href="https://ioinformatics.org/" style="text-decoration:none;">IOI 資訊奧林匹亞</a></h5>
          <h5><a href="https://icpc.global/" style="text-decoration:none;">ICPC</a></h5>
          <!-- <img alt="Vue logo" src="../assets/mochi.png"> -->
        </div>
      </div>
    </div>

    <Footer/>
  


</template>

<script>
// @ is an alias to /src
import {mapGetters} from 'vuex'
import Footer from './footer.vue'
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'Home',
  data () {
    return {
        home: {
            backgroundImage:"url(" + require("../assets/cover.png") + ")"
        }
    }
  },
  components: {
    //  HelloWorld
    Footer
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
  /* .row {
    text-align: center;
  } */
  .home {
    /* background: #f6fff6; */
    background-position: center;
    /* height: 100%; */
    /* width: 100%; */
    background-size: cover;
    /* position: fixed; */
  }

</style>
