<template>
  <main class="cont_all">
    <form class="form" action="" @submit.prevent="handleSubmit">
       <div class="cont_input_form">
        <label for="name">Nome: </label>
      <input v-model="formData.name" type="text" id="name" name="name" placeholder="Nome">
      </div>
      
       <div class="cont_input_form">
        <label for="email">E-mail:</label>
        <input v-model="formData.email" type="text" id="email" name="email" placeholder="E-mail">
      </div>
      
      <div class="cont_input_form">
        <label for="email">CPF:</label>
        <input v-model="cpf" @input="maskCpf" type="text" id="cpf" name="cpf" placeholder="000.000.000-00">
      </div>

       <div class="cont_input_form">
        <label for="birth_date">Data de Nascimento:</label>
        <input v-model="birthDate" @input="maskBirthDate" type="text" id="birth_date" name="birth_date" placeholder="Data de Nascimento">
      </div>
      
       <div class="cont_input_form">
        <label for="cellphone">Telefone Celular(WhatsApp):</label>
        <input v-model="phoneNumber" @input="maskPhoneNumber" type="text" id="cellphone" name="cellphone" placeholder="(XX) XXXXX-XXXX">
      </div>

       <div class="cont_input_form">
        <label for="password">Senha:</label>
        <input v-model="formData.password" type="password" id="password" name="password" placeholder="Senha">
      </div>

      <div class="cont_btn_register">
        <button type="submit" class="btn_register"> Cadastrar </button>
      </div>

      
      <span class="link_register" @click="goLoginPage">
        Já tenho cadastro  
      </span>
    </form>
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
          phoneNumber : '',
          birthDate: '',
          cpf: ''
        }
    },
    methods: {
      handleSubmit() {
        this.formData.cellphone = this.phoneNumber.replace(/\D/g, '')
        this.formData.birth_date = this.birthDate.replace(/^(\d{2})\/(\d{2})\/(\d{4})$/, '$3-$2-$1');
        this.formData.cpf = this.cpf.replace(/\D/g, '')

        apiAccount.registerAccount(this.formData).then((response)=>{
          this.$notify({ type: "success", text: "Pronto, estou te enviando para o acesso!", duration: 2000});
          setTimeout(()=>{
            this.$emit('change-page', 'login')
          }, 2000);
        }).catch(()=>{
          this.$notify({ type: "warn", text: "Hum.. tem algo de errado com os dados!", duration: 2000});

        })
      },
      goLoginPage(){
        this.$emit('change-page', 'login')
      },
      maskPhoneNumber(){
        this.phoneNumber = this.phoneNumber.replace(/[\D]/g, '')
          .replace(/(\d{2})(\d)/, '($1) $2')
          .replace(this.phoneNumber[5] != 9 ? /(\d{4})(\d)/ : /(\d{5})(\d)/, '$1-$2')
          .replace(/(-\d{4})(\d+?)/, '$1');
      },
      maskBirthDate(){
        this.birthDate = this.birthDate.replace(/\D/g, '')
        .replace(/(\d{2})(\d{1})/, '$1/$2')
        .replace(/(\d{2})(\d{1})/, '$1/$2')
        .replace(/(\d{2}\/\d{2}\/\d{4}).*/, '$1')
      },
      maskCpf(){
        this.cpf = this.cpf.replace(/\D/g, '')
        .replace(/(\d{3})(\d{1,3})/, '$1.$2')
        .replace(/(\d{3})(\d{1,3})/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})/, '$1-$2')
        .replace(/(\d{3}\.\d{3}\.\d{3}-\d{2}).*/, '$1');
      }
      
    },
    mounted() {
      
    },
};
</script>

<style>
  .form {
        height: 100vh;
        display: flex;
        flex-direction: column;
        gap: 0.5rem;
        padding: 1rem;
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
    .cont_btn_register{
      display: flex;
      justify-content: center;
    }
    .cont_btn_register button{
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
    .cont_btn_register button:hover{
      opacity: 1;

    }
    .link_register {
        text-align: center;
        font-size: 1.3rem;
        color: rgb(95, 11, 11);
    }

</style>
