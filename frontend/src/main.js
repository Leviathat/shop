import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

// add this
import "./index.css";

createApp(App).use(store).use(router, axios).mount("#app");
