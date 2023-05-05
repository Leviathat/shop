<!-- eslint-disable prettier/prettier -->
<template>
    <div class="min-h-screen">
        <base-navbar />
        <cart-icon />
        <cart-count />
        <div class="w-full py-10">
            <order-list :orders="orders" />
        </div>
    </div>
    <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import BaseNavbar from "@/components/base/BaseNavbar.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";
import OrderList from "@/components/order/OrderList.vue";
import CartIcon from "@/components/cart/CartIcon.vue";
import CartCount from "@/components/cart/CartCount.vue";

export default {
    name: "OrderView",
    components: {
        BaseNavbar,
        FooterComponent,
        CartIcon,
        CartCount,
        OrderList,
    },
    computed: {
        orders: {
            get() {
                return this.$store.getters.getOrderList;
            },
        },
    },
    methods: {
    },
    async created() {
        await this.$store.dispatch("orderList");
    },
};
</script>
