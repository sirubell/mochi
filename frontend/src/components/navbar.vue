<template>
  <div class="container">
    <header class="d-flex flex-wrap align-items-center justify-content-md-between py-2 mb-4 border-bottom">
      <router-link to="/home" class="fs-2 nav-link link-dark col-md-3 text-start">
      Mochi
      </router-link>


      <ul class="fs-5 nav col-md-auto mb-2 justify-content-center mb-md-0">
        <li><router-link to="/problem" class="nav-link px-2 link-dark">Problem</router-link></li>
        <li><router-link to="/status" class="nav-link px-2 link-dark">Status</router-link></li>
        <li><router-link to="/class" class="nav-link px-2 link-dark">Class</router-link></li>
      </ul>

      <div class="fs-5 col-md-3">
        <div v-if="isLogin">
          <router-link to="/user" class="text-end nav-link px-2 link-dark">User</router-link>
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
export default {
  name: 'NavBar',
  props: {
    isLogin: Boolean
  }
}
</script>
