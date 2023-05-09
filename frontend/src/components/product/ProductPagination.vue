<!-- eslint-disable prettier/prettier -->
<template>
    <div class="mt-20">
        <div class="w-2/3 mx-auto">
            <div class="flex flex-col">
                {{ count }}
                {{ prev_page }}
                {{ next_page }}
            </div>
        </div>
    </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>

export default {
    name: "ProductPagination",
    props: ['count', 'next_page', 'prev_page']
};
</script>