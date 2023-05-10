<!-- eslint-disable prettier/prettier -->
<template>
    <div class="mt-20">
        <div class="w-2/3 mx-auto">
            <div class="w-full flex mx-auto space-x-4 justify-center">
                <button v-if="previous" @click="fetchProducts(prev_page)"
                    class="rounded sm:cursor-pointer focus:bg-zinc-900 focus:text-zinc-100 duration-300 inline-flex items-center align-top p-1 px-2 space-x-2">
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                    <span>Previous</span>
                </button>
                <button v-if="next" @click="fetchProducts(next_page)"
                    class="rounded sm:cursor-pointer focus:bg-zinc-900 focus:text-zinc-100 duration-300 inline-flex items-center align-top p-1 px-2 space-x-2">
                    <span>Next</span>
                    <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
                            clip-rule="evenodd"></path>
                    </svg>
                </button>
            </div>
        </div>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
    name: "ProductPagination",
    props: ['count', 'next', 'previous'],
    methods: {
        async fetchProducts(page) {
            await this.$store.dispatch("fetchProducts", page);
            this.$store.dispatch("smoothScrool");
        }
    },
    computed: {
        next_page() {
            const url = new URL(this.next);
            const page = url.searchParams.get('page');
            return parseInt(page);
        },
        prev_page() {
            const url = new URL(this.previous);
            const page = url.searchParams.get('page');
            return parseInt(page);
        }
    }
};
</script>