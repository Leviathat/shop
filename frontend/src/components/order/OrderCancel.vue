<!-- eslint-disable prettier/prettier -->
<template>
    <div class="hover:scale-125 duration-200" @click="cancelOrder">
        <svg width="24" height="24" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink" fill="currentColor" stroke="currentColor">
            <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
            <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round" stroke="#CCCCCC"
                stroke-width="3.072"></g>
            <g id="SVGRepo_iconCarrier">
                <title>cancel</title>
                <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                    <g id="work-case" fill="currentColor" transform="translate(91.520000, 91.520000)">
                        <polygon id="Close"
                            points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                        </polygon>
                    </g>
                </g>
            </g>
        </svg>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
    name: "OrderCancel",
    props: ["id"],
    methods: {
        async cancelOrder() {
            if (confirm("Вы точно хотите отменить заказ ?")) {
                await this.$store.dispatch("cancelOrder", this.id);
                await this.$store.dispatch("orderList");
            }
        }
    }
};
</script>
