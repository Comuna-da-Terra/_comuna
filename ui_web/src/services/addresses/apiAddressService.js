import api from '@/services/api'

export default {
  async registerAddress(formData) {
    return await api.post('/account/address/', formData)
      .then(response => {
        return response.data;
      })
      .catch(error => {
        throw error;
      });
  },
  
  async getListAddress() {
    return await api.get('/account/address/', {})
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async getAddress(id) {
    return await api.get(`/account/address/${id}/`, {})
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
};
