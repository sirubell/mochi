<template>
  <div>
    <h3 v-if="user">Hi, {{user.email}}</h3>
    <h3 v-if="!user">You are not logged in!</h3>
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
    ...mapGetters(['user'])
  }
}
</script>
