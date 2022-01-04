<template>
  <div>
    <h3 v-if="userInfo">Hi, user = {{userInfo.name}}</h3>
    <h3 v-if="!userInfo">You are not logged in!</h3>

    <h3>Hello, this is mochi online judge!</h3>
    
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
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
