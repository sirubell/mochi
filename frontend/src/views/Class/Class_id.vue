<template>
    <div>
        <h1>this is the class id page</h1>
        
        <div id="nav" style="background-color:rgb(108, 159, 184)">
            <router-link to="/class/class_id/homework">Homework</router-link>|
            <router-link to="/class/class_id/exam">Exam</router-link>|
            <router-link to="/class/class_id/member">Member</router-link>
        </div>
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