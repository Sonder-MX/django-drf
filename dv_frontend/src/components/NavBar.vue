<template>
  <el-menu :default-active="activeIndex" mode="horizontal" :router="true" :ellipsis="false">
    <el-menu-item index="/">
      <el-icon><HomeFilled /></el-icon> Home
    </el-menu-item>
    <el-menu-item index="/ulist">
      <el-icon><List /></el-icon> User-List
    </el-menu-item>
    <el-menu-item index="/about">
      <el-icon><ChromeFilled /></el-icon> About
    </el-menu-item>
    <div class="flex-grow" />
    <el-menu-item v-if="!loginStore.isLogin" index="/login">
      <el-button type="primary" size="large">
        <el-icon><Promotion /></el-icon> 登 录
      </el-button>
    </el-menu-item>
    <el-menu-item v-else index="/ucenter">
      <el-icon><Avatar /></el-icon> Hi~{{ loginStore.username }}
    </el-menu-item>
  </el-menu>
</template>

<script setup>
import { onBeforeMount, ref } from "vue"
import { useRoute } from "vue-router"
import { useLoginStore } from "../stores"

const route = useRoute()
const loginStore = useLoginStore()
let activeIndex = ref("")

onBeforeMount(() => {
  activeIndex.value = route.path
})
</script>

<style>
.flex-grow {
  flex-grow: 1;
}
</style>
