<template>
    <div class="cont-all">
      <form class="form" action="" @submit.prevent="handleSubmit">
      <div class="cont-header-perfil">
        <button type="button" class="btn-submit">
          <i class="pi pi-times" @click="this.router.push({name: 'dashboard'});"></i>
        </button>
        <h1>
          Editar Perfil
        </h1>
        <button class="btn-submit" type="submit">
          <i class="pi pi-check" type="submit" ></i>
        </button>
      </div>
        <div class="cont-img-form">
          <picture class="picture-perfil">
            <img src="../../mock/img/mock_to_perfil.png" alt="img_mock">
          </picture>
        </div>
        <div class="cont-input-form">
          <label for="first_name">Nome: </label>
          <input v-model="user.name" type="text" id="first_name" name="first_name" placeholder="Nome">
        </div>

        <div class="cont-input-form">
          <label for="email">E-mail:</label>
          <input v-model="user.email" type="text" id="email" name="email" placeholder="E-mail">
        </div>

        <div class="cont-input-form">
          <label for="email">CPF:</label>
          <input v-model="user.cpf" type="text" id="cpf" name="cpf" placeholder="___.___.___-__">
        </div>

        <div class="cont-input-form">
          <label for="birth_date">Data de Nascimento:</label>
          <input v-model="birthDate" @input="maskBirthDate" type="text" id="birth_date" name="birth_date" placeholder="Data de Nascimento">
        </div>

        <div class="cont-input-form">
          <label for="cellphone">Telefone Celular(WhatsApp):</label>
          <input v-model="phoneNumber" @input="maskPhoneNumber" type="text" id="cellphone" name="cellphone" placeholder="(XX) XXXXX-XXXX">
        </div>

        <!-- <div class="cont-input-form"> -->
          <div>
            <button class="btn-change-password" type="button"  @click="modal_changePassword = true">Alterar Senha</button>
            <div v-if="modal_changePassword" class="modal-password" >
              <changePasswordModal @close-modal="closeModal"></changePasswordModal>
            </div>

          </div>
        <!-- </div> -->
      </form>
      <div class="cont-address">
        <h2>
          Endereços cadastrados
        </h2>
        <ul style="width: 100%;">
          <li v-for="address in address_user">
            <p >
              {{ address.street }}, {{ address.number }} - {{ address.city }}/{{ address.uf }}
            </p>
            
            <div style="display: flex;">
              <!-- <i class="pi pi-pencil"></i> -->
              <i class="pi pi-trash" @click="deleteAddres(address.id)"></i>
            </div>
          </li>
        </ul>
        <button v-if="address_user.length < 3" @click="this.modal_address = true"> Cadastrar </button>
      </div>
    </div>

    <div v-if="modal_address" class="modal-address">
      <formAddress @close-modal="closeModal"></formAddress> 
    </div>
  </template>

  // ____________SCRIPT____________
  <script>
  import apiAccountService from '@/services/clients/apiClientService';
  import { useRoute, useRouter } from 'vue-router';
  import apiAddressService from "../../services/addresses/apiAddressService"
  import changePasswordModal from "../Perfil/changePassword.vue"
  import { ref } from 'vue';
  import formAddress from "../Address/register_address.vue"

  export default {
      components: {
        changePasswordModal,
        formAddress
      },
      data() {
          return {
            router: useRouter(),
            formData: {},
            phoneNumber : '',
            birthDate: '',
            user: {},
            address_user: [],
            modal_changePassword: ref(false),
            modal_address: ref(false)
          }
      },
      methods: {
        handleSubmit() {
            this.user.cellphone = this.phoneNumber
            this.user.birth_date = this.birthDate.replace(/^(\d{2})\/(\d{2})\/(\d{4})$/, '$3-$2-$1');
            this.user.id = this.user.id
            apiAccountService.editAccount(this.user).then((response)=>{
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
            await apiAccountService.getAccount().then((response)=>{
                this.user = response.data[0]
                this.birthDate = this.user.birth_date.replace(/^(\d{4})-(\d{2})-(\d{2})$/, '$3/$2/$1');
                this.phoneNumber = this.user.cellphone
            }),
            await apiAddressService.getListAddress().then((response)=>{
              this.address_user = response.data.filter(address => address.user == this.user.id )
            })
        },
        async deleteAddres(id){
          await apiAddressService.deleteAddress(id).then((response)=>{
          })
          this.load_data()
        },
        closeModal(){
          this.modal_address = false
          this.modal_changePassword = false
          this.load_data().then(()=> this.delivery_status = true)
        }
      },
      mounted() {
        this.load_data()
      },
  };
</script>

<style>
.cont-all{
  height: 100%;
  width: 100%;
}
  .cont-header-perfil{
    background-color: green;
    justify-content: space-around;
    display: flex;
    width: 95%;
    height: 80px;
    align-items: center;
    /* font-size: x-large; */
    color: white;
    margin: 1rem;
    border-radius: 7px;
  }
  .cont-header-perfil i{
    color: white;
  }
  .cont-header-perfil i:active{
    color: black;
  }
  .form {
    height: auto;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    /* padding: 1rem; */
    justify-content: center;

  }
  .btn-submit{
    border: none;
    background-color: transparent;
  }
  .cont-img-form{
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .cont-img-form picture{
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .form img{
    width: 30%;
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
  .cont-input-form{
    display: flex;
    flex-direction: column;
    justify-content: center;

  }
  .cont-input-form input{
    height: 3rem;
    font-size: 1.0rem;
    padding: 0.5rem;
  }
  .btn-change-password{
    border: none;
    border-radius: 7px;
    background-color: green;
    color: white;
    height: 3rem;
  }
  .btn-change-password{
    width: 100%;
  }
  .modal-password{
    height: 100vh;
    width: 100vw;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    backdrop-filter: blur(2.5px);
  }
  .cont-address{
    background-color: grey;
    color: white;
    width: auto;
    margin: 0px 10px 0px 10px;
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 20px;
    padding: 0.3rem;
  }
  .cont-address h2{
    background-color: green;
    width: 90%;
    padding: 0.5rem;
    margin: 0.5rem;
    border-radius: 7px;
    text-align: center;

  }
  .cont-address li{
    display: flex;
    width: 100%;
    justify-content: space-around;
  }
  .cont-address li button{
    background-color: green;
    color: white;
    border: none;
    border-radius: 7px;
  }
  .btn-add-address{
    width: auto;
    height: auto;
    padding: 0.5rem;
    opacity: 0.3;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0.5rem;
  }
  .btn-add-address:hover{
    opacity: 1;
    
  }
  .modal-address{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 90vh;
    max-width: 300px;
    position: fixed;
    z-index: 1;
  }
  .pi{
    display: flex;
    justify-content: center;
    align-items: center;
    /* border: solid; */
    border-radius: 7px;
    padding: 4px;
  }
  .pi-trash{
    background-color: red;
    opacity: 0.2;
  }    
  .pi-trash:hover{
    opacity: 1;
  }
  .pi-pencil{
    background-color: orange;  
    opacity: 0.2;
  }
  .pi-pencil:hover{
    opacity: 1;

  }
</style>
