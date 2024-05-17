import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import {useAuthStore} from '@/stores/auth.js'
import { useRoute, useRouter } from 'vue-router';

const routes = [
  {path: "/",
    name: 'home',
    component: () => import('../views/HomeView.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/admin",
    name: 'admin',  
    component: () => import('../views/Admin/managementPage.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/dashboard",
    name: 'dashboard',  
    component: () => import('../views/Dashboard/dashboard.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/perfil",
    name: 'Perfil',  
    component: () => import('../views/perfil/perfil.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/pedido",
    name: 'Pedido',  
    component: () => import('../views/Pedido/pedido.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/ordersOpen",
    name: 'Pedidos Abertos',  
    component: () => import('../views/Pedido/ordersOpen.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/avaliableProducts",
    name: 'Produtos disponíveis',  
    component: () => import('../views/Products/list_available_products.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/receivedProducts",
    name: 'Produtos recebidos',  
    component: () => import('../views/Products/list_received_products.vue'),
    meta: {
      auth: true
    }
  },
  {path: "/historico",
    name: 'Historico',  
    component: () => import('../views/Historico/historico.vue'),
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

      } else { 
        next();
      }
    } else {
      if(to.name == 'home'){
        return next()
      }
      next({name: 'home'})
    }
  } else {
    next();
  }
}) 

export default router