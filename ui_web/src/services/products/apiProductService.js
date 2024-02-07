import axios from 'axios';
import api from '@/services/api'

export default {
  async getAllProducts(page) {
    if(page){
      console.log('test')
      return await api.get(`/products/?page=${page}`)
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      }) 
    } else {
     return await api.get('/products/')
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      })
    } 

  },
  async ProductsInOrderAccountView() {
    return await api.get('/products/order/')
      .then(response => {
        return response;
      })
      .catch(error => {
        return error.response.data.detail;
      });
  },
}