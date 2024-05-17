<template>
    <div class="cont-form-category">
        <header class="header-title">
            <h1>Nova Categoria</h1>
            <i class="pi pi-times" @click="$emit('close-modal', false)"></i>
        </header>
        <form class="form-category" @submit.prevent="handleSubmit">
            <label for="name">Nome</label>
            <input type="text" name="name" v-model="category.name">

            <label for="descricao">Descrição</label>
            <textarea name="descricao" v-model="category.descricao" id="" cols="30" rows="7"></textarea>

            <div class="cont-btn">
                <button class="btn-cancelar" @click.prevent="$emit('close-modal', false)"> Cancelar </button>
                <button class="btn-enviar" type="submit" > Enviar </button>
            </div>
        </form>
    </div>
</template>

<script>
import apiCategoryService from '../../services/category/apiCategoryService';

export default {
    data(){
        return {
            category: {}
        };
    },
    emits: ['close-modal'],
    methods:{
        async handleSubmit(){
            await apiCategoryService.createCategory(this.category).then((response)=>{
                this.$emit('close-modal', false)
                console.log(Response)
            })
        },
    },
    async mounted(){
        // this.load_data()    
    }
}
</script>

<style>
.cont-form-category{
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
.form-category{
    display: flex;
    flex-direction: column;
}
input, textarea{
    /* border: none; */
    border-radius: 7px;
    max-width: 270px;
    max-height: 110px;
    border: none;
}
input{
    height: 30px;
}

input[type="file"]{
    display: none;
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