import axios from 'axios';
import api from '@/services/api'

export default {
  async registerAccount(formData) {
    return await api.post('/api/account/', formData)
      .then(response => {
        console.log(response)
        return response.data;
      })
      .catch(error => {
        throw error;
      });
  },
  
  async getAccount(data) {
    return await api.post('/api/account/', data)
      .then(response => {
        console.log(response)
        return response.data;
      })
      .catch(error => {
        throw error;
      });
  },
};
