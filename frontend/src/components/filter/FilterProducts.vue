<!-- eslint-disable prettier/prettier -->
<template>
    <div class="bg-zinc-100 relative">
        <div @click="showCategories" class="sm:hidden w-full flex justify-center py-2 cursor-pointer">
            <span class="mx-2 inline-block align-top font-sans font-semibold">Фильтры</span>
        </div>
        <div class="w-3/4 mx-auto">
            <div class="form-control w-full flex flex-col sm:flex-row justify-between text-zinc-600"
                :class="{ 'hidden sm:flex': categoriesHidden }">
                <label v-for="category in categories" :key="category.id" class="font-sans font-semibold capitalize py-2 px-4 w-full text-center border-b-4 box-border sm:text-center mx-auto my-1 sm:my-0 sm:mx-1 cursor-pointer 
         hover:bg-zinc-200" :class="{ 'border-black text-zinc-900 bg-zinc-150': filter.includes(category.name) }">
                    <span class="">
                        {{ category.name }}
                    </span>
                    <input type="checkbox" class="checkbox hidden" v-model="filter" :value="category.name" />
                </label>

            </div>
        </div>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
    name: "FilterProducts",
    data() {
        return {
            categoriesHidden: true,
        }
    },
    computed: {
        filter: {
            get() {
                return this.$store.getters.getFilter;
            },
            set(value) {
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
    methods: {
        showCategories() {
            this.categoriesHidden = !this.categoriesHidden
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
};
</script>
