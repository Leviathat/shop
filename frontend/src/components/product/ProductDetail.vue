<!-- eslint-disable prettier/prettier -->
<template>
    <div class="mt-20" v-if="product.id">

        <div class="w-3/4 h-full bg-zinc-200 mx-auto flex flex-col md:flex-row">
            <div class="h-full w-full sm:w-1/2  relative p-5 sm:p-10">
                <div class="w-1/3 absolute h-full z-30 left-0 top-0" @click="prevIndex"></div>
                <div class="w-1/3 absolute h-full z-30 right-0 top-0" @click="nextIndex"></div>

                <div class="flex flex-row h-full relative" v-if="product.images.length > 0">
                    <div v-for="(image, index) in product.images" :key="image"
                        class="w-full h-full duration-500 drop-shadow-2xl"
                        :class="{ '-translate-x-full opacity-0 absolute': index !== currentImageIndex }">
                        <img :src="image.image.replace('http://', 'https://')" alt="Abstract Design"
                            class="h-full w-full object-cover" />
                    </div>
                </div>
                <div v-else class="h-full w-full">
                    <img src="/default.webp" alt="Default image" class="h-full w-full object-cover">
                </div>

                <div class="absolute flex justify-center w-full left-0 py-2 sm:py-4">
                    <button class="h-1 w-14 mx-1" v-for="(images, index) in product.images"
                        :class="{ 'bg-zinc-900': index === currentImageIndex, 'bg-zinc-500': index !== currentImageIndex }"
                        :key="index" @click="setCurrentIndex(index)">
                    </button>
                </div>
            </div>
            <div class="min-h-full w-full bg-zinc-800 md:w-1/2 sm: p-5 sm:p-10">
                <div class="w-full h-full mx-auto sm:">
                    <div class="h-full flex flex-col justify-between">
                        <div class="flex flex-col">

                            <div class="flex justify-between">

                                <p class="text-zinc-100 text-xl md:text-2xl font-bold capitalize">
                                    {{ product.name }}
                                </p>

                            </div>

                            <!-- PRICE -->
                            <div class="flex flex-row">
                                <span class="text-blue-600 text-xl md:text-2xl font-semibold">₸ {{ product.price
                                    / 1
                                }}</span>

                                <span class="text-zinc-500 ml-2 text-lg md:text-xl font-semibold line-through align-top">₸
                                    {{ product.price / 1 }}</span>

                            </div>

                            <!-- CATEGORIES -->
                            <div class="max-w-1/3 mt-1 md:mt-4 flex flex-row">
                                <p class="text-base md:text-xl font-semibold">
                                    <span class="text-zinc-100 mr-2">Категории:
                                    </span>
                                    <span v-for="category in product.categories" :key="category.name"
                                        class="text-zinc-200 border-b-2 py-1 border-zinc-200 mr-2">
                                        {{ category.name }}
                                    </span>
                                </p>
                            </div>

                            <!-- SIZES -->
                            <div class="flex flex-col mt-1">
                                <span class="text-base md:text-xl font-semibold text-zinc-100">Размеры: </span>
                                <div class="flex flex-row">
                                    <p>
                                        <span v-for="size in product.sizes" :key="size.name"
                                            class="text-sm md:text-base font-semibold mr-2 p-1 border-b-2 border-yellow-200 font-sans text-zinc-200">
                                            {{ size.name }}
                                        </span>
                                    </p>
                                </div>
                            </div>

                            <!-- DESCRIPTION-->
                            <div class="flex flex-col">

                                <p
                                    class="sm:hidden text-zinc-100 text-base md:text-xl font-semibold capitalize mt-1 md:mt-5">
                                    <span v-if="showLess" @click="showMore" class="text-zinc-400">
                                        {{ excerpt }}...
                                    </span>
                                    <span v-else @click="showMore">
                                        {{ product.description }}
                                    </span>
                                </p>
                                <p
                                    class="hidden sm:block text-zinc-100 text-base md:text-xl font-semibold capitalize mt-1 md:mt-5">
                                    {{ product.description }}</p>
                            </div>
                        </div>
                        <div class="flex flex-col mt-5">
                            <div class="flex w-full">
                                <button type="button" @click.prevent="this.$parent.addToCart(product)"
                                    :disabled="!product.in_stock"
                                    class="text-zinc-100 w-5/6 md:w-1/2 mx-auto hover:bg-zinc-100 bg-zinc-900 duration-300 hover:text-zinc-900 focus:outline-none font-semibold font-sans px-5 py-2">
                                    <span class=" text-center inline-flex items-center align-bottom">
                                        <svg aria-hidden="true" class="w-5 h-5 mr-2 -ml-1" fill="currentColor"
                                            viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                            <path
                                                d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z">
                                            </path>
                                        </svg>
                                        Добавить
                                    </span>
                                </button>
                            </div>
                            <div class="hidden w-full sm:justify-between md:flex mt-5">
                                <span class="text-sm text-gray-500 sm:text-center dark:text-gray-400">© 2023
                                    <router-link to="/" class="hover:underline">
                                        SSWTSK
                                    </router-link> All rights reserved
                                </span>
                                <div class="flex mt-4 space-x-6 sm:justify-center sm:mt-0">
                                    <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                            <path fill-rule="evenodd"
                                                d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"
                                                clip-rule="evenodd" />
                                        </svg>
                                        <span class="sr-only">Facebook page</span>
                                    </a>
                                    <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                            <path fill-rule="evenodd"
                                                d="M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z"
                                                clip-rule="evenodd" />
                                        </svg>
                                        <span class="sr-only">Instagram page</span>
                                    </a>
                                    <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                            <path
                                                d="M8.29 20.251c7.547 0 11.675-6.253 11.675-11.675 0-.178 0-.355-.012-.53A8.348 8.348 0 0022 5.92a8.19 8.19 0 01-2.357.646 4.118 4.118 0 001.804-2.27 8.224 8.224 0 01-2.605.996 4.107 4.107 0 00-6.993 3.743 11.65 11.65 0 01-8.457-4.287 4.106 4.106 0 001.27 5.477A4.072 4.072 0 012.8 9.713v.052a4.105 4.105 0 003.292 4.022 4.095 4.095 0 01-1.853.07 4.108 4.108 0 003.834 2.85A8.233 8.233 0 012 18.407a11.616 11.616 0 006.29 1.84" />
                                        </svg>
                                        <span class="sr-only">Twitter page</span>
                                    </a>
                                    <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                            <path fill-rule="evenodd"
                                                d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
                                                clip-rule="evenodd" />
                                        </svg>
                                        <span class="sr-only">GitHub account</span>
                                    </a>
                                    <a href="#" class="text-gray-500 hover:text-gray-900 dark:hover:text-white">
                                        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                                            <path fill-rule="evenodd"
                                                d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10c5.51 0 10-4.48 10-10S17.51 2 12 2zm6.605 4.61a8.502 8.502 0 011.93 5.314c-.281-.054-3.101-.629-5.943-.271-.065-.141-.12-.293-.184-.445a25.416 25.416 0 00-.564-1.236c3.145-1.28 4.577-3.124 4.761-3.362zM12 3.475c2.17 0 4.154.813 5.662 2.148-.152.216-1.443 1.941-4.48 3.08-1.399-2.57-2.95-4.675-3.189-5A8.687 8.687 0 0112 3.475zm-3.633.803a53.896 53.896 0 013.167 4.935c-3.992 1.063-7.517 1.04-7.896 1.04a8.581 8.581 0 014.729-5.975zM3.453 12.01v-.26c.37.01 4.512.065 8.775-1.215.25.477.477.965.694 1.453-.109.033-.228.065-.336.098-4.404 1.42-6.747 5.303-6.942 5.629a8.522 8.522 0 01-2.19-5.705zM12 20.547a8.482 8.482 0 01-5.239-1.8c.152-.315 1.888-3.656 6.703-5.337.022-.01.033-.01.054-.022a35.318 35.318 0 011.823 6.475 8.4 8.4 0 01-3.341.684zm4.761-1.465c-.086-.52-.542-3.015-1.659-6.084 2.679-.423 5.022.271 5.314.369a8.468 8.468 0 01-3.655 5.715z"
                                                clip-rule="evenodd" />
                                        </svg>
                                        <span class="sr-only">Dribbble account</span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div v-if="!product.in_stock"
            class="mt-5 w-3/4 md:w-1/3 mx-auto bg-rose-500 flex flex-col justify-center items-center py-4">
            <span class="font-semibold font-sans text-zinc-100">
                Распродан
            </span>
        </div>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>

