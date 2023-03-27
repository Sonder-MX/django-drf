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
    isLogin: false,
    username: "",
    access: localStorage.getItem("access") || "",
    refresh: localStorage.getItem("refresh") || "",
  }),
  getters: {},
  actions: {
    login(username, password) {
      serHttp
        .post("/token/", { username, password })
        .then((resp) => {
          this.username = username
          this.access = resp.data.access
          this.refresh = resp.data.refresh
          this.isLogin = true
          localStorage.setItem("access", resp.data.access)
          localStorage.setItem("refresh", resp.data.refresh)
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
  },
})
