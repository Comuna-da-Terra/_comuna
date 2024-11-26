<template>
    <div class="app-logo">
      <img alt="Vue logo" class="logo" src="@/assets/logo.png"   @animationend="logoAnimationEnd"/>
    </div>
    <div class="cont-login" v-if="!showLogo">
      <loginPage v-if="page == 'login'"  @change-page="changePage"></loginPage>
      <registerPage v-if="page == 'register'" @change-page="changePage"> </registerPage>
    </div>
</template>

// ____________SCRIPT____________
<script>
import loginPage from './Login/clientLogin.vue' ;
import registerPage from './Register/clientRegister.vue' ;

export default {
  components: {
    loginPage,
    registerPage,
  },
  data() {
    return {
      showLogo: true,
      page: "login"
    };
  },
  methods: {
    logoAnimationEnd() {
    },
    changePage(page){
      this.page = page
    }
  },
  mounted() {
    
    setTimeout(() => {
      this.showLogo = false;
    }, 2000); 
  },
};
</script>



<style>
main{
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.app-logo{
  width: 100%;
  display: flex;
  justify-content: center;
  position: absolute;
  opacity: 0.3;
}
.logo {
  animation: grow 2.5s linear;
  width: 600px;
  height: 600px;
}
@keyframes grow {
  from {
    width: 100px; 
    height: 100px;
  }
  to {
    width: 600px;
    height: 600px;
  }
}
.cont-login{
  z-index: 1;
  height: 100vh;
}
@media screen {
  
}

.c-loader {
    animation: is-rotating 1s infinite;
    border: 7px solid #e5e5e5;
    border-radius: 50%;
    border-top-color: #0c981a;
    height: 70px;
    width: 70px;
    position: fixed;
  }
  @keyframes is-rotating {
    to {
      transform: rotate(1turn);
    }
  }

</style>
