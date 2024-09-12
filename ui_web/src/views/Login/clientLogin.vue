<template>
  <main class="cont_all">
    <form class="form" @submit.prevent="handleSubmit">
  
       <div class="cont_input_form">
        <label for="email">E-mail:</label>
        <input v-model="formData.email" type="text" name="email" placeholder="E-mail" autocomplete="email">
      </div>

       <div class="cont_input_form">
        <label for="senha">Senha:</label>
        <input v-model="formData.password" type="password" name="senha" placeholder="Senha" autocomplete="current-password">
        <span class="sp-forgot-passowrd">
          <a href="http://api.comunadaterra.com.br/api/account/reset_password/"> Esqueci minha senha... </a>
        </span>
      </div>

      <div class="cont_btn_login">

        <button type="submit" class="btn_login"> Login </button> 

      </div>

      
      <span @click="goRegisterPage" class="link_login">
         Quero participar! 
      </span>
    </form>
  </main>
</template>

// ____________SCRIPT____________
<script>
import serviceAuth from '@/services/clients/apiAuthService';
import { useRoute, useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth.js';

export default {
    data() {
      // const authStore = useAuthStore();
        return {
          router: useRouter(),
          formData: {
            email: '',
            password: ''
          },
          is_superuser: null
        }
    },
    methods: {
      async handleSubmit() {
        await serviceAuth.login(this.formData).then(resp=>{
          const authStore = useAuthStore()
          this.$notify({ type: "success", text: "Wow, Seja bem vindo !", duration: 2000});
          setTimeout(()=>{
            this.is_superuser = authStore.user.is_superuser
            this.is_superuser ? 
            this.router.push({name: 'admin'})
            :
            this.router.push({name: 'dashboard'});
          }, 2000);
          
        }).catch((err)=>{
          this.$notify({ type: "warn", text: "Hum... algo errado com seu E-mail ou senha !", duration: 3000});
        })
      },
      goRegisterPage(){
        this.$emit('change-page', 'register')
      }
      
    },
    mounted() {},
};
</script>

<style scoped>
  .cont_all{
    display: flex;
    justify-content: center;
  }
  .form {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        justify-content: center;
    }
    .form input{
      background-color: grey;
      opacity: 0.5;
      border-radius: 8px;
      border: none;
    }
    ::placeholder {
      color: white;
      opacity: 1;
    }
    .form label{
      font-size: 1.1rem;
      color: rgb(16, 16, 16);
      font-weight: bold;
      text-decoration: none;
    }
    .cont_input_form{
      display: flex;
      flex-direction: column;
      justify-content: center;

    }
    .cont_input_form input{
      height: 3rem;
      font-size: 1.0rem;
      padding: 0.5rem;
    }
    .cont_btn_login{
      display: flex;
      justify-content: center;
    }
    .cont_btn_login button{
      margin-top: 1rem;
      cursor: pointer;
      height: 2.5rem;
      width: 100%;
      background-color: rgb(69, 167, 69);
      border: none;
      border-radius: 3px;
      font-weight: bold;
      font-size: 1.2rem;
      
      opacity: 0.8;
    }
    .cont_btn_login button:hover{
      opacity: 1;

    }
    .link_login {
      text-align: center;
      font-size: 1.3rem;
      color: rgb(95, 11, 11);
    }
    .sp-forgot-passowrd{
      font-size: 0.8rem;
      cursor: pointer;
      width: fit-content;
    }
    .sp-forgot-passowrd:hover{
      text-decoration: underline;
    }
</style>
