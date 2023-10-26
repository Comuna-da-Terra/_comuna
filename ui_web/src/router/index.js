import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import {useAuthStore} from '@/stores/auth.js'
import { useRoute, useRouter } from 'vue-router';

const routes = [
  {path: "/",
    name: 'home',
    component: () => HomeView
  },
  // {path: "/client/login",
  //   name: 'login',
  //   component: () => import('../views/Login/clienteLogin.vue'),
  //   meta: {
  //     auth: true
  //   }
  // },
  //   {path: "/client/register",
  //   name: 'register',
  //   component: () => import('../views/Register/clientRegister.vue'),
  //   meta: {
  //     auth: true
  //   }
  // },
  {path: "/dashboard",
    name: 'dashboard',  
    component: () => import('../views/Dashboard/dashboard.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/dashboard/order/",
    name: 'order',  
    component: () => import('../views/Products/finish_order.vue'),
    meta: {
      auth: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,

})

router.beforeEach(async (to, from, next)=>{
  if(to.meta?.auth){
    const auth = useAuthStore();
    const isAuthenticated = await auth.verifyAccessToken();
    
    if (isAuthenticated) {
      if(to.name == 'home'){
        next({name: 'dashboard'})

      } else if(to.name == 'register'){
        next({name: 'dashboard'})

      }
      next();
    } else {
      if(to.name == 'home'){
        next()
      } 
    }
  } else {
    next();
  }
}) 

export default router