import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './vuex'
import 'bootstrap'
import './assets/custom.scss'
import './axios'

createApp(App).use(router).use(store).mount('#app')
