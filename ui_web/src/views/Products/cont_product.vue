<template>
    <div class="cont-all">
      <div class="cont-search-products">
        <div class="cont_input_search">
          <input v-model="searchValue" type="search" placeholder="O que você está procurando?">
          <button @click="searchProduct()">Search</button>
        </div>
        <ul class="list-cateogry">
          <li v-for="(category, index) in categories" :key="index" @click="filterProducts(category.id)" >{{category.name}}</li>
          <li @click="productsShow = products">Todos..</li>
        </ul>
      </div>
      <div class="cont-body">
        <div style="display: flex; justify-content: space-around; margin-top: 1rem;">
          <i @click="previousPage()" class="pi pi-chevron-circle-left" style="color: black; font-size: 1.5rem" ></i>
          <h2 style="display: flex; text-align: center; justify-content: center;">Lista de Produtos</h2>
          <i @click="nextPage()" class="pi pi-chevron-circle-right" style="color: black; font-size: 1.5rem" ></i>
        </div>
        <ul class="cont-list-product">
          <li v-for="(product, index) in productsShow" :key="index">
            <div class="cont-item-product">
              <picture style="display: flex;">
                <img src="https://encurtador.com.br/pDR78" alt="img_cesta">
                <!-- <img src="../../mock/img/mock_to_product.png" alt="img_mock"> -->
              </picture>
              
              <div class="cont-data-product">
                <span>{{ product.name }}</span>
                <span>R$ {{ product.price }}</span>
                <span> INF {{ product.likely_stock }}</span>
                <span>GRT {{ product.garanteed_stock }}</span>
              </div>
              <div class="cont-quantity-controls">
                <!-- <button @click="increaseAmountProduct(product.id, index)">+</button> -->
                <button v-if="cestaToBuy?.order?.status >= 2" @click="router.push({name: `Pedido`})" >
                  Pedido aberto 
                  <i class="pi pi-shopping-bag" style="color: whitesmoke; font-size: 1.5rem" ></i>
                </button>
                <div v-else>
                  <input type="text" v-model="orderAmount[index]" placeholder="0"/>
                  <!-- <button @click="decreaseAmountProduct(product.id, index)">-</button> -->
                  <button @click="createOrderProduct(product, index )" >
                    <i class="pi pi-cart-plus" style="color: whitesmoke; font-size: 1.5rem" ></i>
                  </button>
                </div>
              </div>
            </div>
          </li>
        </ul>
        <div style="display: flex; justify-content: space-around; padding-bottom: 15px;">
          <i @click="previousPage()" class="pi pi-chevron-circle-left" style="color: black; font-size: 1.5rem" ></i>
          <h2 style="display: flex; text-align: center; justify-content: center;">Previous</h2>
          <h2 style="display: flex; text-align: center; justify-content: center;">Next</h2>
          <i @click="nextPage()" class="pi pi-chevron-circle-right" style="color: black; font-size: 1.5rem" ></i>
        </div>
      </div>
      <div v-if="cestaToBuy?.order?.status == 1" class="cont_basket" >
        <h2 style="text-align: center;">Cesta</h2>
        <div style="display: flex; position: fixed; margin-left: 1.5rem; margin-top: -1rem;">
          <button v-if="!viewListBasket" @click="viewListBasket = true"> Ver mais</button>
          <button v-if="viewListBasket" @click="viewListBasket = false"> Ver menos</button>
        </div>
        <div style="display: flex; justify-content: space-around; margin: 0.5rem;">
          <p> Unidades: {{ cestaToBuy.order_products?.reduce((acc, item) => acc + item.quantity, 0) }}</p>
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
              <input type="number" v-model="order_product.quantity" min="1">
            </p>
            <p>
              R$  {{ order_product.total_price }}
            </p>
            <button @click="editOrderProduct(order_product.id, order_product.quantity)">Editar</button>
            <button @click="removeFromBasket(order_product.id, index)">Remover</button>
          </li>
        </ul>
      </div>
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
      user: authStore.user,
      categories: [],
      searchValue: '',
      page: 1,
      maxPage: 0
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
    async nextPage(){
      if(this.page < this.maxPage){
        this.page += 1
        await apiProductService.getPageProducts(this.page).then((response)=>{
          this.products = response.data.results
          this.productsShow = this.products
        })
      }
    },
    async previousPage(){
      if(this.page >= 2){
        this.page -= 1
        await apiProductService.getPageProducts(this.page).then((response)=>{
          this.products = response.data.results
          this.productsShow = this.products
        })
      }
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
        product: product.id,
        quantity: this.orderAmount[index],
        user: this.user.id
      }
      if (this.orderAmount[index] > 0 && this.orderAmount[index] !== undefined) {
        await apiOrderProductService.createOrderProduct(data).then((resp)=>{
          apiProductService.ProductsInOrderAccountView().then((response)=>{ this.cestaToBuy = response.data })
            this.orderAmount[index] = 0
            return this.$notify({ type: "success", text: "Produto adicionado !", duration: 3000});
        }).catch((err)=> {
          return this.$notify({ type: "warn", text: err.response.data.results, duration: 3000});
        })
        
      } else {
        this.$notify({ type: "warn", text: "Por favor, selecione uma quatidade válida !", duration: 3000});
      }
      
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
    },
    async finishOrder(){
      this.router.push({name: 'order'});
    },
    async load_data(){
      await apiProductService.getPageProducts().then((response)=>{
        this.maxPage = Math.ceil((response.data.count) / 20)
        console.log(response)
        this.products = response.data.results
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
.cont-all{
  height: 100%;
  width: 100vw;
  display: flex;
  justify-content: center;
}
.cont-search-products{
  padding-top: 68px;
  background-color: green;
  width: 100%;
  position: fixed;
}
.cont-body{
  margin-top: 130px;
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
.cont-list-product {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  
}
.cont-list-product li {
  display: flex;
  margin: 0.3em;
  flex-direction: row;
  height: fit-content;
}
.cont-item-product{
  width: 100%;
  max-width: 480px;
  min-width: 376px;
  height: 6rem;
  display: flex;
  justify-content: space-between;
}
.cont-item-product img {
  width: 7em;
  border-radius: 7px;
}

.cont-data-product {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
.cont-data-product span {
  font-weight: bolder;
  font-size: 0.7rem;
  width: 100%;
  text-align: center;
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

.cont-quantity-controls {
  display: flex;
  width: 5em;
  align-items: center;
  justify-content: space-evenly;
  flex-direction: column;

}

.cont-quantity-controls button {
  background-color: rgb(28, 115, 28);
  color: white;
  width: 5em;
  height: fit-content;
  border: none;
  cursor: pointer;
  border-radius: 10px;
  font-size: 1rem;
  padding: 0.2rem 0.4rem;
}

.cont-quantity-controls input {
  width: 100%;
  border: none;
  font-size: 2rem;
  text-align: center;
}
.cont-quantity-controls input::placeholder {
  color: grey;
}
.cont-type-product{
  bottom: 0;
}
.cont_basket{
  position: fixed;
  bottom: -65px;
  background-color: green;
  width: 95%;
  border-top-right-radius: 15px;
  border-top-left-radius: 15px;

  /* transform: translateX(-50%); */
  transition: bottom 0.5s ease;
}
.cont_basket:hover{
  bottom: 0;
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
.pi{
  cursor: pointer;
}
</style>
  