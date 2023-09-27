import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
// import Login from '../views/Login/clienteLogin.vue'
// import Register from '../views/Register/clientRegister.vue'
// import Dashboard from '../views/Dashboard/dashboard.vue'

const routes = [
  {path: "/",                 component: () => HomeView},
  {path: "/client/login", name: 'login',    component: () => import('../views/Login/clienteLogin.vue')},
  {path: "/client/register",  component: () => import('../views/Register/clientRegister.vue')},
  {path: "/dashboard", name: 'dashboard',       component: () => import('../views/Dashboard/dashboard.vue')},
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,

})

export default router
