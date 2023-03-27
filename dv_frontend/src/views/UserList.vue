<template>
  <NavBar />
  <div class="table-container">
    <el-table :data="userListData" border style="width: 100%" max-height="80vh">
      <el-table-column fixed prop="id" label="ID" />
      <el-table-column prop="username" label="用户名" />
      <el-table-column label="身份" width="180">
        <template #default="{ row }">
          <span v-if="row.identity === 0" class="col-identity ordinary-user">
            <el-icon><User /></el-icon> 普通用户
          </span>
          <span v-else-if="row.identity === 1" class="col-identity ordinary-admin">
            <el-icon><EditPen /></el-icon> 普通管理员
          </span>
          <span v-else class="col-identity super-admin">
            <el-icon><Edit /></el-icon> 超级管理员
          </span>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { onBeforeMount, ref } from "vue"
import NavBar from "../components/NavBar.vue"
import { serHttp, useLoginStore } from "../stores"

const loginStore = useLoginStore()
let userListData = ref([])

onBeforeMount(async () => {
  if (loginStore.refreshToken()) {
    router.push({ name: "Login" })
  }
  const res = await serHttp.get("/user")
  userListData.value = res.data
})
</script>

<style scoped>
.table-container {
  margin: 0 10vw;
}

.col-identity {
  font-weight: bolder;
  cursor: default;
}

.ordinary-user {
  color: #409eff;
}

.ordinary-admin {
  color: #67c23a;
}

.super-admin {
  color: #f59e46;
}

.el-icon {
  vertical-align: middle;
}
</style>
