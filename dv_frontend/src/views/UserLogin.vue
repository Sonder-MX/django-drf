<template>
  <div
    class="dv-login-box"
    v-loading="loginInfo.loading"
    element-loading-background="rgba(252, 252, 252, 0.5)">
    <span>
      <router-link :to="{ name: 'Home' }" class="dv-back-home">
        <el-icon><HomeFilled /></el-icon> 返回首页
      </router-link>
    </span>
    <h1 style="text-align: center; color: #58585b">用户登录</h1>
    <el-divider />
    <div class="dv-form-box">
      <el-form
        label-position="right"
        label-width="50px"
        ref="ruleFormRef"
        :model="loginInfo"
        :rules="formRules"
        :hide-required-asterisk="true">
        <el-form-item label="账号" prop="uname">
          <el-input
            v-model.trim="loginInfo.uname"
            placeholder="请输入用户账号"
            prefix-icon="UserFilled" />
        </el-form-item>
        <div style="padding: 5px"></div>
        <el-form-item label="密码" prop="upwd">
          <el-input
            v-model.trim="loginInfo.upwd"
            placeholder="请输入密码"
            show-password
            prefix-icon="Lock" />
        </el-form-item>
      </el-form>
    </div>
    <div style="text-align: center; margin-top: 50px">
      <el-button type="primary" @click="loginSubmit(ruleFormRef)">登 录</el-button>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from "vue"
import { useRouter } from "vue-router"
import { useLoginStore } from "../stores"

const router = useRouter()
const loginStore = useLoginStore()
const ruleFormRef = ref(null)
const loginInfo = reactive({
  uname: "",
  upwd: "",
  loading: false,
})
const formRules = reactive({
  uname: [
    { required: true, message: "请输入用户名", trigger: "blur" },
    { min: 4, max: 10, message: "长度在 4 到 10 个字符", trigger: "blur" },
  ],
  upwd: [
    { required: true, message: "请输入密码", trigger: "blur" },
    { min: 8, max: 16, message: "长度在 8 到 16 个字符", trigger: "blur" },
  ],
})

const loginSubmit = (formEl) => {
  if (!formEl) return
  formEl.validate((valid) => {
    if (valid) {
      loginInfo.loading = true
      loginStore.login(loginInfo.uname, loginInfo.upwd)
      setTimeout(() => {
        loginInfo.loading = false
        if (loginStore.isLogin) {
          router.push({ name: "Home" })
        } else {
          loginInfo.upwd = ""
        }
      }, 300)
    }
  })
}
</script>

<style scoped>
.dv-login-box {
  width: 500px;
  height: 350px;
  padding: 10px;
  border-radius: 8px;
  border: 2px solid #00000049;
  box-shadow: 8px 8px 2px 1px rgba(0, 0, 0, 0.2);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.dv-form-box {
  margin-top: 42px;
}

.el-button {
  padding: 0 40px;
}

.dv-back-home {
  color: #39393a;
  text-decoration: none;
}
</style>
