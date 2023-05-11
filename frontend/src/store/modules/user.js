/* eslint-disable prettier/prettier */
import { registerUser, loginUser, userInfo } from "@/api/auth";
import router from "@/router";

export default {
  state: {
    user: null,
  },
  getters: {
    getUser(state) {
      return state.user;
    },
  },
  mutations: {
    SET_USER(state, user) {
      state.user = user;
    },
  },
  actions: {
    async register({ commit, dispatch }, newUser) {
      const response = await registerUser(newUser);
      commit("SET_USER", response);
      const payload = {};

      if (response) {
        payload.message = "Вы успешно зарегистрировались";
        payload.type = 2;
        router.push("/");
      } else {
        payload.message = "Ошибка при регистрации";
        payload.type = 4;
      }
      dispatch("addAlert", payload);
    },
    async login({ commit, dispatch }, userData) {
      const response = await loginUser(userData);
      commit("SET_USER", response);
      const payload = {};

      if (response) {
        payload.message = "Вы успешно авторизовались";
        payload.type = 2;
        router.push("/");
      } else {
        payload.message = "Ошибка при авторизации";
        payload.type = 4;
      }
      dispatch("addAlert", payload);
    },
    async info({ commit }) {
      const response = await userInfo();
      commit("SET_USER", response);
    },
  },
};
