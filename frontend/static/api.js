const safeMethod = ["get", "head", "options"]

// 构造axios实例
const service = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 5000,
})

// 请求拦截器
service.interceptors.request.use(
  (request) => {
    if (safeMethod.includes(request.method)) {
      return request
    }
    // 判断是否登录 或者 token是否过期 或者 添加headers .......
    return request
  },
  (error) => {
    return Promise.reject(error) // 返回错误信息
  }
)
