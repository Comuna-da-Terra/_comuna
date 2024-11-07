<template>
    <main class="cont_all">
        <div class="cont_header">
            <div>
                <h1 class="welcome_text">Bem vindo, {{ user.name ? user.name.split(' ')[0] : user}}!</h1>
            </div>
            <div style="display: flex; align-items: center;">
            </div>
            <div class="cont_menu_list_perfil">
                <ul class="menu_list_perfil">
                    <li> <h2>{{ wallet.valuation }}</h2> </li>

                    <li v-if="!user.is_superuser && this.isMobile" class="pi pi-user"  @click="changePage('Perfil')"></li>
                    <li v-if="!user.is_superuser && !this.isMobile"  @click="changePage('Perfil')">Perfil</li>

                    <li v-if="!user.is_superuser && [2,3].includes(orderOpen[0]?.status)" @click="changePage('Pedido')">
                    <!-- <li v-if="!user.is_superuser && [2,3].includes(status_order)" @click="changePage('Pedido')"> -->
                        <p v-if="this.isMobile" class="pi pi-shopping-bag"></p>
                        <p v-else class="p-pedido-aberto">Pedido Aberto</p>
                    </li>
                    <li v-if="user.is_superuser" @click="changePage('Pedidos Abertos')">Pedidos em aberto</li>
                    
                    <li class="pi pi-book" v-if="this.isMobile" @click="changePage('Historico')"></li>
                    <li v-else @click="changePage('Historico')">Histórico</li>
                    
                    <li v-if="this.isMobile" class="pi pi-sign-out" @click="logout"></li>
                    <li v-else @click="logout">Sair</li>
                </ul>
            </div>
        </div>

        <contProduct></contProduct>
    </main>
</template>

// ____________SCRIPT____________
<script>
import contProduct from '../Products/cont_product.vue';
// import perfilUser from '../perfil/perfil.vue'
import { useAuthStore } from '@/stores/auth.js';
import { useRoute, useRouter } from 'vue-router';
import apiAccountService from "../../services/clients/apiClientService"
import apiOrderService from "../../services/order/apiOrderService"
import apiWalletService from "../../services/wallets/apiWalletService"

export default {
    components: { 
        contProduct, 
    },
    data() {
        const authStore = useAuthStore();

        return {
            router: useRouter(),
            // user_id: authStore.user_id, // Refatorar authStore para receber usuario diretamente
            status_order: 0,
            user: authStore.user,
            list: {},
            orderOpen: [],
            wallet: 0,
            isMobile: false,
        };
    },

    methods: {
        async logout(){
            const token = localStorage.getItem('token')
            const refresh_token = localStorage.getItem('refresh_token')

            if(token && refresh_token){ 
                localStorage.removeItem('token')
                localStorage.removeItem('refresh_token')
                
                this.$notify({ type: "success", text: "Obrigado, volte sempre!", duration: 2000});
                return setTimeout(()=>{
                    this.router.push({name: 'home'});
                }, 2000);
            } else {
                this.$notify({ type: "warn", text: "Hum... parece que você ja não esta conosco !", duration: 2000});
                this.router.push({name: 'home'});

            }
        },
        changePage(page){
            this.router.push({name: `${page}`});
        },
        async getWallet(){
            await apiWalletService.getWallet().then(response=>{
                this.wallet = response.data
            })
        },
        async load_data(){
            await apiOrderService.getOrder().then((response)=>{
                this.orderOpen = response.data.filter(order => order.status != 4)
            }).catch((err)=>{
                console.log(err)
            })
        },
        checkScreenSize() {
            this.isMobile = window.innerWidth < 480;
        }
        
    },
    mounted() {
        this.load_data()
        this.getWallet()
        this.checkScreenSize();
        window.addEventListener('resize', this.checkScreenSize);
    },
    beforeDestroy() {
        window.removeEventListener('resize', this.checkScreenSize);
    },
    computed() {},
    
};
</script>

<style scoped>

.cont_header {
    top: 0;
    position: fixed;
    z-index: 2;
    background-color: green;
    color: white;
    width: 100%;
    display: flex;
    justify-content: space-between;
    min-height: 38px;
}

.welcome_text {
    font-size: 0.9rem;
    padding: 0.5rem;
}

.cont_menu_list_perfil {
    display: flex;
}

.menu_list_perfil {
    display: flex;
    flex-direction: row;
    /* margin-right: 1rem; */
    justify-content: space-between;
    /* justify-content: space-around; */
    align-items: center;
    list-style: none;
}

.menu_list_perfil li {
    list-style: none;
    margin-right: 1rem;
    cursor: pointer;
}
.p-pedido-aberto{
    background-color: green;
    color: orange;
    font-weight: bold;
    border-radius: 10px;
    padding: 5px;
}
.table_products {
    width: 100%;
    height: 100%;
}
.pi{
    font-size: 1.3rem;
}
</style>