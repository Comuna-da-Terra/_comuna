<template>
  <main class="cont-all-register">
      <div @click="this.$emit('change-page', 'login')" class="notify-register-sucess" v-if="registerSucess">
      <h1>
        Foi enviado um link para o E-mail informado, acesse o mesmo para ativar sua conta. 
      </h1>
      <h2>Ele ira expirar em 10 minutos!</h2>
    </div>
  
    <form v-else class="form" action="" @submit.prevent="handleSubmit">
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
        <PasswordInput
          v-model="formData.password"
          placeholder="Digite sua senha"
        />
        <!-- <div class="input-wrapper">
          <input v-model="formData.password" :type="passwordFieldType" id="password" name="password" placeholder="Senha">
          <span @click="switchVisibility" class="pi" :class="passwordFieldType === 'password' ? 'pi-eye' : 'pi-eye-slash'"></span>
        </div> -->
        <!-- <input v-model="formData.password" :type=passwordFieldType id="password" name="password" placeholder="Senha">
        <span @click="switchVisibility" class="pi pi-eye"> </span> -->
      </div>

      <div class="cont_input_form">
        <span>
          <input v-model="formData.policy" type="checkbox" required>
          <p>Concordo com os
            <a href="termosdeuso" target="_blank"> Termos de Uso</a>
            e
            <a href="politicadeprivacidade" target="_blank">Polítca de privacidade </a>
          </p>
        </span>
      </div>

      <div class="cont_btn_register">
        <button type="submit" class="btn_register"> Cadastrar </button>
      </div>

      
      <span class="link_register" @click="goLoginPage">
        Já possuo cadastro  
      </span>
    </form>
  </main>
</template>

// ____________SCRIPT____________
<script>
import apiAccount from '@/services/clients/apiClientService'; // Certifique-se de ajustar o caminho correto
import { useRoute, useRouter } from 'vue-router';
import PasswordInput from '../../components/passwordInput.vue';

export default {  
    components: {
      PasswordInput,
    },    
    data() {
        return {
          baseURL: import.meta.env.VITE_WEB_BASE_URL,
          router: useRouter(),
          formData: {},
          phoneNumber : '',
          birthDate: '',
          cpf: '',
          policy: false,
          passwordFieldType: "password",
          registerSucess: false,
        }
    },
    methods: {
      handleSubmit() {
        this.formData.cellphone = this.phoneNumber.replace(/\D/g, '')
        this.formData.birth_date = this.birthDate.replace(/^(\d{2})\/(\d{2})\/(\d{4})$/, '$3-$2-$1');
        this.formData.cpf = this.cpf.replace(/\D/g, '')

        apiAccount.registerAccount(this.formData).then((response)=>{
          this.registerSucess = true
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
      },
      switchVisibility(){
        this.passwordFieldType = this.passwordFieldType === "password" ? "text" : "password";
      }
    },
    mounted() {
      
    },
};
</script>

<style>
  .form {
        
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
      height: 2.0rem;
      font-size: 1.0rem;
      padding: 0.5rem;
    }
    input[type="checkbox"]{
      opacity: 1;
    }
    .cont_input_form span{
      display: flex;
      align-items: center;
      gap: 1rem;
    }
    .cont_btn_register{
      display: flex;
      justify-content: center;
    }
    .cont_btn_register button{
      margin-top: 0rem;
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
    i{
      color: blue;
      cursor: pointer;
      opacity: 0.8;
    }
    i:hover{
      opacity: 1;
    }
    .link_register {
      text-align: center;
      font-size: 1.3rem;
      color: #fff;
      -webkit-text-stroke-width: 0.04em; 
      -webkit-text-stroke-color: white; 
      -webkit-text-fill-color: #573009;
      font-weight: bold;
      cursor: pointer;
    }

    .input-wrapper {
      position: relative;
      display: flex;
      align-items: center;
    }

    .input-wrapper input {
      width: 100%;
      padding-right: 2.5rem; /* Espaço para o ícone */
    }

    .input-wrapper span {
      position: absolute;
      right: 10px;
      cursor: pointer;
      font-size: 1.2rem;
      color: #666;
    }
    .notify-register-sucess{
      display: flex;
      align-items: center; 
      flex-direction: column; 
      text-align: center;
      justify-content: center;
      height: 100%;
      width: 100%;
    }
</style>
