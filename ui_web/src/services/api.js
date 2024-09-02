import axios from 'axios'

const api = axios.create({
    baseURL: "http://api.comunadaterra.com.br/api",
    //baseURL: "http://127.0.0.1:8000/api",
    // baseURL: "http://192.168.1.103:8000/api",
    headers: {
        'Content-Type': 'application/json'
    }
});

export default api;
