/* eslint-disable prettier/prettier */
import { makeOrder, getOrders, patchCancelOrder } from "@/api/order";
import router from "@/router";

export default {
  state: {
    order: {
      products: null,
    },
    orderList: null,
    total_amount: 0,
  },
  getters: {
    getOrder(state) {
      return state.order;
    },
    getOrderList(state) {
      return state.orderList;
    },
    getTotal(state) {
      return state.total_amount;
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
    SET_TOTAL_AMOUNT(state, total) {
      state.total_amount = total;
    },
  },
  actions: {
    async orderList({ commit }) {
      const response = await getOrders();
      commit("SET_ORDER_LIST", response);
    },

    async postOrder({ state, dispatch, commit }) {
      const payload = {};
      const data = {
        order: state.order,
      };
      const response = await makeOrder(data);
      if (response) {
        payload.message = "Заказ успешно оформлен";
        payload.type = 1;
        router.push("/");
        commit("CLEAR_CART");
      } else {
        payload.message = "Ошибка при оформлении заказа";
        payload.type = 4;
      }
      dispatch("addAlert", payload);
    },

    async cancelOrder({ commit, dispatch }, id) {
      const payload = {};
      const data = {
        order_id: id,
      };
      const order = await patchCancelOrder(data);
      commit("SET_CANCELLED_ORDER", order.id);
      if (order) {
        payload.message = "Заказ отменен";
        payload.type = 3;
        router.push("/");
      } else {
        payload.message = "Ошибка при отмене заказа";
        payload.type = 4;
      }
      dispatch("addAlert", payload);
    },

    async loadTotal({ commit, state }) {
      const cart = await state.cart;
      try {
        const total = cart.reduce((total, product) => {
          return total + parseFloat(product.price) * product.quantity;
        }, 0);
        commit("SET_TOTAL_AMOUNT", total);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
