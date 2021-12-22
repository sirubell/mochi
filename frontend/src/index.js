router.beforeEach((to, from, next) => {
    const isLogin = localStorage.getItem('token');
    if (isLogin) {
      next();
      if(to.path == '/login') {
        alert('已登入')
        next('/');
      }
    } else {
      if( to.path !== '/login' && to.path !== '/')
        next('/login')
      else
        next()
    }
  })