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
      console.log(response);
      dispatch("addAlert", { message: "Ошибка при регистрации", type: 4 });
    },
    async login({ commit, dispatch }, userData) {
      const response = await loginUser(userData);
      commit("SET_USER", response);
      const payload = {}
      
      if (response.status) {
        payload.message = "Вы успешно авторизовались"
        payload.type = 2
        router.push("/")
      }
      else {
        payload.message = "Ошибка при авторизации"
        payload.type = 4 
      }
      dispatch("addAlert", payload);
    },
    async info({ commit }) {
      try {
        const response = await userInfo();
        commit("SET_USER", response);
      } catch (error) {
        router.push("/login");
        console.log(error);
      }
    },
  },
};
