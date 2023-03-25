<template>
  <div class="dv-login-box">
    <span>
      <router-link :to="{ name: 'Home' }" class="dv-back-home">
        <el-icon><HomeFilled /></el-icon> 返回首页
      </router-link>
    </span>
    <h1 style="text-align: center; color: #58585b">用户登录</h1>
    <el-divider />
    <div class="dv-form-box">
      <el-form label-position="right" label-width="50px" :model="loginInfo">
        <el-form-item label="账号">
          <el-input
            v-model="loginInfo.uname"
            placeholder="请输入用户账号"
            prefix-icon="UserFilled" />
        </el-form-item>
        <div style="padding: 5px"></div>
        <el-form-item label="密码">
          <el-input
            v-model="loginInfo.upwd"
            placeholder="请输入密码"
            show-password
            prefix-icon="Lock" />
        </el-form-item>
      </el-form>
    </div>
    <div style="text-align: center; margin-top: 50px">
      <el-button type="primary">登 录</el-button>
    </div>
  </div>
</template>

<script setup>
import { reactive } from "vue"

const loginInfo = reactive({
  uname: "",
  upwd: "",
})
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
