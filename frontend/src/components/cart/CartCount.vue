<!-- eslint-disable prettier/prettier -->
<template>
    <div class="absolute">
        {{ count }}
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
    name: "CartCount",
    computed: {
        count: {
            get() {
                return this.$store.getters.getCartCount;
            },
        },
    },
};
</script>