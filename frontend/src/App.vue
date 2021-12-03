<template>
    <div>
      <div id="nav" style="background-color:rgb(89, 160, 101)">
          <router-link to="/">Mochi</router-link> |
          <router-link to="/problem">Problem</router-link> |
          <router-link to="/status">Status</router-link> |
          <router-link to="/class">Class</router-link> |
      </div>
      <router-view/>
    </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav{
      color:rgb(187, 40, 40)!important
}
#nav {
  background-image: rgb(89, 160, 101);
  padding: 20px;
}

#nav a {
  font-weight: 200;
  color: #126bc5;
}

#nav a.router-link-exact-active {
  color: #06140e;
}
</style>
