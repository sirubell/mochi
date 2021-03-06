import { createRouter, createWebHistory } from 'vue-router'
import Home from './components/Home.vue'
import ComponentSlot from './components/component_slot.vue'
import Status from './components/status.vue'
import Login from './components/user/login.vue'
import SignUp from './components/user/signup.vue'
import User from './components/user/user.vue'
import Forgot_password from './components/user/forgot_password.vue'
import Reset from './components/user/reset.vue'
import Reset_token from './components/user/reset_token.vue'
import Change_Password from './components/user/change_password.vue'
import Change_Email from './components/user/change_email.vue'
import Footer from './components/footer.vue'

import Submission from './components/submission.vue'

import Problem from './components/problem/problem.vue'
import ProblemAll from './components/problem/problem_all.vue'
import Problem_id_submission from './components/problem/problem_id_submission.vue'
import NewProblem from './components/problem/new_problem.vue'

import ClassAll from './components/class/class_all.vue'

import Homework from './components/class/homework_all.vue'
import Homework_id from './components/class/homework_id.vue'
import Homework_status from './components/class/homework_status.vue'
import NewHomework from './components/class/homework_new.vue'

import Exam from './components/class/exam.vue'
import Exam_id_problem from './components/problem/problem.vue'
import Exam_id_problemset from './components/class/exam_id_problemset.vue'
import Exam_id_dashboard from './components/class/exam_id_dashboard.vue'
import NewExam from './components/class/exam_new.vue'


const routes = [
  { path: '/test-new-problem', component: NewProblem },
  { path: '/test-new-exam', component: NewExam },
  { path: '/test-new-homework', component: NewHomework },
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
    path: '/submission/:submission_id',
    component: Submission
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
        path: ':problemId',
        name: 'problem-id',
        component: Problem
      },
      {
        path: 'submission/:problemId',
        name: 'problemSubmission',
        component: Problem_id_submission
      }
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
        component: Homework_id
      },
      {
        path: 'homework_status/:id',
        component: Homework_status
      },
      {
        path: 'homework/:homeworkId/problem/:problemId',
        component: Problem
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
        path: 'exam/:examId/:problemId',
        component: Exam_id_problem
      },
      {
        path: 'exam/:Exam_id/dashboard',
        component: Exam_id_dashboard
      }
    ]
  },
  {
    path: "/forgot_password",
    component: Forgot_password,
  },
  {
    path: "/reset",
    component: Reset,
  },
  {
    path: "/reset/:token",
    component: Reset_token,
  },
  {
    path: "/change_password",
    component: Change_Password,
  },
  {
    path: "/change_email",
    component: Change_Email,
  },
  {
    path: "/footer",
    component: Footer,
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
