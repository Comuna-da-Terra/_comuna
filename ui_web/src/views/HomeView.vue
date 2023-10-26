<template>
    <div class="app-logo">
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="400" height="400"  @animationend="logoAnimationEnd"/>
    </div>
    <div class="cont-login" v-if="!showLogo">
      <loginPage v-if="page == 'login'"  @change-page="changePage"></loginPage>
      <registerPage v-if="page == 'register'" @change-page="changePage"> </registerPage>
    </div>
</template>

// ____________SCRIPT____________
<script>
// import { useRoute, useRouter } from 'vue-router';
import loginPage from './Login/clientLogin.vue' ;
import registerPage from './Register/clientRegister.vue' ;

export default {
  components: {
    loginPage,
    registerPage,
  },
  data() {
    return {
      // router: useRouter(),
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



<style scoped>
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
}
@keyframes grow {
  from {
    width: 100px; 
    height: 100px;
  }
  to {
    width: 400px;
    height: 400px;
  }
}
.cont-login{
  z-index: 1;
  height: 100vh;
}
@media screen {
  
}

</style>
