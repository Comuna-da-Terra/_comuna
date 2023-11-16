<template>
    <main class="cont_all">
        <div class="cont_header">
            <div>
                <h1 class="welcome_text">Bem vindo, {{ user.first_name }} {{ user.last_name}} !</h1>
            </div>
            <div class="cont_menu_list_perfil">
                <ul class="menu_list_perfil">
                    <li v-if="!user.is_superuser" @click="changePage('Perfil')">Perfil</li>
                    <li v-if="!user.is_superuser" @click="changePage('Pedido')">Pedido</li>
                    <li v-if="user.is_superuser" @click="changePage('Pedidos Abertos')">Pedidos em aberto</li>
                    <li @click="changePage('Historico')">Histórico</li>
                    <li @click="logout">Sair</li>
                </ul>
            </div>
        </div>

        <contProduct></contProduct>
    </main>
</template>

// ____________SCRIPT____________
<script>
import contProduct from '../Products/cont_product.vue';
import perfilUser from '../perfil/perfil.vue'
import { useAuthStore } from '@/stores/auth.js';
import { useRoute, useRouter } from 'vue-router';
import apiAccountService from "../../services/clients/apiClientService"
import apiOrderService from "../../services/order/apiOrderService"

export default {
    components: { 
        contProduct, 
    },
    data() {
        const authStore = useAuthStore();

        return {
            router: useRouter(),
            user_id: authStore.user_id,
            user: {},
            list: {},
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
    width: 100%;
    display: flex;
    justify-content: space-between;
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
    margin-right: 1rem;
    justify-content: space-around;
    align-items: center;
    list-style: none;
}

.menu_list_perfil li {
    list-style: none;
    margin-right: 1rem;
}

.table_products {
    width: 100%;
    height: 100%;
}



</style>
