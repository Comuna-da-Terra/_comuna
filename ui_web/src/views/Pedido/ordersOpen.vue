<template>
    <main class="cont_all">
        <h1 style="color: green;" v-if="orderOpens.length == 0">Sem pedidos em aberto!</h1>
        
        <div v-else-if="orderOpens.length > 0">
            <div style="display: flex; justify-content: space-evenly; ">
                <h1 style="color: green;" >Pedidos em aberto</h1>
                <button v-if="user.is_superuser" @click="requestCSV">Gerar Planilha</button>
            </div>
            <ul style="width: 100%;">
                <li class="li-order" v-for="(order, index) in orderOpens" :key="index">
                    <div :id="`cont-details-order(${index})`" class="cont-details-order change-border-close">
                        <p>{{ order["client"] }}</p>
                        <p>{{ order["address"] }}</p>
                        <span style="color: green;" v-if="order['delivery'] === true">ENTREGAR</span>
                        <span style="color: orange;" v-else="order['delivery'] === false">RETIRADA</span>
                        <p><button @click="toggleSeeProducts(order, index)">PRODUTOS</button></p>
                    </div>
                    <div>
                        <ul v-if="order.see_products">
                            <li style="list-style: none;" v-for="product, index in order.order_product" :key="index">
                                <div class="cont-prodycts-order">
                                    <p>{{ product.name }}</p>
                                    <input type="number" v-model="product.quantity">
                                    <button @click="editOrder(order.order_product[index], product.quantity)" >EDITAR</button>
                                </div>
                            </li>
                        </ul>
                    </div>
                </li>
            </ul>
        </div>
        
        <button @click="this.router.push({ name: 'dashboard' });">Voltar</button>

    </main>
</template>
  
  // ____________SCRIPT____________
<script>
import apiAccountService from '@/services/clients/apiClientService';
import apiOrderService from '@/services/order/apiOrderService';
import apiOrderProductService from '../../services/orderProduct/apiOrderProductService'
import apiProductService from "../../services/products/apiProductService"
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {
    data() {
        const authStore = useAuthStore();
        return {
            router: useRouter(),
            orderOpens: [],
            user: {},
            user_id: authStore.user_id,
        }
    },
    methods: {
        handleSubmit() { },
        async load_data() {
            await apiAccountService.getAccount(this.user_id).then((response) => {
                this.user = response.data[0]
            })
            await apiOrderService.getOpenOrders().then((response) => {
                this.orderOpens = response.data
                console.log(this.orderOpens)
            })
            await apiProductService.ProductsInOrderAccountView().then((response)=>{
                const test = response.data 
                console.log(test)
            })
        
        },
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
        async editOrder(order_product, quantity){
            console.log(order_product)
       
            const data = {
                id: order_product.id,
                quantity: quantity,
            }
            await apiOrderProductService.updateOrderProduct(data).then((resp)=>{
                const test = apiProductService.ProductsInOrderAccountView().then((response)=>{ this.cestaToBuy = response.data })
                console.log(test)
                return this.$notify({ type: "success", text: "Order alterado com sucesso!", duration: 3000});
        })
        },
        async requestCSV(){
            await apiOrderService.getOrdersCSV()
        }
    },
    async mounted() {
        await this.load_data()
    },
};
</script>
  
<style scoped>
.li-order {
    display: flex;
    flex-direction: column;
    margin: 1rem;
    list-style: none;
}

.cont-details-order {
    display: grid;
    grid-template-columns: 2fr 3fr 1fr 1fr;
    justify-content: space-around;
    align-items: center;
    padding: 0.5rem;
    border: 1px solid;
    gap: 1rem;
}
.cont-details-order p, span{
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

.cont-details-order p {
    width: fit-content;
}

.cont-details-order span {
    border: 0.5px solid;
    border-radius: 5px;
    padding: 2px;
}
</style>
  