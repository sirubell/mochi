<template>
  <div id="app">
    <Nav />
    <div class="auth-wrapper">
        <!-- <div class="auth-inner">

        </div> -->
      </div>
  </div>
</template>

<script>
  import Nav from './components/Nav.vue'
  // import Login from './components/auth/Login.vue'
  export default {
    name: "App",
    components: {
      Nav,
      // Login
    }
  };
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Fira+Sans:400,500,600,700,800');
  
  body {
    background: rgb(194, 212, 176) !important;
    min-height: 100vh;
    display: flex;
    font-weight: 400;
    font-family: 'Fira Sans', sans-serif;
  }

  h1, h2, h3, h4, h5, h6, label, span {
    font-weight: 500;
    font-family: 'Fira Sans', sans-serif;
  }

  body, html, #app, #root, .auth-wrapper {
    width: 100%;
    height: 100%;
  }

  #app {
    text-align: center;
  }

  .navbar-light {
    background-color: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
  }

  .auth-wrapper {
    width: flex;
    justify-content: center;
    flex-direction: column;
    text-align: left;
  }

  .auth-inner {
    width: 450px;
    margin: auto;
    background: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
    padding: 40px 35px 45px 55px;
    transition: all .3s;
  }

  .auth-wrapper form-control:focus {
    border-color: rgb(182, 231, 231);
    box-shadow: none;
  }

  .auth-wrapper h3 {
    text-align: center;
    margin: 0;
    line-height: 1;
    padding-bottom: 20px;
  }

  .custom-control-label {
    font-weight: 400;
  }

  .forgot-password,
  .forgot-password a {
    text-align: right;
    font-size: 13px;
    padding-top: 10px;
    color: cadetblue;
    margin: 0;
  }

  .forgot-password a {
    color: crimson;
  }
</style>