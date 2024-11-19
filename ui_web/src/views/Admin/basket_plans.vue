<template>
    <main class="cont-all">
        <div class="cont-header">
            <button type="button" class="btn-submit">
            <i class="pi pi-times" @click="this.router.push({name: 'admin'});"></i>
            </button>
            <h1>
                Planos de cesta
            </h1>
            <button class="btn-submit" type="submit">
            <i class="pi pi-check" type="submit" ></i>
            </button>
        </div>
        <div class="cont-filter-plans">
            <label for="semanal">Semanal
                <input name="semanal" type="checkbox" v-model="this.filter_week">
            </label>

            <label for="quinzenal">Quinzenal
                <input name="quinzenal" type="checkbox" v-model="this.filter_twoweek">
            </label>

            <label for="medio">Cesta Média
                <input name="medio" type="checkbox" v-model="this.filter_medio">
            </label>

            <label for="grande">Grande
                <input name="grande" type="checkbox" v-model="this.filter_big">
            </label>
            <button @click="filterPlans()">Filtrar</button>
        </div>
        <div style="display: flex; justify-content: space-around; width: 100%;">
            <h3>Planos semanais {{ this.amout_week }}</h3>
            <h3>Planos quinzenais {{ this.amout_twoweek }}</h3>
            <h3>Cestas Médias {{ this.amout_basket_medio }}</h3>
            <h3>Cestas Grandes {{ this.amout_basket_big }}</h3>
        </div>
        <!-- <h1 style="cursor: pointer;" @click="getBasketDelivery()">Montar Entregas</h1> -->

        <div style="width: 100%;">
            <ul style="width: 100%;">
                <li class="li-plan li-head">
                    <p>Ativo</p>
                    <p>Período</p>
                    <p>Tamanho</p>
                    <p>Cliente</p>
                </li>
                <li class="li-plan" v-for="(plan, index) in show_plans" :key="index">
                    <div v-if="plan.is_active" style="background-color: green;" class="is-active"></div>
                    <div v-else style="background-color: red;" class="is-active"></div>
                    <p>{{ plan.type == "S" ? "Semanal" : "Quinzenal"}}</p>
                    <p>{{ plan.basket_type == "M" ? "Médio" : "Grande" }}</p>
                    <p>{{ plan.user_name}}</p>
                </li>
            </ul>
        </div>
        
       </main>
</template>
  
// ____________SCRIPT____________
<script>
  
import apiBasketPlanService from "../../services/basketPlan/apiBasketPlanService"
import apiAccountService from '@/services/clients/apiClientService';
import { useRoute, useRouter } from 'vue-router';


export default {
    data() {
        return {
        router: useRouter(),
        clients: [],
        basketPlans: [],
        show_plans: [],
        filter_week: false,
        amout_week: 0,
        amout_twoweek: 0,
        amout_basket_medio: 0,
        amout_basket_big: 0,
        filter_twoweek: false,
        filter_medio: false,
        filter_big: false,
        }
    },
    methods: {
        async load_data(){
            await apiAccountService.getAccounts().then((response) => {
                this.clients = response.data
            })
            await apiBasketPlanService.getAllBasketPlans().then(response => {
                this.basketPlans = response
                this.basketPlans.map((plan)=>{
                    this.clients.find((client)=>{
                        client.id === plan.user 
                            ? plan.user_name = client.name
                            : ""
                    })
                    plan.type == "S" ? this.amout_week += 1 : this.amout_twoweek += 1 
                    plan.basket_type == "M" ? this.amout_basket_medio += 1 : this.amout_basket_big += 1 


                })
                this.show_plans = this.basketPlans
            })

        },
        async getBasketDelivery(){
            console.log("CALL")
            await apiBasketPlanService.getDeliveryBasket((response)=>{
                console.log(response)
            })
        },
        filterPlans(type_filter){
            this.show_plans = this.basketPlans
            this.filter_week ? this.show_plans = this.show_plans.filter((p)=>p.type === "S") : ""
            this.filter_twoweek ? this.show_plans = this.show_plans.filter((p)=>p.type === "Q") : ""
            this.filter_medio ? this.show_plans = this.show_plans.filter((p)=>p.basket_type === "M") : ""
            this.filter_big ? this.show_plans = this.show_plans.filter((p)=>p.basket_type === "G") : ""

        }

    },
    async mounted() {
        this.load_data()
    },
};
</script>

<style scoped>
.cont-all{
    height: 100%;
    display: flex;
    justify-content: flex-start;
}
.cont-header{
    background-color: green;
    justify-content: space-around;
    display: flex;
    width: 95%;
    height: 80px;
    align-items: center;
    font-size: x-large;
    color: white;
    margin: 0rem 1rem 1rem 1rem;
    border-radius: 7px;
}
.cont-filter-plans{
    display: flex;
    width: 100%;
    justify-content: space-around;
}
.pi{
    color: white;
}
.li-head p{
    font-weight: bold;
    align-items: center;
    margin: 0.5rem 0;
}
.li-plan{
    display: grid;
    align-items: center;
    justify-content: space-between;
    grid-template-columns: 10% 25% 25% 25%;
    border: solid 1px;
    border-radius: 5px;
    margin: 0.5rem;
    padding: 5px;

}
.li-plan > *:first-child {
    justify-self: center;
}
.li-plan > *:last-child {
    justify-self: center;
}
.li-plan > *:nth-child(3)  {
    justify-self: center;
}
.li-plan p{
    text-align: start;
}
.is-active{
    background-color: pink;
    border-radius: 50%;
    width: 10px;
    height: 10px;
    box-shadow: 0px 0px 3px;
    align-items: center;
    display: flex;
}

</style>
