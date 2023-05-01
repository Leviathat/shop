/* eslint-disable prettier/prettier */
import { makeOrder } from "@/api/order";

export default {
  state: {
    order: {
      total_amount: null,
      products: null,
    },
  },
  getters: {
    getOrder(state) {
      return state.order;
    },
  },
  mutations: {
    SET_ORDER(state, order) {
      state.order = order;
    },
  },
  actions: {
    async postOrder({ state }) {
      try {
        const data = {
            "order": state.order
        };
        const response = await makeOrder(data);
        console.log(response)
      } catch (error) {
        console.log(error);
      }
    },
  },
};
