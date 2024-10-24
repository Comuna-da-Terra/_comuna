<template>
    <div class="cont_all">
      <header>

          <i type="button" @click="this.router.push({name: 'dashboard'});" class="pi pi-arrow-left"></i>
          <h1 style="margin: 2rem 0 2rem 1rem ;">Pedido</h1>
          <img alt="Vue logo" src="@/assets/logo.svg" width="80" />

      </header>
      
        <form style="display: flex; justify-content: space-around;"  @submit.prevent="handleSubmit" action="">
          <div style="display: flex; flex-wrap: wrap;" >
            <div>
              <label for="delivery">Entregar em casa </label>
              <input style="margin-right: 2rem;" type="checkbox" name="delivery" v-model="delivery_status" :checked="delivery_status">
            </div>
            <div v-if="!delivery_status || (delivery_status && address_user.length != 0)">
              <label for="address">Endereço: </label>
              <select style="max-width: 200px;" required name="address" v-model="delivery_address">
                <option v-if="!delivery_status" v-for="opcao in address_options" :value="opcao.id">{{ opcao.street }}, {{ opcao.number }} - {{ opcao.neighborhood }}</option>
                <option v-if="delivery_status" v-for="opcao in address_user" :value="opcao.id" >{{ opcao.street }}, {{ opcao.number }} - {{ opcao.neighborhood }}</option>
              </select>
              <button class="btn-new-address" style="height: min-content; padding: 0.5px;" type="button" v-if="delivery_status && address_user.length != 0" @click="modal_address = true">
                <i type="button" @click.prevent="closeModal" class="pi pi-plus"></i>
                Novo Endereço
              </button>
            </div>
          </div>
          <button class="btn-create-address" type="button" v-if="delivery_status && address_user.length == 0" @click="modal_address = true">Criar Endereço</button>
          <button class="btn-submit" type="submit">Concluído</button>
        </form>
      
      <div style="width: 100%;">
        
        <ul class="cont-list-products">
          <span style="display: flex; justify-content: space-between;"> 
            <h3>Quantidade de produtos: {{ order_data.order_products?.reduce((total, product) => total + product.quantity, 0)}} </h3>
            <h3>Valor Total: {{ order_data.order?.subtotal }}</h3>
          </span>
          <li v-for="(order_product, index) in order_data.order_products" :key="index">
            <p>{{ order_data?.products[index].name }}</p>
            <p>{{ order_data?.products[index].type }}</p>
            <p>
              <input class="inp-quantity" type="number" v-model="order_product.quantity" min="1"> 
            </p>
            <p>R$  {{ order_product?.total_price }} </p>
            <i type="button" @click="editOrderProduct(order_product.id, order_product.quantity)" class="pi pi-pencil"></i>
            <i type="button" @click.prevent="removeFromBasket(order_product.id, index)" class="pi pi-trash"></i>
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
import formAddress from "../Address/register_address.vue"
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
header{
  width: 100%;
  display: flex; 
  justify-content: space-around;
}
form{
  width: 100%;
}
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
  gap: 1.5rem;
}
.cont-list-products li{
  display: grid;
  grid-template-columns: 20% 20% 20% 20% 10% 10%;
  justify-content: space-evenly;
}
.inp-quantity{
  width: 3rem;
  text-align: center;
  
}
.modal-address{
  width: 100%;
  height: 100%;
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
  background-color: transparent;
  padding: 0.5rem;
  border-radius: 7px;
}
.btn-create-address{
  height: fit-content;
  width: 110px;
}
.btn-submit{
  color: green;
  border: none;
  border-radius: 50%;
  width: 75px;
  height: 75px;
  font-weight: bold;
}
.btn-submit:hover{
  box-shadow: rgba(0, 0, 0, 0.17) 0px -23px 25px 0px inset, rgba(0, 0, 0, 0.15) 0px -36px 30px 0px inset, rgba(0, 0, 0, 0.1) 0px -79px 40px 0px inset, rgba(0, 0, 0, 0.06) 0px 2px 1px, rgba(0, 0, 0, 0.09) 0px 4px 2px, rgba(0, 0, 0, 0.09) 0px 8px 4px, rgba(0, 0, 0, 0.09) 0px 16px 8px, rgba(0, 0, 0, 0.09) 0px 32px 16px;
  background-color: green;
  color: white;
}
.btn-submit:active{
  box-shadow: rgba(0, 0, 0, 0.35) 0px -50px 36px -28px inset;
  background-color: rgb(79, 136, 79);
}
.pi-arrow-left{
  color: black;
  display: flex;
  align-items: center;
  font-size: xx-large;
}
.pi-pencil{
  color: blue;
}
.pi-trash{
  color: red;
}
</style>
  
