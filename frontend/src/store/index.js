import Vuex from "vuex";
import user from "@/store/modules/user";
import product from "@/store/modules/product";
import cart from "@/store/modules/cart";
import order from "@/store/modules/order";

export default new Vuex.Store({
  modules: {
    user,
    product,
    cart,
    order,
  },
});
