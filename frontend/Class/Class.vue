<template>
    <div>
        <h1>this is the class all page</h1>
        <h1><router-link to="/class/class_id">Class_id</router-link></h1>
        <router-view/>
    </div>
</template>
<style>

#nav{
      color:rgb(187, 40, 40)!important
}
#nav {
  background-image: rgb(108, 159, 184);
  padding: 20px;
}
#nav a.router-link-exact-active {
  color: #06140e;
}
</style>