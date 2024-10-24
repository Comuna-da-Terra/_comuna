import axios from 'axios';
import api from '@/services/api'

export default {
  async createOrderProduct(data) {
    return await api.post('/order/product/', data)
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async updateOrderProduct(data) {
    return await api.patch(`/order/product/update/${data.id}/`, data)
    .then(response => {
      return response;
      })
      .catch(error => {
        return error;
      });
  },
  async getOrderProduct() {
 
    return await api.get('/order/product/')
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async deleteOrderProduct(id) {
 
    return await api.delete(`/order/product/delete/${id}/`)
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
}