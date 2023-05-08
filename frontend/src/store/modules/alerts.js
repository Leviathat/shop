/* eslint-disable prettier/prettier */

export default {
  state: {
    alerts: [],
  },
  getters: {
    getAlerts: (state) => state.alerts,
  },
  mutations: {
    ADD_ALERT(state, alert) {
      state.alerts.push(alert);
    },
    REMOVE_ALERT(state, id) {
      const index = state.alerts.findIndex((a) => a.id === id);
      if (index !== -1) {
        state.alerts.splice(index, 1);
      }
    },
  },
  actions: {
    async addAlert({ commit }, { message, type }) {
      const id = Math.random().toString(36);
      const duration = 1300; 
      const alert = { id, message, type, duration };
      commit("ADD_ALERT", alert);
      setTimeout(() => {
        commit("REMOVE_ALERT", id);
      }, duration);
    },
  },
};
