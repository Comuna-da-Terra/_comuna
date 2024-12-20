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
      return response
    })
    .catch(error=> {
      return error
    })   
  },
  async uploadProductFile(data) {
    try {
      //const csrfToken = document.cookie.split(';').find(cookie => cookie.trim().startsWith('csrftoken='));

      // if (!csrfToken) {
      //   console.log("Token CSRF não encontrado.")
      //   throw new Error("Token CSRF não encontrado.");
      // }
      //const csrfValue = csrfToken.split('=')[1];
      
      const response = await api.post("upload_products/", data, {
        headers: {
          'Content-Type': 'multipart/form-data', 
          //'X-CSRFToken': csrfValue,
        }
      });
      
      return response.data;
    } catch (err) {
      console.log(err)
      throw err;
    }
  }
}