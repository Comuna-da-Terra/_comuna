<template>
    <div class="cont-form-plan">
        <header class="header-title">
            <h1>Plano de Cesta</h1>
            <i class="pi pi-times" @click="closeModal"></i>
        </header>
        <form @submit.prevent="handleSubmit">
            <label for="name">Período</label>
            <select v-model="basketPlan.type" required>
                <option value="S">Semanal</option>
                <option value="Q">Quinzenal</option>
            </select> 
            <label for="age">Tamanho da cesta</label>
            
            <select v-model="basketPlan.basket_type" required>
                <option value="M">Média</option>
                <option value="G">Grande</option>
            </select> 
            
            <button v-if="!this.plan" class="btn-create" type="submit">Assinar</button>
            <div v-else style="display: flex">
                <button v-if="!this.basketPlan.is_active" class="btn-edit disabled" type="button" >Alterar Plano</button>
                <button v-else class="btn-edit" type="button" @click="editBasketPlan()" >Alterar Plano</button>
                
                <button v-if="!this.basketPlan.is_active" class="btn-enable" type="button" @click="disableBasketPlan(true)">Ativar  Plano</button>
                <button v-else class="btn-disable" type="button" @click="disableBasketPlan(false)">Desativar  Plano</button>
            </div>
        </form>
    </div>
</template>

<script>
import apiBasketPlanService from "../../services/basketPlan/apiBasketPlanService"

export default {
    components:{},
    data(){
        return {
            contact: {},
            basketPlan: {},
            plan: false
        };
    },
    emits: ['close-modal'],
    methods:{
        async handleSubmit(){
            await apiBasketPlanService.createBasketPlan(this.basketPlan).then((response)=>{
                this.$notify({ type: "success", text: `Plano ${response.type == "S" ? "Semanal":"Quinzenal"} assinado!`, duration: 2000});
                console.log(response)
                this.closeModal()
                return response
            })
        },
        async editBasketPlan(){
        
            await apiBasketPlanService.editBasketPlan(this.basketPlan).then((response)=>{
                this.$notify({ type: "success", text: "Plano Alterado!", duration: 3000});
                this.closeModal()
                return response
            })
        },
        async disableBasketPlan(is_active){
            const data = {
                id: this.basketPlan.id,
                is_active: is_active
            }

            await apiBasketPlanService.editBasketPlan(data).then((response)=>{
                this.$notify({ type: "success", text: `Plano ${response.is_active == true ? "Ativado":"Desativado"}!`, duration: 3000});
                console.log(response)
                this.closeModal()
                return response
            })
        },
        async load_data(){
            await apiBasketPlanService.getBasketPlan().then((response)=>{
                this.basketPlan = response
                this.basketPlan.type == null ? "" : this.plan = true

            })

        },
        closeModal() {
            this.$emit('close-modal')
            return false;
        },
    },
    async mounted() {
    this.load_data()
   }
}
</script>

<style scoped>
.cont-form-plan{
    width: 300px;
    display: flex;
    align-items: center;
    background-color: white;
    padding: 1rem;
    border-radius: 8px;
    flex-direction: column;
    height: fit-content;
    color: black;
    box-shadow: 0 0px 1rem #000000;
}
form{
    display: flex;
    flex-direction: column;
    width: 70%;
    align-items: center;
}
form label{
    width: 100%;
    text-align: start;
}
select{
    height: 2rem;
    width: 100%;
}
.header-title{
    width: 100%;
    display: flex;
    justify-content: space-around;
    align-items: center;
}
button{
    border: none;
    border-radius: 7px;
    cursor: pointer;
    width: 100%;
    height: 2.3rem;
    margin-top: 1rem;
    color: white;
    font-size: 0.9rem;
}
.btn-create{
    background-color: green;
    
}
.btn-edit{
    border-radius:  7px 0px 0px 7px;
    background-color: blue;
    
}
.disabled{
    background-color: grey;
    opacity: 0.5;
    cursor: not-allowed;
}
.btn-disable{
    border-radius:  0px 7px 7px 0px;
    background-color: red;
}
.btn-enable{
    border-radius:  0px 7px 7px 0px;
    background-color: green;
}
.pi-times{
    color: black;
}
</style>
