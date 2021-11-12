import { createRouter, createWebHistory } from 'vue-router';

import Home from './components/Home.vue'
import Problem from './components/Problem.vue'
import Course from './components/Course.vue'
import Class from './components/Class.vue'
import Login from './components/Login.vue'
import Signup from './components/Signup.vue'

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
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/signup',
      name: 'signup',
      component: Signup
    },
  ]
})