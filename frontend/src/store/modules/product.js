/* eslint-disable prettier/prettier */
import { productList, productArticle } from "@/api/product";
import { categoryList } from "@/api/category";

export default {
  state: {
    productData: {
      count: 0,
      next_page: null,
      prev_page: null,
      results: [],
    },
    filter: [],
    categories: [],
    product: {
      id: null,
      name: null,
      description: null,
      price: null,
      images: null,
      categories: null,
      rating: null,
    },
  },
  getters: {
    getProductsList(state) {
      return state.productData;
    },
    getProduct(state) {
      return state.product;
    },
    getFilter(state) {
      return state.filter;
    },
    getCategories(state) {
      return state.categories;
    },
  },
  mutations: {
    SET_PRODUCT_DATA(state, productData) {
      state.productData = productData;
    },
    SET_PRODUCT_DATA_FIELD(state, { field, value }) {
      state.productData[field] = value;
    },
    SET_PRODUCT(state, product) {
      state.product = product;
    },
    SET_FILTER(state, filter) {
      state.filter = filter;
    },
    SET_CATEGORIES(state, categories) {
      state.categories = categories;
    }
  },
  actions: {
    async fetchProducts({ commit, state }) {
      try {
        const response = await productList(state.filter.join(", "));
        commit("SET_PRODUCT_DATA", response.product);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchCategories({ commit }) {
      try {
        const response = await categoryList();
        commit("SET_CATEGORIES", response.category);
      } catch (error) {
        console.log(error);
      }
    },
    async fetchSingleProduct({ commit }, id) {
      try {
        const response = await productArticle(id);
        commit("SET_PRODUCT", response.product);
      } catch (error) {
        console.log(error);
      }
    },
  },
  computed: {
    filterWatcher() {
      return this.$store.watch(
        (state) => state.filter,
        () => {
          this.$store.dispatch("fetchProducts");
        }
      );
    },
  },
};
