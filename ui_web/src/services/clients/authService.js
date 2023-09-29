import api from '@/services/api'
import {useAuthStore} from '@/stores/auth.js'

export default {
  
  async login(formData) {
    const auth = useAuthStore()

    return await api.post('/auth/', formData)
    .then((resp) => {
      localStorage.setItem('token', resp.data.access)
      localStorage.setItem('refresh_token', resp.data.refresh)
      auth.verificarTokenDeAcesso()

      return resp.data;
    })
      .catch(error => {
        throw error;
      });
  },
};
