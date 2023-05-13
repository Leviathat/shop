<!-- eslint-disable prettier/prettier -->
<template>
  <nav class="bg-zinc-200 border-gray-200 box-border ">
    <div class="max--xl flex flex-wrap max-w-screen-xl items-center justify-between mx-auto p-4">
      <router-link to="/"
        class="flex items-center duration-200 border-b-2 border-black md:border-transparent  hover:border-black">
        <span class="self-center text-2xl align-top text-zinc-900 font-semibold whitespace-nowrap">sswtsk</span>
      </router-link>
      <div class="flex items-center md:order-2 relative">
        <profile-dropdown />
        <button type="button" @click="navbar_show"
          class="inline-flex items-center p-2 ml-1 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200">
          <span class="sr-only">Open main menu</span>
          <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"></path>
          </svg>
        </button>
      </div>
      <div class="items-center justify-between w-full md:flex md:w-auto md:order-1" id="mobile-menu-2"
        :class="{ hidden: navbar_hidden }">
        <ul
          class="divide-y-2  flex flex-col text-zinc-900 font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-transparent">
          <li class="py-2 pl-3 pr-4">
            <router-link to="/catalog" class="duration-200 border-b-2 border-transparent hover:border-black">
              Каталог
            </router-link>
          </li>
          <li class="py-2 pl-3 pr-4">
            <router-link to="/contact" class="duration-200 border-b-2 border-transparent hover:border-black">
              О нас
            </router-link>
          </li>
          <li class="py-2 pl-3 pr-4">
            <router-link to="/contact" class="duration-200 border-b-2 border-transparent hover:border-black">
              Главная
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import ProfileDropdown from '@/components/user/ProfileDropdown.vue';

export default {
  name: "HeaderNavbar",
  data() {
    return {
      navbar_hidden: true,
    };
  },
  components: {
    ProfileDropdown,
  },
  methods: {
    navbar_show() {
      this.navbar_hidden = !this.navbar_hidden;
    },
  },
};
</script>
