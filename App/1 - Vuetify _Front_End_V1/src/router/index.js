import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import calc from '../views/calc.vue'
import contato from '../views/contato.vue'
import monitorar from '../views/monitorar.vue'
import exportar from '../views/exportar.vue'
import smenu from '../views/smenu.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/calc',
    name: 'calc',
    component: calc,
  },
  {
    path: '/monitorar',
    name: 'monitorar',
    component: monitorar,
  },
  {
    path: '/contato',
    name: 'Contato',
    component: contato,
  },
  {
    path: '/exportar',
    name: 'exportar',
    component: exportar,
  },
  {
    path: '/smenu',
    name: 'smenu',
    component: smenu,
  },
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
