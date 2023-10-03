import axios from 'axios';
import api from '@/services/api'

export default {
  async createOrderProduct(data) {
    console.log(data)
    return await api.post('/order/product/', data)
      .then(response => {
        console.log(response)
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async getOrderProduct() {
 
    return await api.get('/order/product/')
      .then(response => {
        console.log(response)
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async deleteOrderProduct(id) {
 
    return await api.delete(`/order/product/delete/${id}`)
      .then(response => {
        console.log(response)
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
}