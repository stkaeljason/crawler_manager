// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import axios from 'axios'

axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'

Vue.prototype.$http = axios
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
Vue.use(ElementUI,{ size: 'small' })

router.beforeEach((to, from, next) => {
    // 判断该路由是否需要登录权限
    if (to.meta.requireAuth) {
        // 通过vuex state获取当前的token是否存在
        // console.log(isEmptyObject(store.state.user))
        if(store.state.token) {
            next();
        }
        else {
            next({
                path: '/login',
                query: {redirect: to.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
            })
        }
    }
    else {
        next();
    }
 })


 function isEmptyObject(obj) {
    for (var key in obj) {
        return false;
    }
    return true;
 }
