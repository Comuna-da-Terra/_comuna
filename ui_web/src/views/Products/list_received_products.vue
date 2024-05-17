<template>
    <div class="cont_all">

        
        <!-- <div style="display: flex; flex-direction: column; justify-content: space-between;"> -->
            <header class="cont-header">
                <div class="cont-title">
                    <h1 style="color: green;" v-if="likelyProducts.length == 0">Sem produtos cadastrados!</h1>
                    <h1 style="color: green;" >Produtos cadastrados</h1>
                    <button v-if="user.is_superuser" @click="requestCSV">Planilha</button>
                </div>
                <div class="cont_search">
                    <input v-model="searchValue" type="search" placeholder="O que você está procurando?">
                    <button @click="searchProduct()">Search</button>
                </div>

            </header>
            <ul class="list-products">
                <li>
                    <p>Categoria</p>
                    <p>Nome</p>
                    <p>Preço</p>
                    <p>Quant.</p>
                    <button style="background-color: green;" @click="this.modalCreateProduct = true">
                        <i class="pi pi-plus">
                            <!-- Adicionar produto -->
                        </i>
                    </button>
                </li>
                <li class="li-product" v-for="(product, index) in likelyProductsShow" :key="index">
                    <div class="cont-inp-category">
                        <select name="categoria" v-model=product.category>
                            <option disabled selected value=""> Selecione uma Categoria</option>
                            <option v-for="option in categories" :value="option.id">
                                {{ option.name }}
                            </option>
                        </select>
                        <button @click.prevent="modalCreateCategory = true"> <i class="pi pi-plus"></i> </button>  
                    </div>
                    <input class="imp-name-prod" type="text" v-model=product.name>   
                    <input type="text" v-model=product.price>   
                    <input type="number" v-model=product.likely_stock>
                    <button @click="editProd(product)" > <i class="pi pi-pencil"></i></button>
                </li>
            </ul>
        <!-- </div> -->
        <div class="cont-buttons-footer">
            <button @click="this.router.push({ name: 'admin' });">
                <i class="pi pi-arrow-left">
                    <!-- Sair da lista de Produtos Disponíveis -->

                </i>
            </button>
            <button style="background-color: green;" @click="this.modalCreateProduct = true">
                <i class="pi pi-plus">
                    <!-- Adicionar produto -->
                </i>
            </button>
        </div>
        <div v-if="modalCreateProduct" class="modal-create">
            <formCreateProduct @close-modal="closeModal"></formCreateProduct>
        </div>
        <div v-if="modalCreateCategory" class="modal-create">
            <formCreateCategory @close-modal="closeModal"></formCreateCategory>
        </div>
    </div>
</template>
  
  // ____________SCRIPT____________
<script>
import apiAccountService from '@/services/clients/apiClientService';
import apiProductService from "../../services/products/apiProductService"
import apiCategoryService from '../../services/category/apiCategoryService';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';
import formCreateProduct from './create_product.vue';
import formCreateCategory from '../Category/create_category.vue'

export default {
    components: {
        formCreateProduct,
        formCreateCategory
    },
    data() {
        const authStore = useAuthStore();
        return {
            router: useRouter(),
            user: {},
            user_id: authStore.user_id,
            likelyProducts: [],
            likelyProductsShow: [],
            searchValue: '',
            modalCreateProduct: false,
            modalCreateCategory: false,
            categories: []
        }
    },
    methods: {
        async load_data() {
            await apiAccountService.getAccount(this.user_id).then((response) => {
                this.user = response.data[0]
            })
            
            await apiProductService.getAllProducts().then((response)=>{
                this.likelyProducts = response.data.results 
                this.likelyProductsShow = this.likelyProducts
            })
             await apiCategoryService.getListCategory().then((response)=>{
                this.categories = response.data
                console.log(this.categories)
             })
            
            
        },
        async searchProduct(){                        
                        for (let index = 0; index < this.likelyProducts.length; index++) {
                            if(this.normalizeStrings(this.likelyProducts[index].name).includes(this.normalizeStrings(this.searchValue))){
                                return this.likelyProductsShow = this.likelyProducts.filter((product) => this.normalizeStrings(product.name).includes(this.normalizeStrings(this.searchValue))) 
                            } 
                        }
                        return this.$notify({ type: "error", text: "Hum... Não temos nada sobre isso!", duration: 2000});
        },
        async editProd(data){
            console.log(data)
            await apiProductService.editProduct(data)
            this.load_data()
        },
        async closeModal(){
            this.modalCreateProduct = false
            this.modalCreateCategory = false
            await this.load_data()
        },
        normalizeStrings(string){
            return string.normalize('NFD').replace(/[\u0300-\u036f]/g, "").toLowerCase()
        },
        async requestCSV(){},
    },
    async mounted() {
        await this.load_data()
    },
};
</script>
  
  <style >
.cont_all{
    height: 100%;
    width: 100%;
    margin: 3%;
    display: flex;
    flex-direction: column;
    /* justify-content: space-between; */
}
.cont-header{
    display: flex;
    flex-direction: column;
}
.cont-title{
    display: flex;
    justify-content: space-evenly;
}
.list-products{
    height: 100%;
    padding-bottom: 60px;
    height: fit-content;
}
.list-products li {
    padding: 0.5rem;
    margin: 0.5rem;
    border-radius: 3px;
    width: 100%;
    display: inline-grid;
    grid-template-columns:  15% 20% 10% 10% 10%;
    justify-content: space-around;
    list-style: none;
}
.cont-inp-category{
    width: 100%;
    display: grid;
    grid-template-columns: 80% 20%;
}
.cont-inp-category select{
    width: 100%;
    border-radius:  7px 0px 0px 7px;
}
.cont-inp-category button{
    border-radius:  0px 7px 7px 0px;
}
.imp-name-prod{
    /* overflow: hidden; */
    /* width: 20vw; */
    text-overflow: ellipsis;
}
.cont_search {
    width: 100%;
    display: flex;
    justify-content: center;
    margin: 10px 0px;
}
.cont_search input {
    height: 3rem;
    width: 100%;
    font-size: 1rem;
    border-radius: 7px 0px 0px 7px;
    padding: 1rem;
}
.cont_search button {
    cursor: pointer;
    border-radius: 0px 7px 7px 0px;
    border: none;
    box-shadow: 0 0.5px 3px rgba(0, 0, 0, 0.5);
    
}
.cont_search button:active {
    box-shadow: inset 0 0.5px 3px rgba(0, 0, 0, 0.5);
}
.cont-buttons-footer{
    position: fixed;
    width: 100%;
    bottom: 0.5rem;
    display: inline-grid;
    grid-template-columns: 40% 40%;
    justify-content: space-around;
}
.cont-buttons-footer button{
    border: none;
    border-radius: 8px;
    height: 7vh;


}
.modal-create{
    width: 100%;
    height: 100%;
    position: fixed;
    display: flex;  
    justify-content: center;
    align-items: center;
    z-index: 1;
    background-color: transparent;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}
</style>
  