<template>
    <div class="user-container">
        <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/user/' }">Personal Information</el-breadcrumb-item>
            <el-breadcrumb-item :to="{path: '/user/postHistory'}">Post History</el-breadcrumb-item>
            <el-breadcrumb-item :to="{path: '/user/commentHistory'}">Comment History</el-breadcrumb-item>
            <el-breadcrumb-item>活动详情</el-breadcrumb-item>
        </el-breadcrumb>
        <router-view/>
    </div>
</template>

<script>
import PersonInformation from "@/page/user/personInformation.vue"
import PostHistory from "@/page/user/postHistory.vue"
import CommentHistory from "./commentHistory.vue";

export default {
    name: "index",
    components: {CommentHistory, PostHistory, PersonInformation},
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