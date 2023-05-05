<!-- eslint-disable prettier/prettier -->
<template>
  <div class="min-h-screen">
    <base-navbar />
    <div class="w-3/4 mx-auto">
      <div class="w-full text-center py-10 ">
        <span class="font-semibold text-2xl border-zinc-900 border-b-4">SISCCO</span>
      </div>
    </div>
  </div>
  <footer-component />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import BaseNavbar from "@/components/base/BaseNavbar.vue";
import FooterComponent from "@/components/base/FooterComponent.vue";

export default {
  name: "AboutView",
  components: {
    BaseNavbar,
    FooterComponent,
  },
};
</script>
