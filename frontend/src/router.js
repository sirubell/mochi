import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import ProblemAll from './components/problem/problem_all.vue'
import ComponentSlot from './components/component_slot.vue'
import Status from './components/status.vue'
import ClassAll from './components/class/class_all.vue'
import Login from './components/login.vue'
import SignUp from './components/signup.vue'
import User from './components/user.vue'


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
        name: 'problem_all',
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
  /*{
    path: '/status',
    name: 'Status',
    component: () => import('./components/Status/Status.vue')
  },
  {
    path: '/problem',
    name: 'Problem',
    component: () => import('./components/Problem/Problem.vue')
  },
  {
    path: '/problem/new',
    name: 'AddQuestion',
    component: () => import('./components/Problem/addquestion.vue')
  },
  {
    path: '/problem/problem_id',
    name: 'SpecificProblem',
    component: () => import('./components/Problem/Problem_id.vue')
  },
  {
    path: '/problem/problem_id/code',
    name: 'Code',
    component: () => import('./components/Problem/problem_id/Code.vue')
  },
  {
    path: '/problem/problem_id/submission',
    name: 'ProblemSubmission',
    component: () => import('./components/Problem/problem_id/Submission.vue')
  },
  {
    path: '/problem/problem_id/status',
    name: 'ProblemStatus',
    component: () => import('./components/Problem/problem_id/Status.vue')
  },
  {
    path: '/problem/problem_id/solution',
    name: 'ProblemSolution',
    component: () => import('./components/Problem/problem_id/Solution.vue')
  }*/
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
