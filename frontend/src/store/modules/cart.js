/* eslint-disable prettier/prettier */
import { getCart, addToCart, removeFromCart } from "@/api/cart";

export default {
  state: {
    cart: getCart(),
    count: null
  },
  getters: {
    getCartObject: state => state.cart,
    getCartCount: state => state.count,
  },
  mutations: {
    SET_CART_DATA(state, cartData) {
      state.cart = cartData;
    },
  },
  actions: {
    async addProductToCart({ commit }, product) {
      try {
        const cart = await addToCart(product);
        commit("SET_CART_DATA", cart);
      } catch (error) {
        console.log(error);
      }
    },
    async removeProductFromCart({ commit }, productId) {
      try {
        const cart = await removeFromCart(productId);
        commit("SET_CART_DATA", cart);
      } catch (error) {
        console.log(error);
      }
    },
  },
};
