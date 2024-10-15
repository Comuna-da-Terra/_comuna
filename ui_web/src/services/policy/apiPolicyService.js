import api from '@/services/api'

export default {

    async createPolicy(data){
        await api.post('/policy/', data)
        .then(response=>{
            return response
        })
        .catch(error=> {
            console.log(error)
            return error
        })   
    },
    async getListPolicies(type) {
        return await api.get('/policy/', {
            params: {
                type: type  // Envia o parâmetro type como parte da query
            }
        })
        .then(response => {
            return response;
          })
          .catch(error => {
            throw error;
          });
      },
}