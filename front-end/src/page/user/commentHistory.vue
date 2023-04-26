<template>
    <el-tabs type="border-card">
        <el-tab-pane label="Blog Comment">
            <blog-comment/>
        </el-tab-pane>
        <el-tab-pane label="Music Comment">
            <music-comment/>
        </el-tab-pane>
        <el-tab-pane label="角色管理">角色管理</el-tab-pane>
        <el-tab-pane label="定时任务补偿">定时任务补偿</el-tab-pane>
    </el-tabs>
</template>

<script>
import Tabs from "../../base/tabs.vue";
import BlogComment from "./comment/blogComment.vue";
import MusicComment from "./comment/musicComment.vue";

export default {
    name: "commentHistory",
    components: {MusicComment, BlogComment, Tabs},
    data() {
        return {
            tabs: [
                {
                    title: 'Blog Comment History',
                    key: 'blogCommentHistory',
                    to: 'blogCommentHistory'
                },
                {
                    title: 'Music Comment History',
                    key: 'musicCommentHistory',
                    to: 'musicCommentHistory'
                }
            ]
        }
    }
}
</script>

<style scoped>

</style>