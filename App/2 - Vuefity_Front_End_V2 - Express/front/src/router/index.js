import Vue from 'vue'
import VueRouter from 'vue-router'


import Home from '../views/Home.vue'
// import About from '../views/About.vue'
import contate from '../components/contate.vue'
import monitorar from '../components/monitorar.vue'
import exportar from '../components/exportar.vue'
import cadastrar from '../components/cadastrar.vue'

Vue.use(VueRouter)

  const routes = [

  {
    path: '/',
    name: 'Home',
    component: Home
  },

  {
    path: '/contate',
    name: 'contate',
    component: contate
  },
  {
    path: '/monitorar',
    name: 'monitorar',
    component: monitorar
  },
  {
    path: '/exportar',
    name: 'exportar',
    component: exportar
  },
  {
    path: '/cadastrar',
    name: 'cadastrar',
    component: cadastrar
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
