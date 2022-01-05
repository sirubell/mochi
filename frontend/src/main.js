import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './vuex'
import 'bootstrap'
import './assets/custom.scss'
import './axios'

createApp(App).use(router).use(store).mount('#app')

router.beforeEach((to, from, next) => {

    //獲取使用者登入成功後儲存的登入標誌
    let getFlag = localStorage.getItem("Flag");
   
    //如果登入標誌存在且為isLogin，即使用者已登入
    if(getFlag === "isLogin"){
   
     //設定vuex登入狀態為已登入
     store.state.isLogin = true
     next()

     //如果已登入，還想想進入登入註冊介面，則定向回首頁
     if (!to.meta.isLogin) {
    //   iView.Message.error('請先退出登入')
    //   next({
    //    path: '/home'
    //   })
     }
    
    //如果登入標誌不存在，即未登入
    }else{
     //使用者想進入需要登入的頁面，則定向回登入介面
     if(to.meta.isLogin){
    //   next({
    //    path: '/login',
    //   })
    //   //iViewUi友好提示
    //   iView.Message.info('請先登入')
    //  //使用者進入無需登入的介面，則跳轉繼續
     }else{
      next()
     }
   
    }

});
