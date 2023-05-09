<template>
  <alerts-list />
  <screen-loader />
  <router-view />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import AlertsList from "@/components/base/AlertsList.vue";
import ScreenLoader from "./components/base/ScreenLoader.vue";
export default {
  name: "App",
  components: {
    AlertsList,
    ScreenLoader,
  }
};
</script>