<template>
  <div class="user-container">
    <el-tabs style="height: 200px;">
      <el-tab-pane label="Personal Information">
        <PersonInformation/>
      </el-tab-pane>
      <el-tab-pane label="Post History">
        <post-history/>
      </el-tab-pane>
      <el-tab-pane label="角色管理">角色管理</el-tab-pane>
      <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import PersonInformation from "@/page/user/personInformation.vue"
import PostHistory from "@/page/user/postHistory.vue"

export default {
  name: "index",
  components: {PostHistory, PersonInformation},
  data() {
    return {
      tabPosition: 'left'
    }
  }
}
</script>

<style scoped>
.user-container {
  padding: 18px 32px;
}
</style>