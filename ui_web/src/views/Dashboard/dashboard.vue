<template>
    <main class="all_container">
        <div class="cont_header">
            <div>
                <h1 class="welcome_text">Bem vindo, Celso Furtado !</h1>
            </div>
            <div class="cont_menu_list_perfil">
                <ul class="menu_list_perfil">
                    <li>Perfil</li>
                    <li>Pedido</li>
                    <li>Histórico</li>
                    <li>Sair</li>
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
            <contProduct :products="list.products"></contProduct>
        </div>
    </main>
</template>

// ____________SCRIPT____________
<script>
import contProduct from '../../components/cont_product.vue';


export default {
    data() {
        return {
            list: {
                
            }
        };
    },

    methods: {

        load_data(){
            console.log("heloo")
           
        }
    },
    mounted() {
        this.load_data()
    },
    computed() {
    },
    components: { 
        contProduct, 
    }
};
</script>

<style scoped>
.all_container {
    justify-content: space-between;
}

.cont_header {
    /* height: 10vh; */
    width: 100vw;
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

.cont_input_search {
    width: 100vw;
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

.table_list {
    display: flex;
    justify-content: space-around;
    height: 100%;
    width: 100%;
}

.table_list ul {
    padding: 15px;
    gap: 1rem;
}

.cont_product {
    width: 100%;
    display: flex;
}

.cont_product li {
    list-style: none;
}
</style>
