<template>
    <div class="cont_all">
      <div>
        <button @click="this.router.push({name: 'dashboard'});">back</button>
      </div>
      <div class="cont_logo">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="100" />
      </div>
      <div>
        <h1 style="margin: 2rem 0 2rem 1rem ;">Finalizando Pedido</h1>
      </div>
      <div>
        <form style="display: flex; justify-content: space-around;" action="">
          <div>
            <label for="delivery">Entregar em casa </label>
            <input type="checkbox" name="delivery" v-model="delivery_status">
          </div>
          <div v-if="!delivery_status || (delivery_status && address_user.length != 0)">
            <label for="address">Endereço: </label>
            <select name="address" v-model="order.delivery_address">
              <option v-if="!delivery_status" v-for="opcao in address_options" :value="opcao">{{ opcao.street }}, {{ opcao.number }} - {{ opcao.neighborhood }}</option>
              <option v-if="delivery_status" v-for="opcao in address_user" :value="opcao" >{{ opcao.street }}, {{ opcao.number }} - {{ opcao.neighborhood }}</option>
            </select>
          </div>
          <button v-if="delivery_status && address_user.length == 0">Criar Endereço</button>
        </form>
        <button @click="conclude_order">Concluído</button>
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
import apiAddresses from "../../services/addresses/apiAddresses"
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {

  components: {},
  data() {
    const authStore = useAuthStore();

    return {
      user_id: authStore.user_id,
      router: useRouter(),
      order_data: {},
      delivery_status: false,
      order: {
        delivery_home: null,
      },
      address_options: [],
      address_user: [],
    };
  },
  props: {},
  methods: {
    async load_data(){
      console.log(this.order)
      await apiProductService.ProductsInOrderAccountView().then((response)=>{
        this.order_data = response.data
        console.log(this.order_data)
        if(!this.order_data){
          this.router.push({name: 'dashboard'});
        }
      })
      await apiAddresses.getListAddress().then((response)=>{
        this.address_options = response.data.filter(address => address.is_default == true ) 
        this.address_user = response.data.filter(address => address.user == this.user_id ) 
        console.log(response.data[0].user)
        console.log(this.address_user)
      })
    },
    async removeFromBasket(id, index) {
      await apiOrderProductService.deleteOrderProduct(id)
      this.load_data()
    },
    async conclude_order(){
      this.order.delivery_home = this.delivery_status 
      console.log(this.order)
      console.log(this.delivery_status)
    }
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
  