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
      </div>

      <div class="cont_btn_login">
        <!-- <RouterLink style="width: 100%" to="/dashboard"> -->
          <button type="submit" class="btn_login"> Login </button> 
        <!-- </RouterLink> -->
      </div>

      
      <span class="link_login">
        <RouterLink to="register"> Quero participar!  </RouterLink>
      </span>
    </form>
  </main>
</template>

// ____________SCRIPT____________
<script>
import serviceAuth from '@/services/clients/authService';
import { useRoute, useRouter } from 'vue-router';


export default {
    data() {
        return {
          router: useRouter(),
          formData: {
              email: '',
              password: ''
            }
        }
    },
    methods: {
      async handleSubmit() {
        await serviceAuth.login(this.formData).then(resp=>{
          this.$notify({ type: "success", text: "Wow, Seja bem vindo !", duration: 2000});
          setTimeout(()=>{
            this.router.push({name: 'dashboard'});
          }, 2000);
          
        }).catch((err)=>{
          this.$notify({ type: "warn", text: "Hum... algo errado com seu E-mail ou senha !", duration: 3000 , position: "bottom right"});
        })
      }
      
    },
    mounted() {
      
    },
};
</script>

<style scoped>
     .form {
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        justify-content: center;
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
      background-color: green;
      border: none;
      border-radius: 3px;
      opacity: 0.4;
    }
    .cont_btn_login button:hover{
      opacity: 0.8;

    }
    .link_login {
        text-align: center;
        font-size: 1.3rem;
    }
</style>