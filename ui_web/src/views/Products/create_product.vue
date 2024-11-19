<template>
    <div class="cont-form-product">
        <header class="header-title">
            <h1>Novo Produto</h1>
            <i class="pi pi-times" @click="$emit('close-modal', false)"></i>
        </header>
        <form v-if="modalCreateCategory === false" class="form-product" @submit.prevent="handleSubmit">
            <label for="name">Nome</label>
            <input v-model="product.name" type="text" name="name">

            <div class="cont-data-image">
                <div class="lab-preco">
                    <label for="preco">Preço
                        <input v-model="product.price" style="width: 100px;" type="number" name="preco">
                    </label>
                </div>
                <div class="lab-quantidade">
                    <label for="quantidade">Quantidade
                        <input v-model="product.likely_stock" style="width: 100px;" type="number" name="quantidade">
                    </label>
                </div>
                <div class="lab-tipo">
                    <label for="tipo">Tipo
                        <input v-model="product.type" style="width: 100px;" type="text" name="tipo">
                    </label>
                </div>
                
                <label for="imagem" class="lab-image" >    
                    <img class="viewImage" :src=imgProduct alt="Imagem do produto" v-if="imgProduct">
                    <img src="https://encurtador.com.br/pDR78" alt="img-plus.svg" class="icon-img-plus" v-if="!imgProduct">
                    <input type="file" accept="image/*" id="imagem" name="imagem" @change="whenIncludeImage">
                </label>
            </div>
            
            <label for="categoria">Categoria</label>
            <div class="cont-inp-category">
                <select name="categoria" type="text" v-model=product.category placeholder="Categoria...">
                    <option v-for="option in categories" :value="option.id">
                        {{ option.name }}
                    </option>
                </select>
                <button @click.prevent="changeToModalCreateCategory()"> New </button>  
            </div>
            <div class="cont-btn">
                <button class="btn-cancelar" @click="$emit('close-modal', false)">Cancelar</button>
                <button class="btn-enviar" type="submit">Enviar</button>
            </div>
        </form>
        <div v-if="modalCreateCategory" class="modal-create">
            <formCreateCategory @close-modal="closeModal"></formCreateCategory>
        </div>
    </div>
</template>

<script>
import apiCategoryService from '../../services/category/apiCategoryService';
import apiProductService from "../../services/products/apiProductService"
import formCreateCategory from '../Category/create_category.vue'

export default {
    components:{
        formCreateCategory
    },
    data(){
        return {
            imgProduct: null,
            categories: [],
            product: {},
            modalCreateCategory: false
        };
    },
    emits: ['close-modal'],
    methods:{
        async load_data(){
            await apiCategoryService.getListCategory().then((response)=>{
                this.categories = response.data
                console.log(this.categories)
             })
        },
        async handleSubmit(){
            await apiProductService.createProduct(this.product).then((response)=>{
                this.$emit(this.closeModal, false)
            })
        },
        async whenIncludeImage(event){
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = () => {
                    this.imgProduct = reader.result;
                };
                reader.readAsDataURL(file)
            }
        },
        changeToModalCreateCategory(){
            this.modalCreateCategory = true
        },
        closeModal(){
            this.modalCreateCategory = false
            this.load_data()    
        }
    },
    async mounted(){
        this.load_data()    
    }
}
</script>

<style>
.cont-form-product{
    width: 300px;
    display: flex;
    /* justify-content: center; */
    align-items: center;
    background-color: white;
    padding: 1rem;
    border-radius: 8px;
    flex-direction: column;
    height: fit-content;
    color: green;
    box-shadow: 0 0px 1rem #000000;
}
.header-title{
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
}
.form-product{
    display: flex;
    flex-direction: column;
}
.lab-preco{ grid-area: item-preco;}
.lab-quantidade{ grid-area: item-quantidade;}
.lab-tipo{ grid-area: item-tipo;}
.lab-image{
    grid-area: item-img;
    display: flex;
    justify-content: center;
    background-color: white;
    width: 160px;
    height: 160px;
    border-radius: 6px;
    box-shadow: 0 0 5px #000000;
}
.cont-data-image{
    display: grid;
    grid-template-areas: 
        'item-preco item-img'
        'item-quantidade item-img'
        'item-tipo item-img';
    gap: 10px;
    padding: 10px 0px;
    justify-content: space-between;
    align-items: end;
    
}
input, select{
    /* border: none; */
    border-radius: 7px;
    max-width: 270px;
    max-height: 110px;
    border: none;
}
input, select{
    height: 30px;
}

label input[type="file"]{
    display: none;
}
.icon-img-plus{
    width: 100%;
}
.viewImage{
    width: 100%;
    height: 100%;
    border: solid 1px white;
    border-radius: 6px;

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
.cont-btn{
    width: 100%;
    display: flex;
    justify-content: space-around;
    padding: 1rem 0rem;
}
.cont-btn button{
    color: white;
    font-weight: bolder;
    height: 2rem;
    border: none;
    border-radius: 5px;
    box-shadow: 0 1px 3px #000000;
}
.cont-btn button:hover{
    box-shadow: 0 2px 4px #000000;
}
.cont-btn button:active{
    box-shadow: inset 0 1px 3px rgba(0, 0, 0, 1);   
}
.btn-cancelar{
    background-color: red;
}
.btn-enviar{
    background-color: green;
}
</style>
