import axios from 'axios';
import api from '@/services/api'

export default {
  async registerAccount(formData) {
    return await api.post('', formData)
      .then(response => {
        console.log(response)
        return response.data;
      })
      .catch(error => {
        throw error;
      });
  },
}