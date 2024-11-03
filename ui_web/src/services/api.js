import axios from 'axios'

const api = axios.create({
    //baseURL: "http://api.comunadaterra.com.br/api",
    baseURL: import.meta.env.VITE_API_BASE_URL,
    headers: {
        'Content-Type': 'application/json'
    }
});

export default api;
