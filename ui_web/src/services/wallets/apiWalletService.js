import axios from "axios"
import api from "@/services/api"

export default{
    async getWallet(){
        return await api.get("/wallet").then(response=>{
            return response;
        }).catch(err=>{
            throw err
        })
    },

    async editWallet(data){
        return await api.patch("/wallet", data).then(response=>{
            console.log(response.data)
            return response
            
        }).catch(err=>{
            throw err
        })
    },

    async getAllWallets(){
        return await api.get("/admin/wallets").then(response=>{
            console.log(response.data)
            return response
        }).catch(err=>{
            throw err
        })
    }
}