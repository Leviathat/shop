/* eslint-disable prettier/prettier */
import { makeOrder, getOrders, patchCancelOrder } from "@/api/order";

export default {
  state: {
    order: {
      products: null,
    },
    orderList: null,
  },
  getters: {
    getOrder(state) {
      return state.order;
    },
    getOrderList(state) {
      return state.orderList;
    },
  },
  mutations: {
    SET_ORDER(state, order) {
      state.order = order;
    },
    SET_ORDER_LIST(state, list) {
      state.orderList = list;
    },
    SET_CANCELLED_ORDER(state, id) {
      const order = state.orderList.find((order) => order.id === id);
      if (order) {
        order.status = 5;
        order.status_display = "Отменен";
      }
    },
  },
  actions: {
    async orderList({ commit }) {
      try {
        const response = await getOrders();
        commit("SET_ORDER_LIST", response);
      } catch (error) {
        console.log(error);
      }
    },
    async postOrder({ state }) {
      try {
        const data = {
          order: state.order,
        };
        const response = await makeOrder(data);
        console.log(response);
      } catch (error) {
        console.log(error);
      }
    },
    async cancelOrder({ commit }, id) {
      try {
        const data = {
          order_id: id,
        };
        const order = await patchCancelOrder(data);
        commit("SET_CANCELLED_ORDER", order.id);
        console.log(order);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
