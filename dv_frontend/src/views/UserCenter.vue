<template>
  <NavBar />
  <div class="user-center">
    <el-popconfirm
      width="220"
      confirm-button-text="确定"
      cancel-button-text="取消"
      confirm-button-type="danger"
      :icon="InfoFilled"
      icon-color="#626AEF"
      title="你确定要退出码？"
      @confirm="userLogout">
      <template #reference>
        <el-button type="warning">退出登录</el-button>
      </template>
    </el-popconfirm>
  </div>
</template>

<script setup>
import { onBeforeMount } from "vue"
import { useRouter } from "vue-router"
import NavBar from "../components/NavBar.vue"
import { useLoginStore } from "../stores"

const router = useRouter()
const loginStore = useLoginStore()

const userLogout = () => {
  loginStore.logout()
  router.push({ name: "Home" })
}

onBeforeMount(() => {
  if (loginStore.refreshToken()) {
    router.push({ name: "Login" })
  }
})
</script>

<style scoped>
.user-center {
  margin: 0 10vw;
  padding: 20px;
  background-color: rgba(208, 211, 214, 0.3);
}
</style>
