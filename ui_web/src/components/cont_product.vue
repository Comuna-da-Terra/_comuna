<template>
    <div>
      <ul class="cont_product">
        <h2>Lista de Produtos</h2>
        <li v-for="(product, index) in products" :key="index">
          <picture>
            <!-- <img src="https://encurtador.com.br/pDR78" alt="img_cesta"> -->
            <img src="../mock/img/mock_to_product.png" alt="img_mock">
          </picture>
          <div class="cont-body-product">
            <div class="cont-data-product">
              <label>{{ product.name }} - R$ {{ product.price }}</label>
              <div v-if="product.type" class="cont-type-product">
                <label>
                  <input type="radio" v-model="productSizes[index]" value="P" /> P
                </label>
                <label>
                  <input type="radio" v-model="productSizes[index]" value="M" /> M
                </label>
                <label>
                  <input type="radio" v-model="productSizes[index]" value="G" /> G
                </label>
              </div>
            </div>
            <div class="quantity-controls">
              <button @click="increaseAmountProduct(product.id, index)">+</button>
              <input type="text" v-model="inputAmount[index]" />
              <button @click="decreaseAmountProduct(product.id, index)">-</button>
            </div>
            <button >Quero!</button>

          </div>
        </li>
      </ul>
    </div>
    <div>
      <h2>Cesta</h2>
      <ul>
        <li v-for="(product, index) in cestaToBuy" :key="index">
          {{ product.name }} - R$ {{ product.price }} ({{ product.id }}) x{{ product.quantity }}
          <button @click="removeFromCart(index)">Remover do Carrinho</button>
        </li>
      </ul>
    </div>
</template>
  
  // ____________SCRIPT____________
<script>
export default {
  data() {
    return {
      products: [
        {
          id: 1,
          name: "Abacate",
          stock: 7,
          price: 8.00,
          type: "P",
        },
        {
          id: 2,
          name: "Banana",
          
          stock: 7,
          price: 7.00,
          type: "M",
        },
        {
          id: 3,
          name: "Alface",
          stock: 7,
          price: 6.00,
        },
        {
          id: 4,
          name: "Berinjela",
          stock: 7,
          price: 4.00,
          type: "P",
        },
        {
          id: 5,
          name: "Colve",
          stock: 7,
          price: 7.00,
        }
      ],
      productSizes: [],
      inputAmount: [],
      cestaToBuy: [
        {
          id: 1,
          id_product: 2,
          quantity: 7,
          total_price: 28
        }
      ],
    };
  },
  props: {},
  methods: {
    increaseAmountProduct(id, index) {
      this.inputAmount[index] = (this.inputAmount[index] || 0) + 1;
      controlBuy(product)
      console.log(this.inputAmount)
    },
    decreaseAmountProduct(id, index) {
      if (this.inputAmount[index] > 0) {
        this.inputAmount[index] -= 1;
        controlBuy(product)
        console.log(this.inputAmount)
      }
    },
    async createOrderProduct(product) {
      if (product.quantity > 0) {
        await serviceProductOrder.createOrder(data).then((resp)=>{
          console.log(resp)
        })
        await serviceProductOrder.getOrders(id_order).then((resp)=>{
          console.log(resp)
          this.cestaToBuy = resp.data

        })
      }
    },
    removeFromCart(index) {
      this.cestaToBuy.splice(index, 1);
    },
  },
  mounted() { }
};
</script>
  
<style scoped>
.cont_product {
  width: 100%;
  display: flex;
  flex-direction: column;
  /* gap: 0.3rem; */
}

.cont_product li picture {
  width: 70%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.cont_product li img {
  width: 100%;
}

.cont_product li {
  display: flex;
  margin: 1rem;
}

.cont-body-product {
  width: 100%;
  display: flex;
  justify-content: space-around;
}

.cont-data-product {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}

.cont-type-product {
  display: flex;
}

.cont-type-product label {
  width: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}


.quantity-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;

}

.quantity-controls button {
  /* background: none; */
  width: 100%;
  height: 100%;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  padding: 0.2rem 0.4rem;
}

.quantity-controls input {
  border: none;
  padding: 0.2rem 0.4rem;
  font-size: 1rem;
  text-align: center;
  width: 2rem;
}
.cont-type-product{
  bottom: 0;
}
</style>
  