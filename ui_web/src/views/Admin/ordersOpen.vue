<template>
    <div class="cont_all">

            <header>
                <h1 style="color: green;" v-if="ordersOpen.length == 0">Sem pedidos em aberto!</h1>
                <div v-else style="display: flex; justify-content: space-evenly; ">
                    <h1 style="color: green;" >Pedidos em aberto</h1>
                </div>
                <div class="cont-utils">
                    <!-- <input class="inp-search" type="search" placeholder="Procurar..."> -->
                    <button class="btn-stock active" style="color: green;" v-if="stockUnavailable == false"> </button>
                    <button class="btn-stock desactive" v-if="stockUnavailable == true" @click="filterOrdersAnavailable"> </button>
                    <button v-if="user.is_superuser" @click="requestCSV">Gerar Planilha</button>
                    <button v-if="user.is_superuser" @click="createEtiquette">Etiquetas</button>
                </div>
            </header>
            <ul class="list-orders">
                <li :id="`li-order(${index})`" :class="[ 'li-order']" v-for="(order, index) in ordersShow" :key="index">
                        <div style="display: flex; justify-content: center; width: 100%;">
                            <div :id="`cont-details-order(${index})`" 
                            :class="[
                                'cont-details-order', 
                                { 'unavailable': checkUnavailableItem(order)},
                                {'order-confirmed-color': checkOrderStatus(order)},
                                'change-border-close']">
                                <p>{{ order["client"] }}</p>
                                <span class="span span-address" @click="toggleSeeAddress(order, index)"> ENDEREÇO </span>
                                <p v-if="order.see_address" class="written-address" @click="toggleSeeAddress(order, index)" >
                                    {{ order["address"] }}
                                </p>
                                <span style="color: green;" v-if="order['delivery'] === true">ENTREGAR</span>
                                <span style="color: orange;" v-else="order['delivery'] === false">RETIRADA</span>
                                <p><button @click="toggleSeeProducts(order, index)">PRODUTOS</button></p>
                            </div>
                            <div style="display: flex; flex-direction: column; justify-content: space-around; gap: 3px; margin: 2px;">
                                <button @click="editOrder(order, status=3)" class="btn-order-status order-confirm pi pi-thumbs-up"></button>
                                <button @click="editOrder(order, status=4)" class="btn-order-status order-delivery pi pi-car" ></button>
                            </div>
                        </div>
                        <div>
                            <ul v-if="order.see_products">
                                <li style="list-style: none;" v-for="product, index in order.order_product" :key="index">
                                    <div class="cont-prodycts-order">
                                        <p v-if="notFindProduct.some(item => item.name === product.name)" style="color: red;">{{ product.name }},  NÃO DISPONÍVEL !</p>
                                        <p v-else-if="listProductUnavailable.find(item => item.name == product.name) == null">{{ product.name }}</p>
                                        <p v-else style="color: red;">{{ product.name }}</p>
                                        <span style="height: 10px; width: 10px; color: pink;">{{this.products.filter((item)=>item.name == product.name)[0].garanteed_stock}}</span>
                                        <input type="number" v-model="product.quantity">
                                        <button @click="editOrderProduct(order.order_product[index], product.quantity)" >EDITAR</button>
                                    </div>
                                </li>
                            </ul>
                        </div>
                    
                </li>
            </ul>
        <button @click="this.router.push({ name: 'admin' });">Voltar</button>
    </div>
</template>

  // ____________SCRIPT____________
