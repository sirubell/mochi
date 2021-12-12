import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import ProblemAll from './components/problem/problem_all.vue'
import ComponentSlot from './components/component_slot.vue'
import Status from './components/status.vue'
import ClassAll from './components/class/class_all.vue'
import Login from './components/user/login.vue'
import SignUp from './components/user/signup.vue'
import User from './components/user/user.vue'

const routes = [
  {
    path: '/',
    redirect: 'home'
  },
  {
    path: '/home',
    name: 'home',
    component: Home
  },
  {
    path: '/status',
    name: 'status',
    component: Status
  },
  {
    path: '/user',
    component: User
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/signup',
    component: SignUp
  },
  {
    path: '/problem',
    redirect: '/problem/all',
    component: ComponentSlot,
    children: [
      {
        path: 'all',
        name: 'problem-all',
        component: ProblemAll
      }/*,
      {
        path: 'new'
        component: ProblemNew
      },
      {
        path: ':problemId',
        redirect: ':problem_id/code',
        component: ProblemSpecific,
        props: true
        children: {
          path: 'code'
          
        }
      }
      */
    ]
  },
  {
    path: '/class',
    redirect: '/class/all',
    component: ComponentSlot,
    children: [
      {
        path: 'all',
        name: 'class_all',
        component: ClassAll
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
