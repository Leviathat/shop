<!-- eslint-disable prettier/prettier -->
<template>
    <div class="w-full">
        <!--<div class="fixed top-0 left-0 w-screen h-screen z-50 bg-black/25"></div>-->
        <div class="w-5/6 sm:w-1/3 mx-auto">
            <div class="flex-col">
                <div class="w-full text-center py-4">
                    <span class="text-xl font-semibold">Ваши заказы</span>
                </div>
                <div v-if="orders.length > 0" class="flex flex-col divide-y-2">
                    <div v-for="order in orders" :key="order.id"
                        class="flex py-5 hover:bg-zinc-900 hover:text-zinc-100 duration-200">
                        <order-item :order="order" />
                    </div>
                </div>
                <div v-else class="w-full text-center py-4">
                    <span class="font-semibold text-xl text-zinc-500">Список заказов пуст..</span>
                </div>
            </div>
        </div>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import OrderItem from "./OrderItem.vue";
export default {
    name: "OrderList",
    props: ["orders"],
    components: {
        OrderItem,
    },
};
</script>
