import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'

const routes = [
  {//home
    path: '/',
    name: 'Home',
    component: Home
  },
  {//status
    path: '/status',
    name: 'Status',
    component: () => import('./views/Status/Status.vue')
  },
  {//class
    path: '/class',
    name: 'Class',
    component: () => import('./views/Class/Class.vue')
  },
  {//class_id
    path: '/class/class_id',
    name: 'Class_id',
    component: () => import('./views/Class/Class_id.vue')
  },
  {//class_id homework
    path: '/class/class_id/homework',
    name: 'Homework',
    component: () => import('./views/Class/Class_id/Homework/Homework_all.vue')
  },
  {//class_id member
    path: '/class/class_id/member',
    name: 'Member',
    component: () => import('./views/Class/Class_id/Member.vue')
  },
  {//member edit
    path: '/class/class_id/member/edit',
    name: 'MemberEdit',
    component: () => import('./views/Class/Class_id/Member/Member_edit.vue')
  },
  {//class_id exam
    path: '/class/class_id/exam',
    name: 'Exam',
    component: () => import('./views/Class/Class_id/Exam/Exam_all.vue')
  },
  {//class exam_id
    path: '/class/class_id/exam/exam_id',
    name: 'Exam_id',
    component: () => import('./views/Class/Class_id/Exam/Exam_id.vue')
  },
  {//exam_id dashboard
    path: '/class/class_id/exam/exam_id/dashboard',
    name: 'Dashboard',
    component: () => import('./views/Class/Class_id/Exam/Exam_id/id_dashboard.vue')
  },
  {//exam_id edit
    path: '/class/class_id/exam/exam_id/edit',
    name: 'idedit',
    component: () => import('./views/Class/Class_id/Exam/Exam_id/id_edit.vue')
  },
  {//exam_id problemset
    path: '/class/class_id/exam/exam_id/problemset',
    name: 'Problemset',
    component: () => import('./views/Class/Class_id/Exam/Exam_id/id_problemset.vue')
  },
  {//exam_id submissiion
    path: '/class/class_id/exam/exam_id/submission',
    name: 'Submission',
    component: () => import('./views/Class/Class_id/Exam/Exam_id/id_submission.vue')
  },
  {//exam edit
    path: '/class/class_id/exam/edit',
    name: 'Edit',
    component: () => import('./views/Class/Class_id/Exam/Exam_edit.vue')
  },
  {//problem
    path: '/problem',
    name: 'Problem',
    
    component: () => import('./views/Problem/Problem.vue')
  },
  {
    path: '/problem/new',
    name: 'Add question',
    component: () => import('./views/Problem/addquestion.vue')
  },
  {
    path: '/problem/problem_id',
    name: '題目標題',
    component: () => import('./views/Problem/Problem_id.vue')
  },
  {
    path: '/problem/problem_id/code',
    name: 'code',
    component: () => import('./views/Problem/problem_id/Code.vue')
  },
  {
    path: '/problem/problem_id/submission',
    name: 'submission',
    component: () => import('./views/Problem/problem_id/Submission.vue')
  },
  {
    path: '/problem/problem_id/status',
    name: 'status',
    component: () => import('./views/Problem/problem_id/Status.vue')
  },
  {
    path: '/problem/problem_id/solution',
    name: 'solution',
    component: () => import('./views/Problem/problem_id/Solution.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
