<template>
    <main class="cont_all">
      <div class="cont-header">
        <h1 v-if="orderOpen[0]?.status == 2">
          Pedido Aberto
        </h1>
        <h1 v-else>
          Pedido Fechado
        </h1>
      </div>
      <div class="cont-info-address">
        <span class="span span-entrega"  v-if="orderOpen[0]?.delivery === true">ENTREGAR</span>
        <span class="span span-retirada" v-else="orderOpen[0]?.delivery === false">RETIRADA</span>
        <p>
          {{ address.street }}, {{ address.number }} - {{ address.neighborhood }} - {{ address.city }}/{{ address.uf }}
        </p>
        <p>
          R$ {{ orderOpen[0]?.subtotal }}
        </p>
        <button class="button-pencil" @click="editOrder()">
          <i class="pi pi-pencil"></i>
        </button>
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
              <input type="number" v-model="order_product.quantity" min="1">
            </p>
            <p>
              R$ {{order_product.total_price}}
            </p>
            <button>
              Alterar
            </button>
          </li>
        </ul>
      </div>
        <button @click="this.router.push({name: 'dashboard'});">Voltar</button>
        <!-- <p>{{orderOpen[0]}}</p>     -->

    </main>
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
            router: useRouter(),
            formData: {},
            user: {},
            orderOpen: [],
            orderProducts: [],
            products: [],
            address: {}
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
                this.orderOpen = response.data
            })
            await apiProductService.ProductsInOrderAccountView().then((response)=>{
              this.orderProducts = response.data.order_products
              this.products = response.data.products
            })
            await apiAddressService.getAddress(this.orderOpen[0]?.delivery_address).then((response)=>{
              this.address = response.data
            })
        }
      },
      mounted() {
        this.load_data()
      },
  };
  </script>
  
  <style>
    .cont-header{
      background-color: green;
      justify-content: center;
      display: flex;
      width: 95%;
      height: 80px;
      align-items: center;
      font-size: x-large;
      color: white;
      margin: 1rem;
      border-radius: 7px;
    }
    .cont-info-address{
      display: flex; 
      justify-content: space-around; 
      align-items: center;
      width: 100%;
    }
    .span{
      padding: 0.5rem;
      border-radius: 7px;
      color: white;
    }
    .span-entrega{
      background-color: orange;
    }
    .span-retirada{
      background-color: green;
    }
    .button-pencil{
      background-color: grey;
      border-radius: 7px;
      border: none;
      padding: 5px;
      cursor: pointer;
    }
    .button-pencil:hover{
      box-shadow: 1px 1px 3px black;
    }
    .button-pencil:active{
      box-shadow: none;
    }
    .pi-pencil{
      color: white;
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
      display: flex; 
      width: 100%; 
    }
    .li-product img{
      border-radius: 10px;
    }
    .cont-products{
      width: 100%
    }
  </style>
  