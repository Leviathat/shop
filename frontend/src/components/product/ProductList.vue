<!-- eslint-disable prettier/prettier -->
<template>
  <div class="my-10">
    <div
      class="w-3/4 mx-auto grid grid-flow-row gap-8 text-neutral-600 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 place-content-center"
      v-if="productsData"
    >
      <div
        class="bg-zinc-200 w-full rounded-xl drop-shadow-sm hover:drop-shadow-2xl duration-200 overflow-hidden max-w-xs order-first lg:order-none m-auto"
        v-for="obj in productsData.results"
        :key="obj.id"
      >
        <router-link :to="'/product/' + obj.id">
          <div
            v-if="obj.images.length !== 0"
            class="w-full h-2/3 cursor-pointer"
          >
            <img
              :src="obj.images[0].image"
              alt="Abstract Design"
              class="w-full h-full object-cover aspect-square"
            />
          </div>
          <div v-else class="bg-zinc-200 w-full h-2/3 cursor-pointer">
            <img
              src="/default.webp"
              alt="Default image"
              class="w-full h-full object-cover aspect-square"
            />
          </div>
          <div class="py-4 px-4 pt-1 max-h-1/3">
            <div class="w-full flex flex-row justify-between">
              <div class="flex flex-row">
                <span class="text-xl text-gray-800 font-semibold uppercase">
                  {{ obj.name }}
                </span>
              </div>
            </div>
            <div class="w-full flex flex-row justify-between">
              <span
                v-for="category in obj.categories"
                :key="category.id"
                class="align-bottom text-sm text-gray-400 font-semibold uppercase"
              >
                {{ category.name }}
              </span>
            </div>
            <div class="w-full flex flex-row justify-between">
              {{ obj.description.slice(0, 50) }}...
            </div>
            <div class="w-full flex flex-row justify-between">
              <div class="flex flex-row">
                <span
                  class="text-xl text-gray-800 font-semibold self-center uppercase"
                >
                  ₸ {{ obj.price / 1 }}
                </span>
              </div>
              <!-- CART -->
              <div class="flex items-center">
                <button
                  type="button"
                  @click.prevent="addToCart(obj)"
                  class="text-gray-900 bg-white hover:bg-zinc-900 duration-300 hover:text-zinc-100 focus:outline-none rounded-lg text-sm font-semibold font-sans px-5 py-2"
                >
                  Добавить
                </button>
              </div>
            </div>
            <span class=""></span>
          </div>
        </router-link>
      </div>
    </div>
  </div>
  <product-pagination
    v-if="productsData"
    :count="productsData.count"
    :next="productsData.next"
    :previous="productsData.previous"
  />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import ProductPagination from "./ProductPagination.vue";

export default {
  name: "ProductList",
  components: {
    ProductPagination,
  },
  computed: {
    cart: {
      get() {
        return this.$store.getters.getCartObject;
      },
    },
    productsData: {
      get() {
        return this.$store.getters.getProductsList;
      },
    },
  },
  methods: {
    async addToCart(product) {
      await this.$store.dispatch("addProductToCart", product);
    },
  },
  async created() {
    await this.$store.dispatch("fetchProducts");
    this.$store.dispatch("Loaded", true);
  },
};
</script>
