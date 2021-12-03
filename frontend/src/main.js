import { createApp } from 'vue'
import App from './App.vue'
import routera from './router'
import 'bootstrap'

createApp(App).use(routera).mount('#app')

// import VueJsonToTable from 'vue-json-to-table'
// Vue.use(VueJsonToTable)