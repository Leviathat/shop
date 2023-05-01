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
    async register({ commit }, newUser) {
      try {
        const response = await registerUser(newUser);
        commit("SET_USER", response);
        router.push("/login");
      } catch (error) {
        console.log(error);
      }
    },
    async login({ commit }, userData) {
      try {
        const response = await loginUser(userData);
        commit("SET_USER", response);
        router.push("/");
      } catch (error) {
        console.log(error);
      }
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
