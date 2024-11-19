<template>
    <div class="cont-modal">
      <div class="modal-payment">
      <div style="display: flex;">
        <h2>Confirmar Pagamento</h2>
        <i type="button" @click.prevent="closeModal" class="pi pi-times"></i>
      </div>
      <form action="" @submit.prevent="handleSubmit">
        <label for="cliente">Cliente: {{ client.name }}</label>
        <input type="date" v-model="formData.date_payment"> 
        <input type="number" v-model="formData.value_payment" placeholder="R$0,00" step="0.01">
        <button type="submit">Confirmar</button>
      </form>
    </div>
    </div>
  </template>
  
  <script>
  import apiPaymentService from "@/services/payment/apiPaymentService";

  export default {
    props:{
        client: {
            type: Object,
            required: true,
        },
    },
    data() {
      return {
        formData: {
          user: this.client.id,
          date_payment: new Date().toISOString().slice(0, 10),
          value_payment: null
        }
      };
    },
    emits: ['pagamentoConfirmado'],
    methods: {
      async handleSubmit() {
        if (!this.formData.date_payment || !this.formData.value_payment) {
          alert('Preencha todos os campos!');
          return;
        }
        
    
        await apiPaymentService.createPayment(this.formData).then(response=>{
        })
        this.closeModal(
          this.$notify({ type: "success", text: "Pagamento Registrado", duration: 2000})
          
        )
      },

      closeModal() {
        this.$emit('close-modal')
        return false;
      },
    },
  };
  </script>

<style scoped>
.cont-modal{
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;

}
.modal-payment{
  background-color: whitesmoke;
  width: 30vw;
  height: 35vh;
  border: none;
  border-radius: 3%;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
  
}
.modal-payment form{
  display: flex;
  height: 50%;
  flex-direction: column;
  justify-content: space-between;
}

</style>