<template>
    <div class="cont_all">
      <div class="cont_body">
            <div class="cont_input_search">
                <input v-model="searchValue" type="search" placeholder="O que você está procurando?">
                <button @click="searchProduct()">Search</button>
            </div>
            <ul class="list-cateogry">
                <li v-for="(category, index) in categories" :key="index" @click="filterProducts(category.id)" >{{category.name}}</li>
                <li @click="productsShow = products">Todos..</li>
            </ul>
        </div>
      <ul class="cont_product">
        <h2 style="display: flex; text-align: center; justify-content: center;">Lista de Produtos</h2>
        <li v-for="(product, index) in productsShow" :key="index">
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
import apiCategoryService from "../../services/category/apiCategoryService"
import apiProductService from "../../services/products/apiProductService"
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {
  data() {
    const authStore = useAuthStore();

    return {
      router: useRouter(),
      products: [],
      productsShow: [],
      productSizes: [],
      orderAmount: [],
      cestaToBuy: [],
      viewListBasket: false,
      id_user: authStore.user_id,
      categories: [],
      searchValue: ''
    };
  },
  props: {},
  methods: {
    filterProducts(idCategory){
      this.productsShow = this.products.filter((product)=> product.category === idCategory)
    },
    searchProduct(){
      for (let index = 0; index < this.categories.length; index++) {
        if(this.searchValue == ''){
          return this.$notify({ type: "error", text: "Hum... informe o que deseja procurar!", duration: 2000});
        } else if (this.normalizeStrings(this.categories[index].name).includes(this.normalizeStrings(this.searchValue))){
          return this.productsShow = this.products.filter((product) => product.category === this.categories[index].id )
        }
      }

      for (let index = 0; index < this.products.length; index++) {
        if(this.normalizeStrings(this.products[index].name).includes(this.normalizeStrings(this.searchValue))){
          return this.productsShow = this.products.filter((product) => this.normalizeStrings(product.name).includes(this.normalizeStrings(this.searchValue))) 
        } 
      }
      return this.$notify({ type: "error", text: "Hum... Não temos nada sobre isso!", duration: 2000});
    },
    normalizeStrings(string){
      return string.normalize('NFD').replace(/[\u0300-\u036f]/g, "").toLowerCase()
    },
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
        await apiProductService.ProductsInOrderAccountView().then((response)=>{ this.cestaToBuy = response.data })
        this.orderAmount[index] = 0
        return this.$notify({ type: "success", text: "Produto adicionado !", duration: 3000});
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
        this.productsShow = this.products
      })
      await apiProductService.ProductsInOrderAccountView().then((response)=>{
        this.cestaToBuy = response.data
      })
      await apiCategoryService.getListCategory().then((response)=>{
          this.categories = response.data
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
  width: 100%;
}
.cont_body{
    width: 100%;
}
.cont_input_search {
    width: 100%;
    display: flex;
    justify-content: center;
}
.cont_input_search input {
    height: 3rem;
    width: 80%;
    font-size: 1rem;
    border-radius: 7px;
    padding: 1rem;
}
.list-cateogry {
    display: flex;
    justify-content: space-around;
    width: 100%;
    list-style: none;
    padding: 0;
}

.list-cateogry li {
    cursor: pointer;
}
.cont_product {
  width: 100%;
  display: flex;
  flex-direction: column;
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
  width: 100%;
  height: 100%;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  padding: 0.2rem 0.4rem;
}

.quantity-controls input {
  background-color: gray;
  border: none;
  padding: 0.2rem 0.4rem;
  font-size: 1rem;
  text-align: center;
  width: 2rem;
}
.quantity-controls input::placeholder {
  color: black;
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
  