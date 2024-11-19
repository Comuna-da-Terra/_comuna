import api from "@/services/api"

export default {
  async createBasketPlan(data) {
      try {
          const response = await api.post("basketplan/", data);
          return response.data;

      } catch (err) {
          throw err
      }    
  },
  async getBasketPlan() {
      try {
        const response = await api.get("basketplan/");
        return response.data;  
      } catch (err) {
        throw err;
      }
  },
  async getAllBasketPlans() {
      try {
        const response = await api.get("basketplan/all/");
        return response.data;  
      } catch (err) {
        throw err;
      }
  },
  async editBasketPlan(data) {
    console.log(data)
      try {
        const response = await api.patch("basketplan/edit/", data);
        return response.data;  
      } catch (err) {
        throw err;
      }
  }, 
  // async getDeliveryBasket() {
  //   try {
  //     const response = await api.post("basketplan/delivery/");
  //     return response.data;  
  //   } catch (err) {
  //     throw err;
  //   }
  // },
}