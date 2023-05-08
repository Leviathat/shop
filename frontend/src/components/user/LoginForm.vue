<!-- eslint-disable prettier/prettier -->
<template>
    <div class="flex flex-col w-full">
        <span class="text-2xl text-center font-sans font-bold my-10">С возвращением!</span>
        <form class="font-semibold flex flex-col justify-center" @submit.prevent="onSubmit">
            <div class="relative z-0 w-full mb-6 group">
                <input type="tel" pattern="7[0-9]{10}" name="floating_phone" id="floating_phone"
                    class="rounded-none block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=" " v-model="userData.phone_number" required />
                <label for="floating_phone"
                    class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
                    Номер телефона</label>
            </div>
            <div class="relative z-0 w-full mb-6 group">
                <input type="password" name="floating_password" id="floating_password"
                    class="rounded-none block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
                    placeholder=" " v-model="userData.password" required />
                <label for="floating_password"
                    class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
                    Пароль
                </label>
            </div>
            <button type="submit"
                class="text-white duration-300 bg-blue-700 hover:bg-blue-900 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                Войти
            </button>
        </form>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
    name: "LoginForm",
    data() {
        return {
            userData: {
                phone_number: null,
                password: null,
            },
        };
    },
    methods: {
        onSubmit() {
            const data = {
                'user': this.userData
            }
            this.$store.dispatch("login", data);
        },
    },
};
</script>
