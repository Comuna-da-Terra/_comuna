<template>
    <main class="cont_all">
        <div class="cont_header">
            <div>
                <h1 class="welcome_text">Bem vindo, {{ user.name ? user.name.split(' ')[0] : user}}!</h1>
            </div>
            <div class="cont-menu"> 
                <ul class="menu-list">
                    <li>
                        <a href="termosdeuso" target="_blank">Termos de Uso</a> 
                    </li>
                    <li>
                        <a href="politicadeprivacidade" target="_blank">Política de Privacidade</a>
                    </li>
                    <li @click="changePage('Histórico de Ordens')">Histórico</li>
                    <li @click="logout">Sair</li>
                </ul>
            </div>
        </div>

        <div class="cont-main">
            <ul>
                <li @click="changePage('Plano de cestas')">
                    <h1> Plano de Cestas</h1>
                    <i class="pi pi-shopping-bag "></i>
                </li>
                <li @click="changePage('Produtos disponíveis')">
                    <h2> Produtos Disponíveis </h2> 
                    <figure>
                        <i class="pi pi-box"></i>
                        <i class="pi pi-angle-double-right"></i>
                    </figure>
                </li>
                <li @click="changePage('Produtos recebidos')">
                    <h2> Produtos Recebidos </h2>
                    <figure>
                        <i class="pi pi-angle-double-left"></i>
                        <i class="pi pi-box"></i>
                    </figure>
                </li>
                <li @click="changePage('Pedidos Abertos')">
                    <h2> Pedidos em Aberto </h2>
                    <i class="pi pi-shopping-bag"></i>
                </li>
                <li @click="changePage('Clientes Registrados')">
                    <h2> Cliente Cadastrados </h2> 
                    <i class="pi pi-user"></i>
                </li>
            </ul>
        </div>
    </main>
</template>

// ____________SCRIPT____________
<script>
// import contProduct from '../products/cont_product.vue';
import { useAuthStore } from '@/stores/auth.js';
import { useRouter } from 'vue-router';
import apiAccountService from "../../services/clients/apiClientService"
import changePassword from '../Perfil/changePassword.vue';
// import apiOrderService from "../../services/order/apiOrderService"

export default {
    components: { 
        // contProduct, 
    },
    data() {
        const authStore = useAuthStore();

        return {
            router: useRouter(),
            user_id: authStore.user_id,
            user: authStore.user,
            list: {},
            orderOpen: [],
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
        async load_data(){
            await apiAccountService.getAccount(this.user_id).then((response)=>{
                this.user = response.data[0]
            })
            // await apiOrderService.getOrder().then((response)=>{
            //     this.orderOpen = response.data
            // }).catch((err)=>{
            //     console.log(err)
            // })
        },
        
    },
    mounted() {
        this.load_data()
    },
    computed() {},
    
};
</script>

<style scoped>

.cont_header {
    top: 0;
    position: fixed;
    z-index: 1;
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

.cont-menu {
    display: flex;
}

.menu-list {
    display: flex;
    flex-direction: row;
    margin-right: 1rem;
    justify-content: space-around;
    align-items: center;
    list-style: none;
}

.menu-list li {
    list-style: none;
    margin-right: 1rem;
}
.cont-main{
    margin-top: 38px;
    height: 100%;
    width: 100%;
}
.cont-main ul{
    padding: 2rem 0.7rem 2rem 0.7rem;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items:center;
    flex-wrap: wrap;
    gap: 1rem;
}
.cont-main ul li{
    background-color: green;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    height: fit-content;
    width: 100%;
    font-size: 95%;
    cursor: pointer;
    border-radius: 10px;
    color: white;
}
.pi{
    font-size: 3rem;
}
i{
    color: white;
}
</style>
