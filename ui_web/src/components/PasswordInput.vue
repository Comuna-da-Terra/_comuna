<template>
    <div class="input-wrapper">
      <input
        :type="passwordFieldType"
        v-model="internalPassword"
        :placeholder="placeholder"
      />
      <span
        @click="switchVisibility"
        class="pi"
        :class="passwordFieldType === 'password' ? 'pi-eye' : 'pi-eye-slash'"
      ></span>
    </div>
  </template>
  
  <script>
  export default {
    props: {
        modelValue: {
        type: String,
        default: ""
      },
      placeholder: {
        type: String,
        default: "Enter password"
      }
    },
    data() {
      return {
        passwordFieldType: "password",
        internalPassword: this.modelValue
      };
    },
    watch: {
    // Atualiza o valor do input quando a prop mudar
    modelValue(newValue) {
      this.internalPassword = newValue;
    },
    // Emite a atualização para o componente pai
    internalPassword(newValue) {
        this.$emit("update:modelValue", newValue);
    }
  },
    methods: {
      switchVisibility() {
        this.passwordFieldType =
          this.passwordFieldType === "password" ? "text" : "password";
      },
    },
  };
  </script>
  
  <style scoped>
  .input-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    height: 2rem;
  }
  
  .input-wrapper input {
    width: 100%;
    height: 100%;
    padding-right: 2.5rem; /* Espaço para o ícone */
    padding-left: 1rem; /* Espaço para o ícone */
  }
  
  .input-wrapper span {
    position: absolute;
    right: 10px;
    cursor: pointer;
    font-size: 1.2rem;
    color: #666;
  }
  </style>
  