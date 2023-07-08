<!-- eslint-disable prettier/prettier -->
<template>
  <div class="min-h-screen">
    <base-navbar />
    <div class="w-3/4 mx-auto">
      <div class="w-full text-center py-10 space-y-4">
        <span class="font-bold font-sans text-2xl">SSWTSK</span>
        <div
          class="flex flex-col items-center font-bold font-sans text-xl text-zinc-500"
        >
          <span>Any title could be written here,</span>
          <span>Any product could be posted here,</span>
          <span>Any order could be handled here</span>
        </div>
      </div>
      <div
        class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8"
      >
        <label
          v-for="category in categories"
          :key="category.id"
          class="cursor-pointer group relative flex flex-col p-5 text-zinc-100 font-sans font-semibold bg-gradient-to-br from-amber-900 to-zinc-900"
        >
          <span class="text-left uppercase z-10">
            {{ category.name }}
          </span>
          <input
            type="checkbox"
            class="checkbox hidden"
            v-model="filter"
            :value="category.name"
          />

          <div
            class="group-hover:pr-5 duration-300 inline-flex items-center align-top p-1 justify-end"
          >
            <span class="font-semibold">Next</span>
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
          </div>
          <img
            class="absolute z-0 w-full h-full object-cover top-0 left-0 opacity-25"
            :src="category.image.replace('http://', 'https://')"
            alt="Category image"
          />
        </label>
      </div>
    </div>
  </div>
  <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import BaseNavbar from "@/components/base/BaseNavbar.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";
import router from "@/router";

export default {
  name: "ContactView",
  components: {
    BaseNavbar,
    FooterComponent,
  },
  computed: {
    filter: {
      get() {
        return this.$store.getters.getFilter;
      },
      set(value) {
        router.push("/catalog");
        this.$store.commit("SET_FILTER", value);
      },
    },
    categories: {
      get() {
        return this.$store.getters.getCategories;
      },
      set(value) {
        this.$store.commit("SET_CATEGORIES", value);
      },
    },
  },
  created() {
    this.$watch(
      () => this.filter,
      () => {
        this.$store.dispatch("fetchProducts");
      }
    );
    this.$store.dispatch("fetchCategories");
  },
  mounted() {
    this.$store.dispatch("Loaded", true);
  },
};
</script>
