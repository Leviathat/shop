<!-- eslint-disable prettier/prettier -->
<template>
    <header-contact />
    <div class="w-screen py-10 mt-20">
        <div class="flex justify-center mx-auto w-64 md:w-1/4">
            <login-form />
        </div>
        <div class="flex mt-5 text-center justify-center mx-auto w-64 md:w-1/4">
            <span class="text-gray-500 w-full">
                Вы можете перейти по этой ссылке и <router-link to="/register"
                    class="text-blue-500">зарегистрироваться</router-link>
            </span>
        </div>
    </div>
    <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import LoginForm from "@/components/user/LoginForm.vue";
import HeaderContact from "@/components/base/HeaderContact.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";

export default {
    name: "LoginView",
    components: {
        LoginForm,
        HeaderContact,
        FooterComponent,
    },
    mounted() {
        this.$store.dispatch("Loaded", true);
    },
};
</script>
