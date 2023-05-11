<!-- eslint-disable prettier/prettier -->
<template>
    <div class="sm:w-1/3 mx-auto p-5 bg-zinc-100">
        <div class="flex w-full justify-between">
            <span class="font-semibold text-xl">Сумма</span>
            <span class="font-semibold text-xl">₸ {{ total_amount }}</span>
        </div>
        <div class="flex w-full justify-between">
            <span class="font-semibold text-xl">Доставка</span>
            <span class="font-semibold text-xl">₸ {{ shipping / 1 }}</span>
        </div>
    </div>
    <!-- ORDER SUBMIT -->
    <div class="sm:w-1/3 mx-auto p-5 bg-zinc-100">
        <form class="font-semibold flex flex-col justify-center" @submit.prevent="makeOrder">
            <button type="submit"
                class="duration-300 bg-blue-700 hover:bg-blue-900 focus:ring-4 focus:outline-none focus:ring-blue-300 w-full sm:w-auto px-5 py-2.5"
                :disabled="!user">
                <span class="text-white text-center font-medium ">
                    Оформить заказ
                </span>
            </button>
        </form>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
    name: "NewOrder",
    props: ['cart', 'user'],
    computed: {
        shipping() {
            return this.total_amount * 5 / 100
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
        total_amount: {
            get() {
                return this.$store.getters.getTotal;
            }
        }
    },
    methods: {
        async makeOrder() {
            const orderObj = {
                "total_amount": this.total_amount,
                "products": this.products
            }
            this.order = orderObj
            await this.$store.dispatch("postOrder")
        },
    },
    async mounted() {
        await this.$store.dispatch("loadTotal")
    }
};
</script>
