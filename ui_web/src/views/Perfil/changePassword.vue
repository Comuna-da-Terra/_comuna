<template>
  <div class="cont-code-password">
      <div style="display: flex; flex-direction: column; width: 100%;">
        <label style="display: flex; justify-content: space-around; width: 100%; align-items: center;">
          <h1>Alterar senha</h1>
          <i type="button" @click.prevent="closeModal" class="pi pi-times"></i>
        </label>
        <!-- <p>Você sairá de todas as sessões, exceto desta, para proteger sua conta caso alguém esteja tentando acessá-la.</p> -->
      </div>
      <form class="cont-form" action="" @submit.prevent="handleSubmit">
        
          <input  class="impt-password" name="current_password" v-model="formData.current_password"  type="password" placeholder="Senha atual">
          <input  class="impt-password" name="new_password"  v-model="formData.new_password" type="password" placeholder="Nova senha">
          <input  class="impt-password" name="confirm_password"  v-model="formData.confirm_password" type="password" placeholder="Redigite a nova senha">
          <a href="http://127.0.0.1:8000/api/account/reset_password/">Esqueceu a senha?</a>
          <button type="submit" class="btn-code-confirm">Alterar senha</button>

      </form>
    </div>
    <div v-if="isLoading" class="c-loader"></div>
  </template>
  
  // ____________SCRIPT____________
  <script>
  import apiAccountService from '@/services/clients/apiClientService';
  
  export default {
    data() {
      return {
        isLoading: false,
        formData: {},
        user: {},
        changePassword: false,
      }
    },
    emits: ['close-modal'],
    methods: {
      async handleSubmit(){
        this.isLoading = true
        await apiAccountService.changePassword(this.formData).then((response)=>{
            this.$notify({ type: "success", text: ` ${response.data.success}`, duration: 2500});
            setTimeout(()=>{
              this.closeModal()
            }, 500)
          
        }).catch((err)=>{
          this.$notify({ type: "error", text: ` ${err.response.data.error ? err.response.data.error : "Hum.. tem algo de errado com os dados!"  }`, duration: 2000});
        })
        this.isLoading = false
        
      },
        
      async load_data(){
        await apiAccountService.getAccount().then((response)=>{
          this.user = response.data[0]
        })
      },
      closeModal() {
        this.$emit('close-modal')
        return false;
      },
    },
      mounted(){
        this.load_data()
      },
  };
</script>
  
<style>
  .cont-code-password{
    display: flex;
    flex-direction: column;
    width: 80vw;
    padding: 3px 15px 15px 15px;
    max-width: 300px;
    height: 500px;
    justify-content: space-between;
    align-items: center;
    background-color: whitesmoke;
    border-radius: 10px;
  }
  .cont-form{
    display: flex;
    flex-direction: column;
    width: 100%;
    justify-content: space-around;
    align-items: center;
    height: 100% ;
  }
  .impt-password{
    height: 20%;
    width: 100%;
    padding: 10px;
  }
  .impt-password{
    height: 50px;
    width: 80%;
  }
  .btn-code-confirm{
    width: 70%;
    height: 15%;
    border: none;
    border-radius: 10px;
    color: white;
    background-color: green;
  }
</style>
  