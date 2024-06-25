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
    console.log(data)
    return await api.patch(`order/updated/${data.id}/`, data )
      .then(response => {
        return response;
      })
      .catch(error => {
        throw error;
      });
  },
  async getOrdersCSV() {
    const csvURL = "http://127.0.0.1:8000/api/orders/csv/";
    
    // const csvURL = "http://192.168.1.103:8000/api/orders/csv/";
    window.location.href = csvURL
  }
}