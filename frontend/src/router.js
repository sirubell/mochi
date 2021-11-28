import { createRouter, createWebHistory } from 'vue-router';

import Home from './components/Home.vue'
import Problem from './components/Problem.vue'
import Course from './components/Course.vue'
import Class from './components/Class.vue'
import Logout from "./components/auth/Logout.vue";
import Login from "./components/auth/Login.vue";
import Register from "./components/auth/Register.vue";
import Forgotpassword from './components/auth/forgotpassword.vue';
import AdminPanel from './components/auth/admin.vue';

export default createRouter({
  history : createWebHistory(),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/problem',
      name: 'problem',
      component: Problem
    },
    {
      path: '/course',
      name: 'course',
      component: Course
    },
    {
      path: '/class',
      name: 'class',
      component: Class
    },
    {
      path: "/logout",
      component: Logout,
    },
    {
      path: "/forgot-password",
      component: Forgotpassword,
    },
    {
      path: "/login",
      component: Login,
    },
    {
      path: "/register",
      component: Register,
    },
    {
      path: "/admin",
      component: AdminPanel,
    }
  ]
})