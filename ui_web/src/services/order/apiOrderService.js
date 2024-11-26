import api from '@/services/api'

export default {

  async getOrder() {
    return await api.get('order/active/', {})
       .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async getOpenOrders() {
    return await api.get('order/opens/', {})
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async getHistoryOrders() {
    return await api.get('order/history/', {})
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async updateOrder(data) {
    return await api.patch(`order/updated/${data.id}/`, data )
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async getOrdersCSV() {
    const csvURL = `${import.meta.env.VITE_API_BASE_URL}/orders/csv/`;
    window.location.href = csvURL
  }
}