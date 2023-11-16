<template>
    <main class="cont_all">
        Em desenvolvimento...
        <button @click="this.router.push({name: 'dashboard'});">Voltar</button>
        <!-- <form class="form" action="" @submit.prevent="handleSubmit">
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
  
        <div class="cont_btn_edit">
          <button type="submit" class="btn_edit"> Cadastrar </button>
        </div>
  
        
      </form> -->
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
            user: {},
          }
      },
      methods: {
        handleSubmit() {
            this.formData.cellphone = this.phoneNumber
            this.formData.birth_date = this.birthDate.replace(/^(\d{2})\/(\d{2})\/(\d{4})$/, '$3-$2-$1');
            this.formData.id = this.user.id

            apiAccount.editAccount(this.formData).then((response)=>{
                this.$notify({ type: "success", text: "Pronto, Perfil Editado!", duration: 2000});
            }).catch(()=>{
                this.$notify({ type: "warn", text: "Hum.. tem algo de errado com os dados!", duration: 2000});
    
            })
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
        async load_data(){
            await apiAccountService.getAccount(this.user_id).then((response)=>{
                this.user = response.data[0]
                console.log(this.user)
            })
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
      .cont_btn_edit{
        display: flex;
        justify-content: center;
      }
      .cont_btn_edit button{
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
      .cont_btn_edit button:hover{
        opacity: 1;
  
      }
  
  </style>
  