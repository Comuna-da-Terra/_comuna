<template>
    <div class="cont_all">
      <ul class="cont_product">
        <h2 style="display: flex; text-align: center; justify-content: center;">Lista de Produtos</h2>
        <li v-for="(product, index) in products" :key="index">
          <picture>
            <img src="https://encurtador.com.br/pDR78" alt="img_cesta">
            <!-- <img src="../../mock/img/mock_to_product.png" alt="img_mock"> -->
          </picture>
          <div class="cont-body-product">
            <div class="cont-data-product">
              <label>{{ product.name }} - R$ {{ product.price }}</label>
              <div v-if="product.type != 'Comum'" class="cont-type-product">
                <label>
                  <input type="radio" checked v-model="productSizes[index]" value="P" /> P
                </label>
                <label>
                  <input type="radio"  v-model="productSizes[index]" value="M" /> M
                </label>
                <label>
                  <input type="radio" v-model="productSizes[index]" value="G" /> G
                </label>
              </div>
            </div>
            <div class="quantity-controls">
              <button @click="increaseAmountProduct(product.id, index)">+</button>
              <input type="text" v-model="orderAmount[index]" placeholder="0"/>
              <button @click="decreaseAmountProduct(product.id, index)">-</button>
            </div>
            <button @click="createOrderProduct(product, index )" >Quero!</button>

          </div>
        </li>
      </ul>
    </div>
    <div v-if="cestaToBuy?.order" class="cont_basket" >
      <h2 style="text-align: center;">Cesta</h2>
      <div style="display: flex; position: fixed; margin-left: 1.5rem; margin-top: -1rem;">
        <button v-if="!viewListBasket" @click="viewListBasket = true"> Ver mais</button>
        <button v-if="viewListBasket" @click="viewListBasket = false"> Ver menos</button>
      </div>
      <div style="display: flex; justify-content: space-around; margin: 0.5rem;">
        <p> Unidades: {{ cestaToBuy?.order_products.reduce((acc, item) => acc + item.quantity, 0) }}</p>
        <p> Valor Total: {{ cestaToBuy?.order.subtotal }}</p>
        <button @click="finishOrder"> Finalizar Pedido</button>
       
      </div>
      <ul class="cont-list-basket" v-if="viewListBasket">
        <li v-for="(order_product, index) in cestaToBuy.order_products" :key="index">
          <p>
            {{ cestaToBuy.products[index].name }}
          </p>
          <p>
            {{ cestaToBuy.products[index].type }}
          </p>
          <p>
            {{ order_product.quantity }} 
          </p>
          <p>
            R$  {{ order_product.total_price }}
          </p>
          <button @click="removeFromBasket(order_product.id, index)">Remover</button>
        </li>
      </ul>
    </div>
</template>
  
  // ____________SCRIPT____________
<script>
import apiOrderProductService from '../../services/orderProduct/apiOrderProductService'
import apiProductService from "../../services/products/apiProductService"
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {
  data() {
    const authStore = useAuthStore();

    return {
      router: useRouter(),
      products: [
        {
          id: 1,
          name: "Abacate",
          stock: 7,
          price: 8.15,
        },
        {
          id: 2,
          name: "Banana",
          
          stock: 7,
          price: 7.00,
          type: "M",
        },
        {
          id: 3,
          name: "Alface",
          stock: 7,
          price: 6.00,
        },
        {
          id: 4,
          name: "Berinjela",
          stock: 7,
          price: 4.00,
          type: "P",
        },
        {
          id: 5,
          name: "Colve",
          stock: 7,
          price: 7.00,
        }
      ],
      productSizes: [],
      orderAmount: [],
      cestaToBuy: [],
      viewListBasket: false,
      id_user: authStore.user_id,
    };
  },
  props: {},
  methods: {
    increaseAmountProduct(id, index) {
      this.orderAmount[index] = (this.orderAmount[index] || 0) + 1;
    },
    decreaseAmountProduct(id, index) {
      if (this.orderAmount[index] > 0) {
        this.orderAmount[index] -= 1;
      }
    },
    async createOrderProduct(product, index) {
      const data = {
        id_product: product.id,
        quantity: this.orderAmount[index],
        user: this.id_user
      }
      if (this.orderAmount[index] > 0 && this.orderAmount[index] !== undefined) {
        await apiOrderProductService.createOrderProduct(data).then((resp)=>{
          this.cestaToBuy = resp.data
        })
        this.load_data()
      } else {
        this.$notify({ type: "warn", text: "Por favor, selecione uma quatidade válida !", duration: 3000});
      }
      
    },
    async removeFromBasket(id, index) {
      await apiOrderProductService.deleteOrderProduct(id)
      this.load_data()
    },
    async finishOrder(){
      this.router.push({name: 'order'});
    },
    async load_data(){
      await apiProductService.getAllProducts().then((response)=>{
        this.products = response.data
      })
      await apiProductService.ProductsInOrderAccountView().then((response)=>{
        this.cestaToBuy = response.data
      })
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
}
.cont_product {
  width: 100%;
  display: flex;
  flex-direction: column;
  /* gap: 0.3rem; */
}

.cont_product li picture {
  width: 70%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.cont_product li img {
  width: 100%;
}

.cont_product li {
  display: flex;
  margin: 1rem;
}

.cont-body-product {
  width: 100%;
  display: flex;
  justify-content: space-around;
}

.cont-data-product {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.cont-type-product {
  display: flex;
}

.cont-type-product label {
  width: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}


.quantity-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;

}

.quantity-controls button {
  /* background: none; */
  width: 100%;
  height: 100%;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  padding: 0.2rem 0.4rem;
}

.quantity-controls input {
  border: none;
  padding: 0.2rem 0.4rem;
  font-size: 1rem;
  text-align: center;
  width: 2rem;
}
.cont-type-product{
  bottom: 0;
}
.cont_basket{
  position: fixed;
  bottom: 0;
  background-color: green;
  width: 95%;
  border-top-right-radius: 15px;
  border-top-left-radius: 15px;
}
.cont-list-basket li {
  flex: 1;
  display: flex;
  justify-content: space-around;
  margin: 1rem;
}
.cont-list-basket li p{
  text-align: center;
  flex-grow: 1;
}
</style>
  