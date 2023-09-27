<template>
    <div class="app-logo">
      <img v-if="showLogo"  alt="Vue logo" class="logo" src="@/assets/logo.svg" width="400" height="400"  @animationend="logoAnimationEnd"/>
    </div>
</template>

// ____________SCRIPT____________
<script>
import { useRoute, useRouter } from 'vue-router';

export default {
  data() {
    return {
      router: useRouter(),
      showLogo: true, // Inicialmente, mostramos o logor
    };
  },
  methods: {
    logoAnimationEnd() {
      this.showLogo = false;
    },
  },
  mounted() {
    
    setTimeout(() => {
      this.showLogo = false;
      this.router.push({name:'login'})

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
}
.cont_buttons{
  height: 100%;
  width: 100%;
  display: flex;
  justify-content: space-evenly;
}
.cont_buttons button {
  height: 15vh;
  width: 25vw;
  font-size: 3rem;
}

</style>
