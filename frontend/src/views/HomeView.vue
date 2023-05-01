<template>
  <div class="min-h-screen">
    <base-navbar />
    <cart-icon />
    <div class="max-w-screen">
      <filter-products />
      <product-list />
    </div>
  </div>
  <footer-component />
</template>

<script>
import BaseNavbar from "@/components/base/BaseNavbar.vue";
import ProductList from "@/components/product/ProductList.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";
import FilterProducts from "@/components/filter/FilterProducts.vue";
import CartIcon from "@/components/cart/CartIcon.vue";

export default {
  name: "HomeView",
  components: {
    BaseNavbar,
    ProductList,
    FooterComponent,
    FilterProducts,
    CartIcon,
  },
};
</script>
