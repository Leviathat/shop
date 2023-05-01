<!-- eslint-disable prettier/prettier -->
<template>
  <header-contact />
  <header-navbar />
  <div class="w-3/4 mx-auto">
    <div class="w-full text-center py-10 ">
      <span class="font-semibold text-2xl border-zinc-900 border-b-4">SISCCO</span>
      <div class="flex flex-col">
        <span class="font-semibold text-xl text-zinc-800 py-2">Atabekov Daulet</span>
        <span class="font-semibold text-xl text-zinc-800 py-2">Bekdair Edyge</span>
        <span class="font-semibold text-xl text-zinc-800 py-2">Mukanov Murager</span>
      </div>
    </div>
  </div>
  <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import HeaderContact from "@/components/base/HeaderContact.vue";
import HeaderNavbar from "@/components/base/HeaderNavbar.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";

export default {
  name: "AboutView",
  components: {
    HeaderContact,
    HeaderNavbar,
    FooterComponent,
  },
};
</script>
