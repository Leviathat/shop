/* eslint-disable prettier/prettier */
import { getCart, addToCart, removeFromCart } from "@/api/cart";

export default {
  state: {
    cart: [],
    count: null,
  },
  getters: {
    getCartObject: (state) => state.cart,
    getCartCount: (state) => state.count,
  },
  mutations: {
    SET_CART_DATA(state, cartData) {
      state.cart = cartData;
    },
    CLEAR_CART(state) {
      state.cart = getCart();
    },
  },
  actions: {
    async addProductToCart({ commit, dispatch }, product) {
      const cart = await addToCart(product);
      commit("SET_CART_DATA", cart);
      dispatch("addAlert", { message: "Продукт добавлен в корзину", type: 2 });
    },
    async removeProductFromCart({ commit, dispatch }, productId) {
      const cart = await removeFromCart(productId);
      commit("SET_CART_DATA", cart);
      dispatch("addAlert", { message: "Продукт убран из корзины", type: 3 });
    },
    async fetchCart({ commit }) {
      const cart = await getCart();
      commit("SET_CART_DATA", cart);
    },
  },
};
