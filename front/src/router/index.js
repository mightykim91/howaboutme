import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import accountPageRouter from "@/router/modules/account.js";
import mainPageRouter from "@/router/modules/main.js";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {  
    path: "/main",
    name: "All",
    component: () => import("@/views/router-views/WithNavbar.vue"), 
    children: mainPageRouter,
  },
  {
    path: "/user",
    name: "User",
    component: () => import("@/App.vue"), 
    children: accountPageRouter,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
