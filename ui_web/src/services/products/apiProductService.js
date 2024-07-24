import axios from 'axios';
import api from '@/services/api'

export default {
  async getAllProducts() {
    return await api.get('/all_products/').then(response => {
      return response;
    }).catch(error => {
      throw error;
    })
  },
  async getPageProducts(page) {
    if(page){
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
        console.log(error.response.data.detail)
        return error.response.data.detail;
      });
  },
  async editProduct(data){
    await api.patch(`/product/${data.id}/`, data)
    .then(response=> {
      return response
    })
  },
  async createProduct(data){
    await api.post('/products/', data)
    .then(response=>{
      console.log(response)
      return response
    })
    .catch(error=> {
      return error
    })   
  }
}