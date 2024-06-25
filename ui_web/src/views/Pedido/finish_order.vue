<template>
    <div class="cont_all">
      <div>
        <button @click="this.router.push({name: 'dashboard'});">back</button>
      </div>
      <div class="cont_logo">
        <img alt="Vue logo" src="@/assets/logo.svg" width="80" />
      </div>
      <div>
        <h1 style="margin: 2rem 0 2rem 1rem ;">Pedido</h1>
      </div>
      <div>
        <form style="display: flex; justify-content: space-around;"  @submit.prevent="handleSubmit" action="">
          <div>
            <label for="delivery">Entregar em casa </label>
            <input type="checkbox" name="delivery" v-model="delivery_status" :checked="delivery_status">
          </div>
          <div v-if="!delivery_status || (delivery_status && address_user.length != 0)">
            <label for="address">Endereço: </label>
            <select style="max-width: 200px;" required name="address" v-model="delivery_address">
              <option v-if="!delivery_status" v-for="opcao in address_options" :value="opcao.id">{{ opcao.street }}, {{ opcao.number }} - {{ opcao.neighborhood }}</option>
              <option v-if="delivery_status" v-for="opcao in address_user" :value="opcao.id" >{{ opcao.street }}, {{ opcao.number }} - {{ opcao.neighborhood }}</option>
            </select>
            <button style="height: min-content; padding: 0.5px;" type="button" v-if="delivery_status && address_user.length != 0" @click="modal_address = true">
              <i type="button" @click.prevent="closeModal" class="pi pi-plus"></i>
            </button>
          </div>
          <button type="button" v-if="delivery_status && address_user.length == 0" @click="modal_address = true">Criar Endereço</button>
          <button type="submit">Concluído</button>
        </form>
      </div>
      <div>
        
        <ul class="cont-list-products">
          <li> 
            <p>Quantidade de produtos: {{ order_data.order_products?.reduce((total, product) => total + product.quantity, 0)}} </p>
            <p>Valor Total: {{ order_data.order?.subtotal }}</p>
          </li>
          <li v-for="(order_product, index) in order_data.order_products" :key="index">
            <p>
              {{ order_data?.products[index].name }}
            </p>
            <p>
              {{ order_data?.products[index].type }}
            </p>
            <p>
              <input type="number" v-model="order_product.quantity" min="1"> 
            </p>
            <p>
              R$  {{ order_product?.total_price }}
            </p>
            <button @click="editOrderProduct(order_product.id, order_product.quantity)">Editar</button>
            <button @click.prevent="removeFromBasket(order_product.id, index)">Remover</button>
          </li>
        </ul>
      </div>
    </div>
    <div v-if="modal_address" class="modal-address">
      <formAddress @close-modal="closeModal"></formAddress> 
    </div>
</template>
  
  // ____________SCRIPT____________
<script>
import apiOrderProductService from '../../services/orderProduct/apiOrderProductService'
import apiProductService from "../../services/products/apiProductService"
import apiAddressService from "../../services/addresses/apiAddressService"
import apiOrderService from '../../services/order/apiOrderService';
import formAddress from "../address/register_address.vue"
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import { ref } from 'vue';

export default {

  components: {
    formAddress
  },
  data() {
    const authStore = useAuthStore();

    return {
      user: authStore.user,
      router: useRouter(),
      order_data: {},
      delivery_status: null,
      delivery_address: null,
      orderCurrent: null,
      order_status: null,
      address_options: [],
      address_user: [],
      modal_address: ref(false)
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
      await apiOrderService.getOrder().then((response)=>{
        this.orderCurrent = response.data.filter(order => order.status == 1)
        this.order_status = this.orderCurrent[0].status
        this.delivery_status =  this.orderCurrent[0].delivery_home,
        this.delivery_address = this.orderCurrent[0].delivery_address
      })
      await apiAddressService.getListAddress().then((response)=>{
        this.address_options = response.data.filter(address => address.is_default == true ) 
        this.address_user = response.data.filter(address => address.user == this.user.id ) 
      })
    },
    async removeFromBasket(id, index) {
      await apiOrderProductService.deleteOrderProduct(id)
      this.load_data()
    },
    async editOrderProduct(id_orderProduct, quantity) {
      if(quantity < 1){
        return this.removeFromBasket(id_orderProduct)
      }
      const data = {
        id: id_orderProduct,
        quantity: quantity,
      }
      await apiOrderProductService.updateOrderProduct(data).then((resp)=>{
        apiProductService.ProductsInOrderAccountView().then((response)=>{ this.cestaToBuy = response.data })

        return this.$notify({ type: "success", text: "Pedido alterado com sucesso!", duration: 3000});
      }).catch((err)=>{
        return this.$notify({ type: "warn", text: err.response.data.detail[0], duration: 3000});
      })
      this.load_data()
    },
    async handleSubmit(){  
      const data = {
        id: this.orderCurrent[0].id,
        delivery_address: this.delivery_address,
        delivery_home: this.delivery_status,
        status: 2
      }
      await apiOrderService.updateOrder(data).then((response)=>{
        const IdAdress = response.data.delivery_address
        apiAddressService.getAddress(IdAdress).then((response)=>{
          let currentAdress = response.data
          
          if(this.delivery_status){
            this.$notify({ type: "success", text: `Pedido executado! Entregaremos em ${currentAdress.street} - ${currentAdress.neighborhood}`, duration: 2000});
            setTimeout(()=>{
              this.router.push({name: 'dashboard'});
            }, 3000);

          } else {

            this.$notify({ type: "success", text: `Pedido executado! Aguardamos você na ${currentAdress.street} - ${currentAdress.neighborhood}`, duration: 2000});
            setTimeout(()=>{
              this.router.push({name: 'dashboard'});
            }, 3000);
          }
        })
      })
    },
    closeModal(){
      this.modal_address = false
      this.load_data().then(()=> this.delivery_status = true)
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
  align-items: center;
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
.modal-address{
  width: 80vw;
  max-width: 300px;
  position: absolute;
  z-index: 1;
  background-color: grey;
  padding: 0.5rem;
  border-radius: 7px;
}
</style>
  