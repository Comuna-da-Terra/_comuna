<template>
    <div class="cont-all">
      <div class="cont-search-products">
        <div class="cont-input-search">
          <input v-model="searchValue" type="search" placeholder="O que você está procurando?" class="inp-search">
          <button class="btn-search" @click="searchProduct()"><h2 class="pi pi-search"></h2></button>
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
                <span>{{ product.likely_stock }} UNIDADES</span>
                <!-- <span>GRT {{ product.garanteed_stock }}</span> -->
              </div>
              <div class="cont-quantity-controls">
                <!-- <button @click="increaseAmountProduct(product.id, index)">+</button> -->
                <button class="btn-pedido-aberto" v-if="cestaToBuy?.order?.status >= 2" @click="router.push({name: `Pedido`})" >
                  <!-- Pedido aberto  -->
                  <i class="pi pi-shopping-bag" style="color: whitesmoke; font-size: 1rem" ></i>
                </button>
                <div v-else>
                  <input type="text" v-model="orderAmount[index]" placeholder="0"/>
                  <!-- <button @click="decreaseAmountProduct(product.id, index)">-</button> -->
                  <button @click="createOrderProduct(product, index )" >
                    <i class="pi pi-cart-plus" style="color: whitesmoke; font-size: 1rem" ></i>
                  </button>
                </div>
              </div>
            </div>
          </li>
        </ul>
        <div style="display: flex; justify-content: space-around; padding-bottom: 15px;">
          <i @click="previousPage()" class="pi pi-chevron-circle-left" style="color: black; font-size: 1.5rem" ></i>
          <h2 style="display: flex; text-align: center; justify-content: center;">Anterior</h2>
          <h2 style="display: flex; text-align: center; justify-content: center;">Próxima</h2>
          <i @click="nextPage()" class="pi pi-chevron-circle-right" style="color: black; font-size: 1.5rem" ></i>
        </div>
      </div>
      <div v-if="cestaToBuy?.order?.status == 1" class="cont-basket" @click="finishOrder" >
        <h1 class="pi pi-shopping-bag" style="text-align: center; font-size: 2rem;"></h1>
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
    async searchProduct(){
      for (let index = 0; index < this.categories.length; index++) {
        if(this.searchValue == ''){
          return this.$notify({ type: "error", text: "Hum... informe o que deseja procurar!", duration: 2000});
        } else if (this.normalizeStrings(this.categories[index].name).includes(this.normalizeStrings(this.searchValue))){
          return this.productsShow = this.products.filter((product) => product.category === this.categories[index].id )
        }
      }
      
      await apiProductService.getAllProducts().then(response =>{
          this.products = response.data
          this.productsShow = this.products
        })

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
        apiProductService.ProductsInOrderAccountView().then((response)=>{ 
          this.cestaToBuy = response.data 
        })
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
  background-color: rgb(255, 255, 255);
  width: 100%;
  position: fixed;
  z-index: 1;
}
input::placeholder {
  color: #000;
}
.btn-search{
  border-radius:0px 7px 7px 0px ;
}
.cont-body{
  margin-top: 130px;
  width: 100%;
  
}
.cont-input-search {
  width: 100%;
  display: flex;
  justify-content: center;
}
.cont-input-search input {
  border-radius: 7px 0px 0px 7px ;
  height: 3rem;
  width: 80%;
  font-size: 1rem;
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
  padding: 0px 1rem;
  
}
.cont-list-product li {
  display: flex;
  margin: 0.3em;
  flex-direction: row;
  height: fit-content;
}
.cont-item-product{
  width: 290px;
  height: 6rem;
  display: flex;
  justify-content: space-around;
}
picture{
  width: 100px;
  align-items: center;
}
.cont-item-product img {
  width: 75%;
  height: 75%;
  border-radius: 7px;
}

.cont-data-product {
  width: 30%;
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
  width: 2em;
  align-items: center;
  justify-content: space-evenly;
  /* flex-direction: column; */
  
}

.cont-quantity-controls button {
  background-color: rgb(28, 115, 28);
  color: white;
  width: 2em;
  height: fit-content;
  border: none;
  cursor: pointer;
  border-radius: 0px 0px 8px 8px;
  font-size: 1.4rem;
  padding: 0.2rem 0.4rem;
}

.cont-quantity-controls input {
  width: 100%;
  border: none;
  border-radius: 8px 8px 0px 0px;
  font-size: 1.4rem;
  text-align: center;
}
.cont-quantity-controls input::placeholder {
  color: grey;
}
.cont-type-product{
  bottom: 0;
}
.cont-basket{
  animation: pulse 1s ease-in-out infinite;
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 27%;
  z-index: 2;
  right: 0%;
  padding: 1rem;
  background-color: orange;
  opacity: 0.7;
  border-radius: 50%;
  transition: bottom 0.5s ease;
}
.cont-basket:hover{
  opacity: 1;
  width: 5rem;
  height: 5rem;
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

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}
</style>
  