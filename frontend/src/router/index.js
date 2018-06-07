/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/home', meta:{requireAuth:true,}, component: 'Home' },
  { path: '/about', component: 'About' },
  { path: '/statis', component: 'Statis' },
  { path: '/login', component: 'Login' },
  { path: '*', component: 'NotFound' },
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
