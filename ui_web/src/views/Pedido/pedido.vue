<template>
    <div class="cont_all">
      <div class="cont-header">
        <h2 v-if="orderOpen[0]?.status == 2">
          Pedido Enviado
        </h2>
        <h2 v-else-if="orderOpen[0]?.status == 3">
          Pedido Fechado
        </h2>
      </div>
      <button class="button-trash" @click="editOrder()" v-if="orderOpen[0]?.status == 2">
          <i class="pi pi-trash bg-trash">Cancelar Pedido</i>
      </button>
      <div class="cont-info-address">
        <span class="span span-entrega"  v-if="orderOpen[0]?.delivery_home === true">ENTREGAR</span>
        <span class="span span-retirada" v-else="orderOpen[0]?.delivery_home === false">RETIRADA</span>
        <span class="span span-address" @click="showAddres = true"> ENDEREÇO </span>
        <p v-if="showAddres" @click="showAddres = false" class="written-address">
          {{ address.street }}, {{ address.number }} - {{ address.neighborhood }} - {{ address.city }}/{{ address.uf }}
        </p>
        <p>
          R$ {{ orderOpen[0]?.subtotal }}
        </p>
      </div>
      <div class="cont-products">
        <h2>
          Produtos: {{ orderProducts.reduce((acc, item)=> acc + item.quantity, 0) }}
        </h2>
        <ul class="ul-products">
          <li class="li-product" v-for="(order_product, index) in orderProducts" :key="index">
            <picture>
              <img style="width: 7rem;" 
                src="https://encurtador.com.br/pDR78" alt="img_cesta">
              <!-- <img src="../../mock/img/mock_to_product.png" alt="img_mock"> -->
            </picture>
            <p>
              {{products.filter((e)=>e.id === order_product.product)[0].name}}
            </p>
            <p>
              <input disabled type="number" v-model="order_product.quantity" min="1">
            </p>
            <p>
              R$ {{order_product.total_price}}
            </p>
          </li>
        </ul>
      </div>
        <button @click="this.router.push({name: 'dashboard'});">Voltar</button>
        <!-- <p>{{orderOpen[0]}}</p>     -->

    </div>
  </template>
  
  // ____________SCRIPT____________
  <script>
  import apiAccount from '@/services/clients/apiClientService';
  import { useRoute, useRouter } from 'vue-router';
  import apiAccountService from '@/services/clients/apiClientService';
  import apiOrderService from '@/services/order/apiOrderService';
  import apiProductService from '@/services/products/apiProductService';
  import apiAddressService from '@/services/addresses/apiAddressService';
  
  export default {
      data() {
          return {
            active: "",
            router: useRouter(),
            formData: {},
            user: {},
            orderOpen: [],
            orderProducts: [],
            products: [],
            address: {},
            showAddres: false
        }
      },
      methods: {
        async editOrder(){
          await apiOrderService.updateOrder({id: this.orderOpen[0].id, status:1}).then((response)=>{
            this.router.push({name: 'order'});
            })
            },
            async load_data(){
              await apiAccountService.getAccount(this.user_id).then((response)=>{
                this.user = response.data[0]
                })
                await apiOrderService.getOrder().then((response) => {
                  this.orderOpen = response.data.filter(order => order.status != 4)
                  })
                  await apiProductService.ProductsInOrderAccountView().then((response)=>{
                    if (response == "Nenhum pedido encontrado para este usuário."){
                      console.log("___________________________________________")
                      this.router.push({name: 'dashboard'});
                } 
              this.orderProducts = response.data.order_products
              this.products = response.data.products
            })
            await apiAddressService.getAddress(this.orderOpen[0]?.delivery_address).then((response)=>{
              this.address = response.data
              console.log(this.orderOpen)
            })
        }
      },
      mounted() {
        this.load_data()
      },
  };
  </script>
  
  <style>
    .cont_all{
      display: flex;
      height: 100%;
      width: 100%;
      flex-direction: column;
      align-items: center;
      
    }
    .cont-header{
      top: 0;
      height: 100%;
      width: 100%;
      background-color: green;
      justify-content: center;
      display: flex;
      width: 95%;
      height: 80px;
      align-items: center;
      font-size: x-large;
      color: white;
      margin: 3vh;
      border-radius: 7px;
    }
    .cont-info-address{
      display: flex; 
      justify-content: space-around; 
      align-items: center;
      width: 100%;
      padding: 3%;
    }
    .span{
      padding: 0.5rem;
      border-radius: 7px;
      color: white;
      cursor: pointer;
    }
    .span-entrega{
      background-color: orange;
    }
    .span-retirada{
      background-color: green;
    }
    .span-address{
      background-color: black;
      color: white;
      
    }
    .written-address{
      position: fixed;
      width: 70%;
      text-align: center;
      padding: 0.3rem;
      font-size: 0.8rem;
      background-color: white;
      border: 1px solid;
      border-radius: 7px;
      cursor: pointer;
      z-index: 1;
    }
    .button-trash, bg-trash{
      border-radius: 7px;
      width: 30%;
      border: none;
      padding: 5px;
      cursor: pointer;
      opacity: 0.4;
      background-color: rgba(197, 9, 9, 0.844);
      color: white;
    }
    .button-trash:hover{
      box-shadow: 1px 1px 3px black;
      opacity: 1;
    }
    .button-trash:active{
      box-shadow: -1px 1px 1px black inset;
      /* box-shadow: none; */
      /* opacity: 0.3; */

    }
    .ul-products{
      display: flex;
      flex-direction: column;
    }
    .li-product{
      background-color: rgb(227, 221, 221);
      justify-content: space-between;
      padding: 0.5rem 1rem;
      align-items: center; 
      border-radius: 7px;
      margin-top: 1rem;
      display: grid;
      grid-template-columns: 40% 20% 10% 20%; 
      width: 100%; 
    }
    .li-product img{
      border-radius: 10px;
    }
    .li-product input{
      max-width: 2rem;
    }
    .cont-products{
      width: 100%
    }
  </style>
  