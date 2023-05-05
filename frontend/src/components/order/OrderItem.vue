<!-- eslint-disable prettier/prettier -->
<template>
    <div class="w-full flex flex-col cursor-pointer">
        <div class="flex z-30 text-center">
            <div class="px-2">
                <pre class="font-sans font-semibold"
                    :class="{ 'text-orange-500': order.status === 5, 'text-emerald-500': order.status === 4, }">{{ order.status_display }}</pre>
            </div>
            <div class="w-full text-left px-2">
                ₸ {{ order.total_amount }}
            </div>
            <div class="w-full text-right px-2">
                {{ created_at }}
            </div>
            <order-cancel :id="order.id" v-show="order.status !== 5" />
        </div>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import OrderCancel from "./OrderCancel.vue";
import moment from "moment";
import "moment/locale/ru";

export default {
    name: "OrderItem",
    props: ["order"],
    components: {
        OrderCancel,
    },
    computed: {
        created_at() {
            moment.locale("ru");
            const dateString = "2023-05-03T14:55:48.452111Z";
            const result = moment(dateString).fromNow();
            return result;
        },
    },
};
</script>