<script>
import apiOrderProductService from '../../services/orderProduct/apiOrderProductService'
import apiProductService from "../../services/products/apiProductService"
import apiAccountService from '@/services/clients/apiClientService';
import apiOrderService from '@/services/order/apiOrderService';
import apiEtiquetteService from '@/services/etiquette/apiEtiquetteService'
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {
    data() {
        const authStore = useAuthStore();
        return {
            user_id: authStore.user_id,
            listProductUnavailable: [],
            listProductsInOrder: [],
            stockUnavailable: false,
            ordersUnavailable: [],
            router: useRouter(),
            showAddres: false,
            ordersOpen: [],
            ordersShow: [],
            products: [],
            user: {},
            notFindProduct: [],
        }
    },
    methods: {
        handleSubmit() { },
        async load_data() {
            await apiAccountService.getAccount(this.user_id).then((response) => {
                this.user = response.data[0]}
                )
            await apiOrderService.getOpenOrders().then((response) => {
                response.data.message ? this.ordersOpen = [] : this.ordersOpen = response.data
                this.ordersShow = this.ordersOpen}).catch((err)=>{
                    console.log(err)

                })
            await apiProductService.getAllProducts().then((response)=>{
                this.products = response.data})
            await this.verifyAmountProductAvailable()
        },
        checkUnavailableItem(order){
            const itemProducts = order.order_product
            let check = false
            let verifyUnavailableOrder = null
            itemProducts.forEach((item, index)=>{
                verifyUnavailableOrder != true ? 
                    verifyUnavailableOrder = this.listProductUnavailable.some((prod)=>{
                        return prod.id == item.id_product})
                    : verifyUnavailableOrder = true })
                if(verifyUnavailableOrder){
                    check = true
                    !this.ordersUnavailable.some(item => item.id === order.id) ? 
                        this.ordersUnavailable.push(order) : "_" }
            return check
        },
        checkOrderStatus(order){
            let check= false
            if(order.status > 2) {
                check = true
            } 
            return check
        },
        filterOrdersAnavailable(){
            this.ordersShow != this.ordersUnavailable ? 
                this.ordersShow = this.ordersUnavailable 
                : this.ordersShow = this.ordersOpen

        },
        toggleSeeAddress(order, index) {
            order.see_address = !order.see_address },
        toggleSeeProducts(order, index) {
            order.see_products = !order.see_products

            const myDiv = document.getElementById(`cont-details-order(${index})`)
            if (myDiv.classList.contains("change-border-close")){
                myDiv.classList.remove("change-border-close");
                myDiv.classList.add("change-border-open");
            }else{
                myDiv.classList.remove("change-border-open");
                myDiv.classList.add("change-border-close");
            }
        },
        async editOrderProduct(item, quantity){
            const data = { id: item.id, quantity: quantity }
            await apiOrderProductService.updateOrderProduct(data).then((response)=>{
                    this.load_data()
                    return this.$notify({ type: "success", text: "Order alterado com sucesso!", duration: 3000})}).catch((err)=>{
                            console.log(err)
                        })
                },
        async editOrder(order, status){
            if (this.checkUnavailableItem(order)){
                return this.$notify({ type: "warn", text: "Não possuimos todos os itens desse pedido!", duration: 3000})}
            const data = {
                id: order.id,
                status: status
            }
            await apiOrderService.updateOrder(data).then((response)=>{
                data.status == 3 
                    ? this.$notify({ type: "ok", text: "Pedido confirmado!", duration: 5000})
                    : this.$notify({ type: "success", text: "Pedido entregue com sucesso!", duration: 5000})
                this.load_data()

            })
        },

        async listAmountProductInAllOrders(){
            this.listProductsInOrder = []
            this.ordersOpen.map(order => {
                const order_product = order.order_product
                order_product.forEach(product => {
                    const existingProductIndex = this.listProductsInOrder.findIndex(item=>item.name === product.name);
                    existingProductIndex === -1 ?
                        this.listProductsInOrder.push({ name: product.name, quantity: product.quantity })
                        : this.listProductsInOrder[existingProductIndex].quantity += product.quantity
                });
            });
        },
        async verifyAmountProductAvailable() {
            await this.listAmountProductInAllOrders();
            this.listProductUnavailable = [];

            // Itera sobre cada item na lista de pedidos
            this.listProductsInOrder.forEach(item => {
                // Verifica se o produto correspondente existe
                const product = this.products.find(product => product.name === item.name);
                // Se o produto não for encontrado, pode registrar ou executar lógica adicional
                if (!product) {
                    console.log(`Produto não encontrado: ${item.name}`);
                    this.notFindProduct.push(item)
                    return; // Sai da iteração se o produto não existir
                }

                // Verifica a quantidade e atualiza as informações do item
                if (item.quantity > product.garanteed_stock ) {
                    item.id = product.id;
                    item.available = product.garanteed_stock;
                    item.variation = item.quantity - product.garanteed_stock;
                    this.listProductUnavailable.push(item);
                }
            });

    // Atualiza a disponibilidade de estoque após todos os produtos terem sido verificados
    this.stockUnavailable = this.listProductUnavailable.length > 0;
},

        async requestCSV(){
            await apiOrderService.getOrdersCSV()
        },
        async createEtiquette(){
            await apiEtiquetteService.emitEtiquette(this.ordersOpen)

        },
        },
    async mounted() {
        await this.load_data()},
};
</script>

<style scoped>
.cont_all{
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.cont-utils{
    margin: 0px 0.1rem;
    display: grid;
    grid-template-columns: 33% 33% 33%;
    justify-content: space-around;
    justify-items: center;
    align-items: center;
}
.inp-search{
    padding: 1rem;
    width: 100%;
}
.btn-stock{
    height: 1.3rem;
    width: 1.3rem;
    border: none;
    border-radius: 50%;
    cursor: pointer;
}
.btn-stock.desactive{
    background-color: red;
    box-shadow: 0px 0px 7px red;
}
.btn-stock.active{
    background-color: green;
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
.btn-order-status{
    width: 1.5rem;
    height: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    border: none;
    border-radius: 10%;
    color: white;
    cursor: pointer;
}
.order-confirm{
    background-color: blue;
}
.order-delivery{
    background-color: green;
}
.unavailable{
    background-color: rgba(255, 0, 0, 0.507);
}
.order-confirmed-color{
    background-color: rgba(0, 128, 0, 0.332);
}
/* .order-delivered-color{
    background-color: green;
} */
.cont-details-order {
    display: grid;
    grid-template-columns: 2fr 2fr 2fr 1fr;
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
    grid-template-columns: 1fr 30px 70px 60px;
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
    padding: 3px;
    font-size: 70%;
}
</style>
