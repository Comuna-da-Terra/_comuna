<template>
  <div class="cont-form-address">
    <div style="display: flex; justify-content: end; position: absolute; right: 2rem;">
      <i type="button" @click.prevent="closeModal" class="pi pi-times"></i>

    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
      <h1>Criar Endereço</h1>
    </div>
    <form class="form-address" @submit.prevent="submitForm">
      <div class="cont-input-cep">
        <label for="zip_code"> CEP: </label>
        <input v-model="formData.zip_code" name="zip_code" required maxlength="8" minlength="8" />
        <button type="button" @click.prevent="fetchAddress">
          <!-- <i class="pi pi-map"></i> -->
          <i class="pi pi-map-marker"></i>

        </button>
        <span style="display: flex; width: 100%; justify-content: center;" v-if="errors.zip_code" class="error">{{ errors.zip_code}}</span>
      </div>
      <div class="cont-input-address">
        <label for="state"> Estado: </label>
        <input class="inp-address" v-model="formData.state" name="state" required :disabled="readOnlyFields"/>
        <span v-if="errors.uf" class="error">{{ errors.uf[0] }}</span>
      </div>
      <div class="cont-input-address">
        <label for="city"> Cidade: </label>
        <input class="inp-address" v-model="formData.city" name="city" required maxlength="64" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.city" class="error">{{ errors.city[0] }}</span> -->
      </div>
      <div class="cont-input-address">
        <label for="neighborhood"> Bairro: </label>
        <input class="inp-address" v-model="formData.neighborhood" name="neighborhood" required maxlength="64" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.neighborhood" class="error">{{ errors.neighborhood[0] }}</span> -->
      </div>
      <div class="cont-input-address">
        <label for="street"> Rua: </label>
        <input class="inp-address" v-model="formData.street" name="street" required maxlength="64" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.street" class="error">{{ errors.street[0] }}</span> -->
      </div>
      <div class="cont-input-address">
        <label for="number"> Número: </label>
        <input class="inp-address" v-model="formData.number" name="number" required maxlength="10" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.number" class="error">{{ errors.number[0] }}</span> -->
      </div>
      <div class="cont-input-address" style="display: flex; flex-direction: column;">
        <label for="complement"> Complemento: </label>
        <textarea class="inp-address" v-model="formData.complement" name="complement" rows="4" style="resize: none;"  maxlength="120" :disabled="readOnlyFields"></textarea>
        <!-- <span v-if="errors.uf" class="error">{{ errors.uf[0] }}</span> -->
      </div>
      <button type="submit">Salvar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import apiAddresses from '../../services/addresses/apiAddressService';
export default {
  data() {
    return {
      formData: {
        country: 'Brasil',
      },
      readOnlyFields: true,
      errors: {},
    };
  },
  emits: ['close-modal'],
  methods: {
    async submitForm() {
      apiAddresses.registerAddress(this.formData).then(response => {
          this.closeModal()
        })
        .catch(error => {
          console.error(error);
        });
    },
    fetchAddress() {
    if (!this.formData.zip_code) {
      this.errors.zip_code = 'CEP é obrigatório';
      return;
    }else{
      this.errors.zip_code = ''
    }

      const cep = this.formData.zip_code.replace(/\D/g, '');

      if (cep.length === 8) {
        axios
          .get(`https://viacep.com.br/ws/${cep}/json/`)
          .then(response => {
            if (!response.data.erro) {
              this.formData.street = response.data.logradouro;
              this.formData.city = response.data.localidade;
              this.formData.uf = response.data.uf;
              this.formData.neighborhood = response.data.bairro;
            }
            this.readOnlyFields = false
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    closeModal() {
      this.$emit('close-modal')
      return false;
    },
  },
};
</script>

<style>
.cont-form-address{
  width: 300px;
  display: flex;
  background-color: whitesmoke;
  padding: 1rem;
  margin: 1rem;
  border-radius: 8px;
  flex-direction: column;
  height: fit-content;
}
.form_address{
  height: auto;
  width: 100%;
}
.cont-input-address{
  display: flex;
  flex-direction: column;
}
.inp-address {
  background-color: grey;
  border: none;
  border-radius: 7px;
  color: white;
  font-size: 1.0rem;
  padding: 0.5rem;
}
.cont-input-cep{
  display: flex;
  gap: 5px;
}
.cont-input-cep button{
  border: none;
  background-color: transparent;
  border-radius: 100%;
  height: 100%;
  padding: 0;
}
.pi-map-marker{
  cursor: pointer;
  color: red;
  background: rgba(3, 95, 3, 0.43);
  box-shadow: 0px 2px 3px black;
}
.pi-map-marker:active{
  box-shadow: none
}
.error {
  color: rgb(192, 7, 7);
}
</style>
