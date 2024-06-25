<template>
    <div class="in-development">Em desenvolvimento...</div>
    <main class="cont_all">
        <div class="cont-header">
            <button type="button" class="btn-submit">
            <i class="pi pi-times" @click="this.router.push({name: 'admin'});"></i>
            </button>
            <h1>
                Histórico de Ordens
            </h1>
            <button class="btn-submit" type="submit">
            <i class="pi pi-check" type="submit" ></i>
            </button>
        </div>

        <!-- <div style="width: 100%;">
            <ul class="ul-client" style="width: 100%;">
                <li class="li-client li-head">
                    <p>Atividade</p>
                    <p>Nome</p>
                    <p>Telefone</p>
                    <p>E-mail</p>
                    <p>Data de Nascimento</p>
                </li>
                <li class="li-client" v-for="(client, index) in clients" :key="index">
                    <div v-if="client.is_active" style="background-color: green;" class="is-active"></div>
                    <div v-else style="background-color: red;" class="is-active"></div>
                    <p>{{ client.name.split(' ')[0] }} {{ client.name.split(" ").length > 1 ? client.name.split(' ').pop() : ""}}</p>
                    <p>{{ client.cellphone }}</p>
                    <p>{{ client.email }}</p>
                    <p>{{ dateString( new Date(client.birth_date)) }}</p>
                </li>
            </ul>
        </div> -->
        
    </main>
  </template>
  
  // ____________SCRIPT____________
  <script>
  import apiAccountService from '@/services/clients/apiClientService';
  import { useRoute, useRouter } from 'vue-router';
  
  export default {
      data() {
          return {
            router: useRouter(),
            clients: [],
          }
      },
      methods: {
        handleSubmit() {},
        async load_data(){
            await apiAccountService.getAccounts().then((response) => {
                this.clients = response.data
            console.log(this.clients)})
        },
        dateString(date){
            return date.toLocaleDateString('pt-BR', {day: '2-digit', month: '2-digit', year: '2-digit'})},
      },
      mounted() {
        this.load_data()
      },
  };
  </script>
  
  <style >
  .in-development{
    width: 100%;
    height: 2rem;
    text-align: center;
    background-color: orange;
    font-size: x-large;
    position: absolute;
    top:0
  }
    .cont_all{
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
    .btn-submit{
        border: none;
        background-color: transparent;
    }
    .pi{
        color: white;
    }
    .li-head p{
        font-weight: bold;
        align-items: center;
        margin: 0.5rem 0;
    }
    .li-client{
        display: grid;
        align-items: center;
        justify-content: space-between;
        grid-template-columns: 10% 20% 20% 20% 20%;
        border: solid 1px;
        border-radius: 5px;
        margin: 0.5rem 0;
        padding: 5px;

    }
    .li-client > *:first-child {
        justify-self: center;
    }
    .li-client > *:last-child {
        justify-self: center;
    }
    .li-client p{
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
  