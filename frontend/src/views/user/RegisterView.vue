<!-- eslint-disable prettier/prettier -->
<template>
    <header-contact />
    <div class="w-screen py-10 mt-20">
        <div class="flex justify-center mx-auto w-64 md:w-1/4">
            <register-form />
        </div>
        <div class="flex mt-5 text-center justify-center mx-auto w-64 md:w-1/4">
            <span class="text-gray-500 w-full">
                Перейдите в
                <router-link to="/login" class="text-blue-500">личный кабинет</router-link>, если у вас уже есть аккаунт!
            </span>
        </div>
    </div>
    <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import RegisterForm from "@/components/user/RegisterForm.vue";
import HeaderContact from "@/components/base/HeaderContact.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";

export default {
    name: "RegisterView",
    components: {
        RegisterForm,
        HeaderContact,
        FooterComponent,
    },
};
</script>
