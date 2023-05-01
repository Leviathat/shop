<!-- eslint-disable prettier/prettier -->
<template>
    <base-navbar />
    <cart-icon />
    <cart-count />
    <product-detail :product="product" />
    <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import BaseNavbar from "@/components/base/BaseNavbar.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";
import ProductDetail from "@/components/product/ProductDetail.vue"
import CartIcon from "@/components/cart/CartIcon.vue";
import CartCount from "@/components/cart/CartCount.vue";

export default {
    name: "ProductView",
    components: {
        BaseNavbar,
        FooterComponent,
        ProductDetail,
        CartIcon,
        CartCount,
    },
    computed: {
        product: {
            get() {
                return this.$store.getters.getProduct;
            },
        },
    },
    methods: {
        async addToCart(product) {
            await this.$store.dispatch("addProductToCart", product);
        },
    },
    async created() {
        this.productId = this.$route.params.id;
        await this.$store.dispatch("fetchSingleProduct", this.productId);
    },
};
</script>
