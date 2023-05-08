<!-- eslint-disable prettier/prettier -->
<template>
  <div class="min-h-screen">
    <base-navbar />
    <div class="w-3/4 mx-auto">
      <div class="w-full text-center py-10">
        <span class="font-semibold text-2xl">Contacts</span>
        <div class="flex flex-col text-left font-semibold text-xl py-10 space-y-4">
          <span>
            tg:
            <a class="py-2 text-sky-600" href="https://web.telegram.org/a/#832855518">@nemanedeushed</a>
          </span>
          <span>
            inst:
            <a class="py-2 text-rose-600" href="https://www.instagram.com/sswtsk/">@sswtsk</a>
          </span>
        </div>
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
  name: "ContactView",
  components: {
    BaseNavbar,
    FooterComponent,
  },
};
</script>