export default {
    name: "ProductDetail",
    props: {
        product: Object,
    },
    data() {
        return {
            showLess: true,
            currentImageIndex: 0,
        }
    },
    computed: {
        excerpt() {
            return this.product.description.slice(0, 100);
        },
        imagesArrayLength() {
            return this.product.images.length - 1
        },
    },
    methods: {
        showMore() {
            this.showLess = !this.showLess;
        },
        setCurrentIndex(index) {
            this.currentImageIndex = index;
        },
        nextIndex() {
            if (this.currentImageIndex < this.imagesArrayLength) {
                this.currentImageIndex++;
            }
            else {
                this.currentImageIndex = 0
            }
        },
        prevIndex() {
            if (this.currentImageIndex > 0) {
                this.currentImageIndex--;
            }
            else {
                this.currentImageIndex = this.imagesArrayLength
            }
        },
    }
};
</script>
<!-- eslint-disable prettier/prettier -->
<style>
.slider-container {
    display: flex;
    justify-content: center;
    align-items: center;
}

.slider {
    width: 100%;
    overflow: hidden;
}

.slides {
    display: flex;
    transition: transform 0.5s ease-in-out;
}

.slide {
    flex-shrink: 0;
    width: 100%;
}

.slide-image {
    width: 100%;
    height: auto;
}

.controls {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 1rem;
}

.prev-button,
.next-button {
    border: none;
    background-color: transparent;
    font-size: 1rem;
    font-weight: bold;
    cursor: pointer;
}

.prev-button:disabled,
.next-button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}
</style>