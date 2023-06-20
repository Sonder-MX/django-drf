const tbodyContent = document.getElementById("tbody-content")
const loginText = document.getElementById("loginText")
let isLogin = JSON.parse(localStorage.getItem("isLogin")) || false
let acessToken = localStorage.getItem("acessToken") || ""
let refreshToken = localStorage.getItem("refreshToken") || ""
let tbodyHtml = ""

// 获取用户列表
const getUsetList = async () => {
  const resp = await service.get("user/", {
    headers: {
      Authorization: `Bearer ${acessToken}`,
    },
  })
  resp.data.forEach((userInfo) => {
    tbodyHtml += `
    <tr>
      <td>${userInfo.username || userInfo.email}</td>
      <td>${userInfo.email}</td>
    </tr>
    `
  })
  tbodyContent.innerHTML = tbodyHtml
}

// 登录
const login = () => {
  const email = document.getElementById("email").value.trim()
  const password = document.getElementById("password").value.trim()
  if (!email || !password) {
    alert("邮箱或密码不能为空")
    return
  }
  service
    .post("token/", { email, password })
    .then(({ data }) => {
      localStorage.setItem("isLogin", true)
      localStorage.setItem("acessToken", data.access)
      localStorage.setItem("refreshToken", data.refresh)
      window.location.reload()
    })
    .catch(() => {
      alert("登录失败，账号或密码错误！")
    })
}

// 注册
const register = () => {
  const email = document.getElementById("email").value.trim()
  const password = document.getElementById("password").value.trim()
  if (!email || !password) {
    alert("请输入邮箱或密码后完成注册！")
    return
  }
  service
    .post("user/", { email, password })
    .then(({ data }) => {
      window.location.reload()
      alert(`账号：${data.email} 注册成功！`)
    })
    .catch(({ response }) => {
      for (let value of Object.values(response.data)) {
        if (Array.isArray(value)) {
          alert(value[0])
        } else {
          alert(value)
        }
        break
      }
    })
}

// 退出登录
const logout = () => {
  localStorage.clear()
  window.location.reload()
}

// 检查token是否过期
const checkToken = () => {
  if (!acessToken.trim()) {
    localStorage.clear()
    alert("token不存在或已过期，请重新登录！")
    return
  }
  // token、refresh -> [header, payload, signature]
  const refreshExp = JSON.parse(atob(refreshToken.split(".")[1])).exp
  if (Math.floor(Date.now()) / 1000 >= refreshExp) {
    localStorage.clear()
    alert("登录信息已过期，请重新登录！")
    return
  }
  const tokenB64 = acessToken.split(".")[1]
  const tokenInfo = JSON.parse(atob(tokenB64))
  // console.log(tokenInfo.exp)
  if (Math.floor(Date.now()) / 1000 >= tokenInfo.exp) {
    service
      .post("token/refresh/", { refresh: refreshToken })
      .then(({ data }) => {
        localStorage.setItem("acessToken", data.access)
        acessToken = data.access
        isLogin = true
      })
      .catch(() => {
        localStorage.clear()
        window.location.reload()
        alert("获取用户token失败，请重新登录！")
      })
  }
}

// 页面加载时执行
// 判断是否登录
checkToken()
if (isLogin) {
  getUsetList() // 页面加载时获取用户列表
  const tokenB64 = acessToken.split(".")[1]
  const userName = JSON.parse(atob(tokenB64)).username
  loginText.innerHTML = `
  <span style='margin-right:8px'>你好~${userName || ""}</span>
  <a href="/pages/userinfo_update">我的信息</a>
  <button type="button" id="logoutBtn">退出登录</button>
  `
  const logoutBtn = document.getElementById("logoutBtn")
  logoutBtn.addEventListener("click", logout)
} else {
  tbodyContent.innerHTML = `<tr>
    <td colspan="2" style="text-align: center">请登录后查看</td>
  </tr>`
  loginText.innerHTML = "<div>未登录</div>"
}
