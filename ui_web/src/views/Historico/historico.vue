<template>
    <main class="cont_all">
        Em desenvolvimento...
        <button @click="this.router.push({name: 'dashboard'});">Voltar</button>
        
    </main>
  </template>
  
  // ____________SCRIPT____________
  <script>
  import apiAccount from '@/services/clients/apiClientService'; // Certifique-se de ajustar o caminho correto
  import { useRoute, useRouter } from 'vue-router';
  
  export default {
      data() {
          return {
            router: useRouter(),
            formData: {},
            user: {},
          }
      },
      methods: {
        handleSubmit() {},
        async load_data(){
            await apiAccountService.getAccount(this.user_id).then((response)=>{
                this.user = response.data[0]
            })
        }
        
      },
      mounted() {},
  };
  </script>
  
  <style>
  
  </style>
  