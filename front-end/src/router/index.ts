import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RegisterView from "@/views/RegisterView.vue";
import LoginView from "@/views/LoginView/index.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/userRegister",
      name: "User Register",
      component: RegisterView,
      meta: {
        requiredNone: true,
      },
    },
    {
      path: "/login",
      name: "Login",
      component: LoginView,
      meta: {
        requiredNone: true,
      },
    },
  ],
});

export default router;
