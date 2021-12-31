import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import ProblemAll from './components/problem/problem_all.vue'
import ProblemID from './components/problem/problem_id.vue'
import Problem_id_submission from './components/problem/problem_id_submission.vue'
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

import Homework from './components/class/homework.vue'
import Exam from './components/class/exam.vue'
import Exam_id_problem from './components/class/exam_id_problem.vue'
import Exam_id_problemset from './components/class/exam_id_problemset.vue'
import Exam_id_dashboard from './components/class/exam_id_dashboard.vue'

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
        path: ':id/submission',
        name: 'id-board',
        component: Problem_id_submission
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
        // redirect: '/problem/:id',
        component: Homework
      },
      {
        path: 'exam',
        component: Exam
      },
      {
        path: 'exam/:id',
        component: Exam_id_problemset
      },
      {
        path: 'exam/:id/:id',
        component: Exam_id_problem
      },
      {
        path: 'exam/:id/dashboard',
        component: Exam_id_dashboard
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
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
