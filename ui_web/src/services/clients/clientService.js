import axios from 'axios';
import api from '@/services/api'

export default {
  async registerAccount(formData) {
    console.log(formData)
    return await api.post('/account/', formData)
      .then(response => {
        console.log(response)
        return response.data;
      })
      .catch(error => {
        console.log(error)
        throw error;
      });
  },
  
  async getAccount(id) {
    return await api.get('/account/', {})
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
};
