<template>
    <div class="cont_all">
      <div>
        <button @click="this.router.push({name: 'dashboard'});">back</button>
      </div>
      <div class="cont_logo">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="100" />
      </div>
      <div>
        <h1 style="margin: 2rem 0 0 1rem ;">Finalizando Pedido</h1>
      </div>
      <div>
        <form action="">
          <label for="delivery">Entregar </label>
          <input type="checkbox" name="delivery">
          
          <label for="address"></label>
          <input type="number" name="address">
        </form>
      </div>
      <div>
        
        <ul class="cont-list-products">
        <li v-for="(order_product, index) in order_data.order_products" :key="index">
          <p>
            {{ order_data?.products[index].name }}
          </p>
          <p>
            {{ order_data?.products[index].type }}
          </p>
          <p>
            {{ order_product?.quantity }} 
          </p>
          <p>
            R$  {{ order_product?.total_price }}
          </p>
          <button @click="removeFromBasket(order_product.id, index)">Remover</button>
        </li>
      </ul>
      </div>
      
    </div>
</template>
  
  // ____________SCRIPT____________
<script>
import apiOrderProductService from '../../services/orderProduct/apiOrderProductService'
import apiProductService from "../../services/products/apiProductService"
import { useRoute, useRouter } from 'vue-router';

export default {
  components: {},

  data() {
    return {
      router: useRouter(),
      order_data: {}
    };
  },
  props: {},
  methods: {
    async load_data(){
      await apiProductService.ProductsInOrderAccountView().then((response)=>{
      this.order_data = response.data
      if(!this.order_data){
        this.router.push({name: 'dashboard'});
      }
    })
    },
    async removeFromBasket(id, index) {
      await apiOrderProductService.deleteOrderProduct(id)
      this.load_data()
    },
  },
  async mounted() {
    this.load_data()
   }
};
</script>
  
<style scoped>
.cont_all{
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}
.cont_logo{
  position: fixed;
  right: 0;
  height: fit-content;
  width: fit-content;
  padding: 0.7rem;
}
.cont-list-products {
  margin-top: 2.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
.cont-list-products li{
  display: flex;
  justify-content: space-evenly;
}
</style>
  