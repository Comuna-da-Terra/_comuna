import axios from 'axios';
import api from '@/services/api'

export default {
  async login(formData) {
    return await api.post('/api/login/', formData)
      .then(response => {
        console.log(response)
        return response.data;
      })
      .catch(error => {
        throw error; // Rejeita a promessa com o erro
      });
  },
};
