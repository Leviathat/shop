<!-- eslint-disable prettier/prettier -->
<template>
    <!-- MAKING ORDER-->
    <div class="sm:w-1/3 mx-auto p-5 bg-zinc-100">
        <form class="font-semibold flex flex-col justify-center" @submit.prevent="makeOrder">
            <button type="submit"
                class="text-white duration-300 bg-blue-700 hover:bg-blue-900 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Оформить заказ
            </button>
        </form>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import router from "@/router";

export default {
    name: "NewOrder",
    props: ['cart'],
    computed: {
        total_amount: {
            get() {
                return this.cart.reduce((total, product) => {
                    return total + (parseFloat(product.price) * product.quantity);
                }, 0);
            }
        },
        products: {
            get() {
                return this.cart.map(({ id, quantity }) => ({ product: id, quantity }));
            }
        },
        order: {
            get() {
                return this.$store.getters.getOrder
            },
            set(value) {
                this.$store.commit("SET_ORDER", value)
            }
        },
        is_auth() {
            return this.$store.getters.getUser ? true : false
        }
    },
    methods: {
        async makeOrder() {
            if (!this.is_auth) {
                router.push("/login");
            }
            const orderObj = {
                "total_amount": this.total_amount,
                "products": this.products
            }
            this.order = orderObj
            await this.$store.dispatch("postOrder")
        },
    },
};
</script>
