import api from "@/services/api"

export default {
    async createPayment(data) {
        await api.post("payment/", data).then(response => {
        }).catch(err =>{
            throw err
        })    
    }
}