import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import ProblemAll from './components/problem/problem_all.vue'
import ProblemID from './components/problem/problem_id.vue'
import ProblemID_dashboard from './components/problem/problem_id_dashboard.vue'
import ComponentSlot from './components/component_slot.vue'
import Status from './components/status.vue'
import ClassAll from './components/class/class_all.vue'
import Login from './components/user/login.vue'
import SignUp from './components/user/signup.vue'
import User from './components/user/user.vue'
import Problem from './components/problem/problem.vue'
import NewProblem from './components/problem/new_problem.vue'
import Forgot from './components/user/forgot.vue'
import Reset from './components/user/reset.vue'
import Change_Profile from './components/user/change_profile.vue'
import Change_Password from './components/user/change_password.vue'

import Homework from './components/class/homework.vue'
import Exam from './components/class/exam.vue'

const routes = [
  { path: '/test-problem', component: Problem },
  { path: '/test-new-problem', component: NewProblem },
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
      },
      {
        path: ':id',
        name: 'problemid',
        component: ProblemID
      },
      {
        path: ':id/dashboard',
        name: 'id-board',
        component: ProblemID_dashboard
      },/*,
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
      }*/
      
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
      },
      {
        path: 'homework/all',
        component: Homework
      },
      {
        path: 'homework/:id',
        redirect: '/problem/:id',
        component: Homework
      },
      {
        path: 'exam',
        component: Exam
      }
    ]
  },
  {
    path: "/forgot",
    component: Forgot,
  },
  {
    path: "/reset/:token",
    component: Reset,
  },
  {
    path: "/change_profile",
    component: Change_Profile,
  },
  {
    path: "/change_password",
    component: Change_Password,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
