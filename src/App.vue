<template>
  <nav class = "navbar navbar-expand-lg navbar-light fixed-top bd-light">
    <div class = "container-fluid">
      <a class = "navbar-brand" href = "/home"> Home </a>
      <div class = "collapse navbar-collapse" id = "navbarSupportedContent">
      <ul class = "navbar-nav me-auto mb-2 mb-lg-0">
        <li class = "nav-item">
          <router-link class = "nav-link" to = "/problem"> Problem </router-link>
        </li>
        <li class = "nav-item">
          <router-link class = "nav-link" to = "/course"> Course </router-link>
        </li>
        <li class = "nav-item">
          <router-link class = "nav-link" to = "/class"> Class </router-link>
        </li>
      </ul>
      <div class="flex-row-reverse">
        <li class = "d-flex nav-item">
          <router-link class = "nav-link" to = "/login"> Log in </router-link>
          <router-link class = "nav-link" to = "/signup"> Sign up </router-link>
        </li>

      </div>
    </div>
    </div>
  </nav>
  <div class = "container">
    <router-view />
  </div>  
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style>
#app {
  font-family : Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing : antialiased;
  -moz-osx-font-smoothing : grayscale;
  text-align : center;
  color : #2c3e50;
  /* margin-top : 60px; */
}


</style>