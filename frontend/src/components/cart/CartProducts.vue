<!-- eslint-disable prettier/prettier -->
<template>
    <div v-if="!user" class="sm:w-1/3 mx-auto p-5 bg-zinc-100 text-center mt-5">
        <span class="text-xl font-semibold text-zinc-900 ">
            Вам нужно быть
            <router-link to="/login" class="text-blue-700 border-b-2 border-blue-700">
                авторизованным
            </router-link>
            , чтобы оформить заказ
        </span>
    </div>

    <div class="mt-5" v-if="cart.length != 0" :class="{ 'blur-xl': !user }">
        <!-- CART ITSELF-->
        <div class="sm:w-1/3 mx-auto p-5 bg-zinc-100">
            <div v-for="product in cart" :key="product.id"
                class="border-b-2 last:border-none border-zinc-300 w-full flex justify-between text-zinc-600 py-4">

                <div class="w-full flex pr-2">
                    <div class="w-full flex flex-row justify-between">
                        <div class="font-semibold flex  w-full">
                            <img :src="'https://notrated.duckdns.org' + product.image" alt="Abstract Design"
                                class="w-20 object-cover aspect-square drop-shadow-2xl rounded-md" />
                            <div class="flex flex-col px-4 justify-between w-full">
                                <div class="flex flex-col">
                                    <div class="inline-flex space-x-2">
                                        <span class="text-zinc-900 uppercase font-semibold">
                                            {{ product.name }}
                                        </span>
                                        <span class="text-green-600 text-base align-top">x{{ product.quantity }}</span>
                                    </div>
                                    <span class="text-zinc-600 text-sm">
                                        {{ product.category }}</span>
                                </div>
                                <div class="flex w-full justify-between">
                                    <button @click.prevent="addToCart(product)" class="z-30">
                                        <span
                                            class="font-semibold text-emerald-500 border-b-2 border-emerald-500 py-1">Добавить</span>
                                    </button>
                                    <div class="flex items-center"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="flex flex-col justify-between items-end w-full ">
                    <div class="w-full  text-right">
                        <span class="text-zinc-900 font-semibold">
                            ₸ {{ product.price / 1 }}</span>
                    </div>
                    <button @click="removeToCart(product.id)">
                        <span class="font-semibold text-rose-500 border-b-2 border-rose-500 py-1 ml-auto">Убрать</span>
                    </button>
                </div>
            </div>
        </div>
        <new-order :cart="cart" :user="user" />
    </div>
    <div v-else class="text-center h-96 flex flex-col justify-center">
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
        user: {
            get() {
                return this.$store.getters.getUser;
            }
        }
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
