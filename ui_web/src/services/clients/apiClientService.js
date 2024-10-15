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
  async getAccounts(id) {
    return await api.get('/accounts/admin/', {})
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  
  async changePassword(formData){
    return await api.patch('/account/change-password/', formData)
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async resetPassword(formData){
    return await api.patch('/account/reset_password/', formData)
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  }
};
