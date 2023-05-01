<!-- eslint-disable prettier/prettier -->
<template>
    <div class="flex flex-col" v-if="user">
        <button type="button" @click="show_dropdown"
            class="flex mr-3 text-sm bg-gray-800 rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300"
            id="user-menu-button" aria-expanded="false" data-dropdown-toggle="user-dropdown"
            data-dropdown-placement="bottom">
            <img class="w-8 h-8 rounded-full" src="@/assets/profile.png" alt="user photo" />
        </button>
        <!-- Dropdown menu -->
        <div class="z-40 bg-white my-4 text-base list-none divide-y divide-gray-100 rounded-lg shadow-2xl md:w-64 absolute top-12 right-0 font-semibold"
            :class="{ hidden: dropdown_hidden }" id="user-dropdown">
            <div class="px-4 py-3">
                <router-link to="/">
                    <span class="block text-sm text-gray-900">{{ full_name }}</span>
                    <span class="block text-sm text-gray-500 truncate">{{ user.email }}</span>
                </router-link>
            </div>
            <ul class="py-2" aria-labelledby="user-menu-button">
                <li>
                    <router-link to="/">
                        <span class="block px-4 py-2 text-sm text-gray-900 hover:bg-gray-300 duration-200">
                            Настройки
                        </span>
                    </router-link>
                </li>
                <li class="cursor-pointer">
                    <span @click="logout" class="block px-4 py-2 text-sm text-gray-900 hover:bg-gray-300 duration-200">
                        Выйти
                    </span>
                </li>
            </ul>
        </div>
    </div>
    <div v-else>
        <router-link to="/login"
            class="flex mr-3 text-sm bg-gray-800 rounded-full md:mr-0 focus:ring-4 focus:ring-gray-300">
            <img class="w-8 h-8 rounded-full" src="@/assets/profile.png" alt="user photo" />
        </router-link>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import { logoutUser } from "@/api/auth";

export default {
    name: "ProfileDropdown",
    data() {
        return {
            dropdown_hidden: true,
        }
    },
    computed: {
        user: {
            get() {
                return this.$store.getters.getUser
            }
        },
        full_name() {
            return `${this.user.last_name} ${this.user.first_name}`
        }
    },
    methods: {
        show_dropdown() {
            this.dropdown_hidden = !this.dropdown_hidden;
        },
        logout() {
            logoutUser();
        },
    },
    async created() {
        await this.$store.dispatch("info");
    },
};
</script>