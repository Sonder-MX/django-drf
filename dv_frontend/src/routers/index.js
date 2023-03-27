import { createRouter, createWebHistory } from "vue-router"
import { msgTips, useLoginStore } from "../stores"

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/UserLogin.vue"),
  },
  {
    path: "/ulist",
    name: "UserList",
    component: () => import("../views/UserList.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/ucenter",
    name: "UserCenter",
    component: () => import("../views/UserCenter.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/about",
    name: "About",
    component: () => import("../views/About.vue"),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    // 判断是否登录
    const loginStore = useLoginStore()
    if (loginStore.isLogin) {
      next()
    } else {
      next({
        path: "/login",
        // query: { redirect: to.fullPath },
      })
      msgTips("请登录后重试！", "error", 2600)
    }
  } else {
    next()
  }
})

export default router
