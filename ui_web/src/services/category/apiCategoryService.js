import api from '@/services/api'

export default {
  async getListCategory() {
    return await api.get('/product/category/', {})
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async createCategory(data){
    return await api.post('/product/category/', data)
      .then(response=> {
        return response
      })
      .catch(error =>{
        throw error;
      })
  }
};
