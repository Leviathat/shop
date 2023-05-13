import { createRouter, createWebHistory } from "vue-router";
import store from "@/store";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/views/HomeView.vue"),
  },
  {
    path: "/catalog",
    name: "catalog",
    component: () => import("@/views/CatalogView.vue"),
  },
  {
    path: "/contact",
    name: "contact",
    component: () => import("@/views/ContactView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("@/views/user/LoginView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("@/views/user/RegisterView.vue"),
  },
  {
    path: "/product/:id",
    name: "product",
    component: () => import("@/views/product/ProductView.vue"),
  },
  {
    path: "/cart/",
    name: "cart",
    component: () => import("@/views/cart/CartView.vue"),
  },
  {
    path: "/order/",
    name: "order",
    component: () => import("@/views/order/OrderView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  store.dispatch("Loaded", false);
  next();
});

export default router;
