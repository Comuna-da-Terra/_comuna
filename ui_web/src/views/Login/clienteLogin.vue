<template>
  <main>
    <form class="form" action="">
  
       <div class="cont_input_form">
        <label for="email">E-mail:</label>
        <input type="text" name="email" placeholder="E-mail">
      </div>

       <div class="cont_input_form">
        <label for="senha">Senha:</label>
        <input type="text" name="senha" placeholder="Senha">
      </div>

      <div class="cont_btn_login">
        <RouterLink style="width: 100%" to="/dashboard">
          <button type="submit" class="btn_register"> Login </button> 
        </RouterLink>
      </div>

      
      <span class="link_login">
        <RouterLink to="register"> Quero participar!  </RouterLink>
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

<style scoped>
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
    .cont_btn_login{
      display: flex;
      justify-content: center;
    }
    .cont_btn_login button{
      margin-top: 1rem;
      cursor: pointer;
      height: 2.5rem;
      width: 100%;
      background-color: green;
      border: none;
      border-radius: 3px;
      opacity: 0.4;
    }
    .cont_btn_login button:hover{
      opacity: 0.8;

    }
    .link_login {
        text-align: center;
        font-size: 1.3rem;
    }

</style>
