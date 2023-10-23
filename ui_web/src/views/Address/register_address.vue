<template>
  <div class="cont-form-address">
    <div style="display: flex; justify-content: end; position: absolute; right: 0.5rem;">
      <i type="button" @click.prevent="closeModal" class="pi pi-times"></i>

    </div>
    <div style="display: flex; align-items: center; justify-content: center;">
      <h1>Criar Endereço</h1>
    </div>
    <form class="form-address" @submit.prevent="submitForm">
      <div class="cont-input-form">
        <label for="zip_code"> CEP: </label>
        <input v-model="formData.zip_code" name="zip_code" required maxlength="8" minlength="8" />
        <button type="button" @click.prevent="fetchAddress">
          <!-- <i class="pi pi-map"></i> -->
          <i class="pi pi-map-marker"></i>

        </button>
        <span style="display: flex; width: 100%; justify-content: center;" v-if="errors.zip_code" class="error">{{ errors.zip_code}}</span>
      </div>
      <div class="cont-input-form">
        <label for="state"> Estado: </label>
        <input v-model="formData.state" name="state" required :disabled="readOnlyFields"/>
        <span v-if="errors.uf" class="error">{{ errors.uf[0] }}</span>
      </div>
      <div class="cont-input-form">
        <label for="city"> Cidade: </label>
        <input v-model="formData.city" name="city" required maxlength="64" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.city" class="error">{{ errors.city[0] }}</span> -->
      </div>
      <div class="cont-input-form">
        <label for="neighborhood"> Bairro: </label>
        <input v-model="formData.neighborhood" name="neighborhood" required maxlength="64" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.neighborhood" class="error">{{ errors.neighborhood[0] }}</span> -->
      </div>
      <div class="cont-input-form">
        <label for="street"> Rua: </label>
        <input v-model="formData.street" name="street" required maxlength="64" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.street" class="error">{{ errors.street[0] }}</span> -->
      </div>
      <div class="cont-input-form">
        <label for="number"> Número: </label>
        <input v-model="formData.number" name="number" required maxlength="10" :disabled="readOnlyFields"/>
        <!-- <span v-if="errors.number" class="error">{{ errors.number[0] }}</span> -->
      </div>
      <div class="cont-input-form" style="display: flex; flex-direction: column;">
        <label for="complement"> Complemento: </label>
        <textarea v-model="formData.complement" name="complement" rows="4" style="resize: none;"  maxlength="120" :disabled="readOnlyFields"></textarea>
        <!-- <span v-if="errors.uf" class="error">{{ errors.uf[0] }}</span> -->
      </div>
      <button type="submit">Salvar</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import apiAddresses from '../../services/addresses/apiAddresses';
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
      // Emitir um evento para notificar o pai para fechar o modal
      this.$emit('close-modal')
      return false;
    },
  },
};
</script>

<style>
.cont-form-address{
  display: flex;
  flex-direction: column;
}
.form_address{
  width: 100%;
}
.cont-input-form {
  margin-bottom: 1rem;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
.error {
  color: red;
}
</style>
