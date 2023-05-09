<!-- eslint-disable prettier/prettier -->
<template>
    <div>
        <base-navbar />
        <cart-products />
    </div>
    <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import BaseNavbar from "@/components/base/BaseNavbar.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";
import CartProducts from "@/components/cart/CartProducts.vue";

export default {
    name: "CartView",
    components: {
        BaseNavbar,
        FooterComponent,
        CartProducts,
    },
    mounted() {
        this.$store.dispatch("Loaded", true);
    },
};
</script>
