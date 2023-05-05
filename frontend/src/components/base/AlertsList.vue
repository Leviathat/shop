<!-- eslint-disable prettier/prettier -->
<template>
  <div class="fixed z-50 sm:right-5 right-8 top-10">
    <div v-for="(alert, index) in alerts" :key="index" :id="'alert-' + alert.id" class="py-2 px-4 rounded-md mb-4">
      <alert-item :type="alert.type" :message="alert.message" :id="alert.id" />
    </div>
  </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
import AlertItem from './AlertItem.vue';

export default {
  name: "AlertsList",
  components: {
    AlertItem
  },
  computed: {
    alerts: {
      get() {
        return this.$store.getters.getAlerts;
      },
    }
  },
};
</script>
