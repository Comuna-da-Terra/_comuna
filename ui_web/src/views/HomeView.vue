<template>
    <div class="app-logo">
      <img v-if="showLogo"  alt="Vue logo" class="logo" src="@/assets/logo.svg" width="500" height="500"  @animationend="logoAnimationEnd"/>

      <div class="cont_buttons" v-else>
        <button >
          <RouterLink to="/client/login">
            Cliente
          </RouterLink>
        </button>
        <button>
          <RouterLink to="/member/login">
            Membro
          </RouterLink>
        </button>
      </div>

    </div>
</template>

// ____________SCRIPT____________
<script>
export default {
  data() {
    return {
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
