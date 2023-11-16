import axios from 'axios';
import api from '@/services/api'

export default {
  async registerAccount(formData) {

    return await api.post('/account/register/', formData)
      .then(response => {

        return response.data;
      })
      .catch(error => {
        console.log(error)
        throw error;
      });
  },
  
  async editAccount(formData) {

    return await api.patch(`account/${formData.id}/`, formData)
      .then(response => {
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
