<!-- eslint-disable prettier/prettier -->
<template>
    <div class="bg-zinc-100 relative">
        <div class="flex flex-col sm:flex-row w-1/3 justify-between mx-auto">
            <label for="status_1"
                class="font-semibold cursor-pointer p-4 hover:bg-black hover:text-white duration-300">Оформлен
                <input type="checkbox" id="status_1" class="hidden" value="1">
            </label>
            <label for="status_2"
                class="font-semibold cursor-pointer p-4 hover:bg-black hover:text-white duration-300">Оплачен
                <input type="checkbox" id="status_2" class="hidden" value="2">
            </label>
            <label for="status_3" class="font-semibold cursor-pointer p-4 hover:bg-black hover:text-white duration-300">В
                пути
                <input type="checkbox" id="status_3" class="hidden" value="3">
            </label>
            <label for="status_4"
                class="font-semibold cursor-pointer p-4 hover:bg-black hover:text-white duration-300">Доставлен
                <input type="checkbox" id="status_4" class="hidden" value="4">
            </label>
            <label for="status_5"
                class="font-semibold cursor-pointer p-4 hover:bg-black hover:text-white duration-300">Отменен
                <input type="checkbox" id="status_5" class="hidden" value="5">
            </label>
        </div>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
    name: "FilterOrder",
};
</script>
