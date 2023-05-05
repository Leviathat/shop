<template>
  <alerts-list />
  <router-view />
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import AlertsList from "@/components/base/AlertsList.vue";
export default {
  name: "App",
  components: {
    AlertsList
  }
};
</script>