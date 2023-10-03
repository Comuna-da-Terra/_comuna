import { defineStore } from 'pinia';
import api from '@/services/api';
import jwtDecode from 'jwt-decode';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null,
    user_id: null
  }),

  actions: {
    async verifyAccessToken() {
      try {
          const token = localStorage.getItem('token');
        if (!token) {
          this.accessToken = false;
          return false;
        }

        api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        const response = await api.get('/auth/verify/')
        if (response.status === 200 && response.data.valid) {
          this.user_id = jwtDecode(token).user_id;
          this.accessToken = true;
          return true;
        
        } else {
          localStorage.removeItem('token')
          localStorage.removeItem('refresh_token')
          this.accessToken = false;
          return false;

        }
      } catch (error) {
        localStorage.removeItem('token')
        localStorage.removeItem('refresh_token')
        this.accessToken = false;
        return false;

      }
    },
  },
});
