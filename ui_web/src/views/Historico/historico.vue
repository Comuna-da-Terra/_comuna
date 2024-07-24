<template>
    <div class="in-development">Em desenvolvimento...</div>
    <main class="cont_all">
        <div class="cont-header">
            <button type="button" class="btn-submit">
            <i class="pi pi-times" @click="this.router.push({name: 'dashboard'});"></i>
            </button>
            <h1>
                Histórico
            </h1>
            <button class="btn-submit" type="submit">
            <i class="pi pi-check" type="submit" ></i>
            </button>
        </div>

        <div>
            <ul class="list-orders" style="width: 100%;">
                <li :id="`li-order(${index})`" v-for="(order, index) in orders" :key="index">
                    <div :id="`cont-details-order(${index})`" class="cont-details-order change-border-close">
                        <p>{{ dateString(new Date(order["date"])) }}</p>
                        <span style="color: blue;" v-if="order['status'] < 4">EM PROCESSO</span>
                        <span style="color: green;" v-else-if="order['status'] >= 4 && order['delivery'] == true">ENTREGUE</span>
                        <span style="color: orange;" v-else="order['status'] >= 4 && order['delivery'] == false">RETIRADO</span>
                        <span class="span span-address" @click="toggleSeeAddress(order, index)"> ENDEREÇO </span>
                        <p v-if="order.see_address" class="written-address">
                            {{ order["address"] }}
                        </p>
                        <span>Total: R${{ order["subtotal"] }} </span>
                        <p><button @click="toggleSeeProducts(order, index)">PRODUTOS</button></p>
                    </div>
                    <div>
                        <ul v-if="order.see_products">
                            <li style="list-style: none;" v-for="product, index in order.order_product" :key="index">
                                <div class="cont-prodycts-order">
                                    <!-- <p v-if="listProductUnavailable.find(item => item.name == product.name) == null">{{ product.name }}</p> -->
                                    <p>{{ product.name }}</p>
                                    <p>{{ product.quantity }}</p>
                                </div>
                            </li>
                        </ul>
                    </div>
                </li>
            </ul>
        </div>
        
    </main>
  </template>
  
  // ____________SCRIPT____________
  <script>
  import apiOrderService from '@/services/order/apiOrderService';
  import { useRoute, useRouter } from 'vue-router';
  
  export default {
      data() {
          return {
            router: useRouter(),
            orders: [],
          }
      },
      methods: {
        handleSubmit() {},
        async load_data(){
            await apiOrderService.getHistoryOrders().then((response) => {
                this.orders = response.data
            console.log(this.orders)})
        },
        dateString(date){
            return date.toLocaleDateString('pt-BR', {day: '2-digit', month: 'long', year: 'numeric'})},
        toggleSeeAddress(order, index) {
            order.see_address = !order.see_address },
        toggleSeeProducts(order, index) {
            order.see_products = !order.see_products;
            const myDiv = document.getElementById(`cont-details-order(${index})`)
            if (myDiv.classList.contains("change-border-close")){
                myDiv.classList.remove("change-border-close");
                myDiv.classList.add("change-border-open");
            }else{
                myDiv.classList.remove("change-border-open");
                myDiv.classList.add("change-border-close");
            }
        },
      },
      mounted() {
        this.load_data()
      },
  };
  </script>
  
  <style>
  .in-development{
    width: 100%;
    height: 2rem;
    text-align: center;
    background-color: orange;
    font-size: x-large;
    position: absolute;
    top:0
  }
    .cont_all{
        height: 100%;
        display: flex;
        justify-content: flex-start;
    }
    .cont-header{
        background-color: green;
        justify-content: space-around;
        display: flex;
        width: 95%;
        height: 80px;
        align-items: center;
        font-size: x-large;
        color: white;
        margin: 0rem 1rem 1rem 1rem;
        border-radius: 7px;
    }
    .btn-submit{
        border: none;
        background-color: transparent;
    }
    .pi{
        color: white;
    }
    .list-orders{
    height: 100%;
}
.li-order {
    display: flex;
    flex-direction: column;
    margin: 1rem;
    list-style: none;
}
.unavailable{
    background-color: rgba(255, 0, 0, 0.507);
}

.cont-details-order {
    display: grid;
    grid-template-columns: 2fr 2fr 2fr 1fr 1fr;
    justify-content: space-around;
    align-items: center;
    padding: 0.5rem;
    border: 1px solid;
    gap: 1rem;
}
.cont-details-order p{
    width: fit-content;
    display: flex;
    justify-content: center;
    font-weight: bold;
}
.change-border-close{
    border-radius: 5px 5px 5px 5px;
}
.change-border-open{
    border-radius: 5px 5px 0px 0px;
}
.written-address{
    position: fixed;
    text-align: center;
    padding: 1rem;
    font-size: 0.8rem;
    background-color: white;
    border: 1px solid;
    border-radius: 7px;
    cursor: pointer;
}

.cont-prodycts-order {
    display: grid;
    grid-template-columns: 1fr 70px 60px;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 2rem 1rem 2rem;
    border: 1px solid grey;
    list-style: none;
}
.cont-prodycts-order p{
    display: flex;
    justify-content: start;
    font-weight: bolder;
    color: grey;
}

.cont-details-order span {
    width: fit-content;
    border: 0.5px solid;
    border-radius: 5px;
    padding: 3px;
    font-size: 70%;
}
  </style>
  