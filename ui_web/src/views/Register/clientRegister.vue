<template>
  <main class="cont_all">
    <form class="form" action="" @submit.prevent="handleSubmit">
       <div class="cont_input_form">
        <label for="first_name">Nome: </label>
      <input v-model="formData.first_name" type="text" id="first_name" name="first_name" placeholder="Nome">
      </div>
      
       <div class="cont_input_form">
        <label for="last_name">Sobrenome:</label>
        <input v-model="formData.last_name" type="text" id="last_name" name="last_name" placeholder="Sobrenome">
      </div>
      
       <div class="cont_input_form">
        <label for="email">E-mail:</label>
        <input v-model="formData.email" type="text" id="email" name="email" placeholder="E-mail">
      </div>

       <div class="cont_input_form">
        <label for="birth_date">Data de Nascimento:</label>
        <input v-model="formData.birth_date" type="text" id="birth_date" name="birth_date" placeholder="Data de Nascimento">
      </div>
      
       <div class="cont_input_form">
        <label for="cellphone">Telefone Celular:</label>
        <input v-model="formData.cellphone" type="text" id="cellphone" name="cellphone" placeholder="WhatsApp">
      </div>

       <div class="cont_input_form">
        <label for="password">Senha:</label>
        <input v-model="formData.password" type="password" id="password" name="password" placeholder="Senha">
      </div>

      <div class="cont_btn_register">
        <button type="submit" class="btn_register"> Cadastrar </button>
      </div>

      
      <span class="link_register">
        <RouterLink to="login"> Já tenho cadastro  </RouterLink>
      </span>
    </form>
  </main>
</template>

// ____________SCRIPT____________
<script>
import apiAccount from '@/services/clients/clientService'; // Certifique-se de ajustar o caminho correto
import { useRoute, useRouter } from 'vue-router';

export default {
    data() {
        return {
          router: useRouter(),
          formData: {}
        }
    },
    methods: {
      handleSubmit() {
        // event.preventDefault();
        console.log(this.formData)
        apiAccount.registerAccount(this.formData).then((response)=>{
          console.log(response)
          this.$notify({ type: "success", text: "Pronto, estou te enviando para o acesso!", duration: 2000});
          setTimeout(()=>{
            this.router.push({name: 'login'});
          }, 2000);
        }).catch(()=>{
          this.$notify({ type: "warn", text: "Hum.. tem algo de errado com os dados!", duration: 2000});

        })
      } 
      
    },
    mounted() {
      
    },
};
</script>

<style>
  .form {
        /* height: 100%; */
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        padding: 1rem;

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
    .cont_btn_register{
      display: flex;
      justify-content: center;
    }
    .cont_btn_register button{
      margin-top: 1rem;
      cursor: pointer;
      height: 2.5rem;
      width: 100%;
      background-color: green;
      border: none;
      border-radius: 3px;
      opacity: 0.4;
    }
    .cont_btn_register button:hover{
      opacity: 1;

    }
    .link_register {
        text-align: center;
        font-size: 1.3rem;
    }

</style>
