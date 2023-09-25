<template>
  <main>
    <form class="form" action="">
       <div class="cont_input_form">
        <label for="name">Nome: </label>
      <input type="text" name="name" placeholder="Nome">
      </div>
      
       <div class="cont_input_form">
        <label for="sobrenome">Sobrenome:</label>
        <input type="text" name="sobrenome" placeholder="Sobrenome">
      </div>
      
       <div class="cont_input_form">
        <label for="email">E-mail:</label>
        <input type="text" name="email" placeholder="E-mail">
      </div>

       <div class="cont_input_form">
        <label for="birth_date">Data de Nascimento:</label>
        <input type="text" name="birth_date" placeholder="Data de Nascimento">
      </div>
      
       <div class="cont_input_form">
        <label for="cellphone">Telefone Celular:</label>
        <input type="text" name="cellphone" placeholder="WhatsApp">
      </div>

       <div class="cont_input_form">
        <label for="senha">Senha:</label>
        <input type="text" name="senha" placeholder="Senha">
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
export default {
    data() {
        return {
      
        }
    },
    methods: {
      
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
