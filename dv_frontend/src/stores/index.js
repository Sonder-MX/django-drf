import axios from "axios"
import { ElMessage } from "element-plus"
import { defineStore } from "pinia"

export const serHttp = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  timeout: 3000,
})

export const msgTips = (msg, tp, duration = 2000) => {
  ElMessage({
    message: msg,
    type: tp,
    duration,
  })
}

export const useLoginStore = defineStore("login", {
  state: () => ({
    isLogin: localStorage.getItem("username") ? true : false,
    username: localStorage.getItem("username") || "",
    access: localStorage.getItem("access") || "",
    refresh: localStorage.getItem("refresh") || "",
    expiredTime: Number(localStorage.getItem("expired")) || 0,
  }),
  getters: {
    isExpired: (state) => new Date().getTime() / 1000 > state.expiredTime,
  },
  actions: {
    login(username, password) {
      serHttp
        .post("/token/", { username, password })
        .then((resp) => {
          this.username = username
          this.access = resp.data.access
          this.refresh = resp.data.refresh
          this.expiredTime = resp.data.expired
          this.isLogin = true
          localStorage.setItem("username", username)
          localStorage.setItem("access", resp.data.access)
          localStorage.setItem("refresh", resp.data.refresh)
          localStorage.setItem("expired", resp.data.expired)
          msgTips("登录成功！", "success")
        })
        .catch((err) => {
          if (err.response) {
            msgTips("用户名或密码错误，请检查用户名或密码后重试！", "error", 3000)
          } else {
            msgTips("网络错误！！！", "error", 3000)
          }
        })
    },
    logout() {
      localStorage.clear()
      this.$reset()
      msgTips("账号已退出！", "success")
    },
    refreshToken() {
      if (this.isExpired && this.refresh !== "") {
        serHttp.post("/token/refresh/", { refresh: this.refresh }).then((resp) => {
          this.access = resp.data.access
          this.expiredTime = resp.data.expired
          localStorage.setItem("access", resp.data.access)
          localStorage.setItem("expired", resp.data.expired)
          this.refresh = ""
          localStorage.removeItem("refresh") // 仅仅刷新access-token，refresh-token仅仅使用一次
        })
      }
      if (this.isExpired && this.refresh === "") {
        localStorage.clear()
        this.$reset()
        msgTips("登录已过期，请重新登录！", "error", 2400)
        return true
      }
    },
  },
})
