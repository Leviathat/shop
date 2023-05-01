<!-- eslint-disable prettier/prettier -->
<template>
    <div class="w-screen mt-5" v-if="cart.length != 0">
        <!-- CART ITSELF-->
        <div class="sm:w-1/3 mx-auto p-5 bg-zinc-100">
            <div v-for="product in cart" :key="product.id"
                class="relative border-b-4 last:border-none border-zinc-300 w-full flex justify-between text-zinc-600 py-4">
                <button @click.prevent="addToCart(product)" class="z-30 absolute -translate-x-1/2 translate-y-full
                    inline-flex items-center justify-center 
                    w-7 h-7 duration-150
                    text-zinc-900
                    hover:bg-zinc-900
                    hover:text-zinc-100">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" xmlns:xlink="http://www.w3.org/1999/xlink"
                        viewBox="0 0 122.875 122.648">
                        <g>
                            <path fill="currentColor" clip-rule="evenodd"
                                d="M108.993,47.079c7.683-0.059,13.898,6.12,13.882,13.805 c-0.018,7.683-6.26,13.959-13.942,14.019L75.24,75.138l-0.235,33.73c-0.063,7.619-6.338,13.789-14.014,13.78 c-7.678-0.01-13.848-6.197-13.785-13.818l0.233-33.497l-33.558,0.235C6.2,75.628-0.016,69.448,0,61.764 c0.018-7.683,6.261-13.959,13.943-14.018l33.692-0.236l0.236-33.73C47.935,6.161,54.209-0.009,61.885,0 c7.678,0.009,13.848,6.197,13.784,13.818l-0.233,33.497L108.993,47.079L108.993,47.079z" />
                        </g>
                    </svg>
                </button>
                <div class="w-full flex pr-2">
                    <div class="w-full flex flex-row justify-between">
                        <div class="font-semibold flex">
                            <img :src="product.image.includes('http://127.0.0.1:8000') ? product.image : 'http://127.0.0.1:8000' + product.image"
                                alt="Abstract Design" class="w-20 object-cover aspect-square drop-shadow-2xl rounded-md" />
                            <div class="flex flex-col px-4 justify-between">
                                <div class="flex flex-col">
                                    <span class="text-zinc-900 uppercase">{{
                                        product.name
                                    }}</span>
                                    <span class="text-zinc-900 uppercase">{{ product.id }}</span>
                                    <span class="text-zinc-600 text-sm">{{
                                        product.category
                                    }}</span>
                                </div>
                                <div class="flex w-ful">
                                    <span class="text-green-600 text-base">x{{ product.quantity }}</span>
                                    <div class="flex items-center"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex flex-col justify-between items-center">
                    <div class="text-right">
                        <span class="text-zinc-900 font-semibold">
                            ₸ {{ product.price / 1 }}</span>
                    </div>
                    <button @click="removeToCart(product.id)"
                        class="inline-flex items-center justify-center w-8 h-8 text-pink-100 transition-colors duration-150 bg-pink-700 rounded-lg focus:shadow-outline hover:bg-pink-800">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        <new-order :cart="cart" />
    </div>
    <div v-else class="text-center w-screen h-96 flex flex-col justify-center">
        <span class="text-2xl font-semibold text-zinc-900 underline underline-offset-4">
            Корзина пуста
        </span>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import NewOrder from "@/components/order/NewOrder.vue";

export default {
    name: "CartProducts",
    components: {
        NewOrder,
    },
    computed: {
        cart: {
            get() {
                return this.$store.getters.getCartObject;
            },
        },
    },
    methods: {
        async addToCart(product) {
            await this.$store.dispatch("addProductToCart", product);
        },
        async removeToCart(productId) {
            await this.$store.dispatch("removeProductFromCart", productId);
        },
    },
};
</script>
