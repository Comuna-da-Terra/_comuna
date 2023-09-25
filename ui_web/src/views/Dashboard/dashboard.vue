<template>
  <div class="all_container">
    <header class="cont_header">
        <div>
            <h1 class="welcome_text" >Bem vindo, Celso Furtado !</h1>
        </div>
        <div class="cont_menu_list_perfil">
            <ul class="menu_list_perfil">
                <li>Perfil</li>
                <li>Pedido</li>
                <li>Histórico</li>
                <li>Sair</li>
            </ul>
        </div>
    </header>

    <div class="cont_body">
        <div class="cont_input_search">
            <input type="search" placeholder="O que você está procurando?">
        </div>
        <table class="table_products">
            <tr class="header_table">
                <th>Frutas</th>
                <th>Verduras</th>
                <th>Legumes</th>
                <th>Sucos/Pol.</th>
                <th>Outros...</th>
            </tr>
            <tr class="table_list">
                <ul class="cont_product"  >
                    <li v-for="(item, index) in list.products" :key=index>
                            <img src="https://encurtador.com.br/pDR78" alt="img_cesta"> 
                    <span>
                        {{item.name}}
                    </span>
                    <span>
                        {{item.quantidade}}
                    </span>
                    <span>
                        {{item.preco}}
                    </span>
                    </li>
                </ul>
            </tr>
        </table>
    </div>
    
    
  </div>
</template>

// ____________SCRIPT____________
<script>
export default {
    data() {
        return {
            list: {
                products:[
                    {
                        name: "Abacate",
                        quantidade: 7,
                        preco: 13.00,
                    },
                    {
                        name: "Abacate",
                        quantidade: 7,
                        preco: 13.00,
                    },
                    {
                        name: "Abacate",
                        quantidade: 7,
                        preco: 13.00,
                    },
                    {
                        name: "Abacate",
                        quantidade: 7,
                        preco: 13.00,
                    },
                    {
                        name: "Abacate",
                        quantidade: 7,
                        preco: 13.00,
                    }
                ]
            }
        }
    },
    methods: {
      
    },
    mounted() {
      
    },
};
</script>

<style scoped>

    .all_container{
        height: 100%;
        width: 100%;
    }
    .cont_header{
        height: 10vh;
        width: 100vw;
        display: flex;
        justify-content: space-between;
        top: 0;
    }
    .welcome_text{
        font-size: 0.9rem;
        padding: 0.5rem;
    }
    .cont_menu_list_perfil{
        display: flex;
    }
    .menu_list_perfil{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
        list-style: none;
    }
    .menu_list_perfil li {
        margin-right: 1rem;
    }
    .cont_body{
        height: 100%;
    }
    .cont_input_search{
        width: 100vw;
        display: flex;
        justify-content: center;
    }    
    .cont_input_search input{
        height: 3rem;
        width: 80%;
        font-size: 1rem;
        border-radius: 7px;
        padding: 1rem;
    }
    .table_products{
        width: 100%;
        height: 100%;
    }
    .header_table{
        display: flex;
        justify-content: space-around;
        width: 100%;
    }
    .header_table th{
        cursor: pointer;
    }
    .table_list{
        display: flex;
        justify-content: space-around ;
        height: 100%;
        width: 100%;
    }
    .table_list ul{
        padding: 15px;
    }
    .cont_product{
        width: 100%;
        display: flex;
    }
    .cont_product img{
        width: 90%;
        padding: 0.1rem;
    }

</style>
