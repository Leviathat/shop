/* eslint-disable prettier/prettier */
export default {
  state: {
    loaded: false,
  },
  getters: {
    getLoaded: (state) => state.loaded,
  },
  mutations: {
    setLoaded(state, value) {
      state.loaded = value;
    },
  },
  actions: {
    Loaded({ commit }, value) {
      commit("setLoaded", value);
    },
  },
};
