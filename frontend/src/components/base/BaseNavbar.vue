<!-- eslint-disable prettier/prettier -->
<template>
    <header-contact />
    <header-navbar />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import HeaderContact from "@/components/base/HeaderContact.vue";
import HeaderNavbar from "@/components/base/HeaderNavbar.vue";

export default {
    name: "BaseNavbar",
    components: {
        HeaderContact,
        HeaderNavbar,
    },
};
</script>