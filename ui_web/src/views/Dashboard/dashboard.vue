<template>
    <main class="cont_all">
        <div class="cont_header">
            <div>
                <h1 class="welcome_text">Bem vindo, {{ user.first_name }} {{ user.last_name}} !</h1>
            </div>
            <div class="cont_menu_list_perfil">
                <ul class="menu_list_perfil">
                    <li>Perfil</li>
                    <li>Pedido</li>
                    <li>Histórico</li>
                    <li @click="logout">Sair</li>
                </ul>
            </div>
        </div>
        


        <div class="cont_body">
            <div class="cont_input_search">
                <input type="search" placeholder="O que você está procurando?">
                <button>Search</button>
            </div>
            <ul class="list-cateogry">
                <li>Frutas</li>
                <li>Verduras</li>
                <li>Legumes</li>
                <li>Sucos/Pol.</li>
                <li>Outros...</li>
            </ul>
        </div>
        <contProduct></contProduct>
    </main>
</template>

// ____________SCRIPT____________
<script>
import contProduct from '../Products/cont_product.vue';
import { useAuthStore } from '@/stores/auth.js';
import { useRoute, useRouter } from 'vue-router';
import apiAccountService from "../../services/clients/clientService"



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
            list: {}
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
        async load_data(){
            await apiAccountService.getAccount(this.user_id).then((response)=>{
                this.user = response.data[0]
            })
        }
    },
    mounted() {
        this.load_data()
    },
    computed() {},
    
};
</script>

<style scoped>

.cont_header {
    /* height: 10vh; */
    width: 100%;
    display: flex;
    justify-content: space-between;
    /* top: 0; */
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

.table_products {
    width: 100%;
    height: 100%;
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
}

.cont_product li {
    list-style: none;
}
</style>
