<template>
    <div>
        <div v-for="(item, index) in personalBlogData" :key="index" class="blog-container">
            <el-card class="blog-card" style="background-position: center">
                <div slot="header">
                    <span>{{ item.username }}:</span>
                    <el-dropdown style="float: right; padding: 3px 0">
                        <span class="el-dropdown-link">
                            Operation<i class="el-icon-arrow-down el-icon--right"></i>
                        </span>
                        <el-dropdown-menu slot="dropdown">
                            <el-dropdown-item @click.native="deletePersonalBlog(item.id)">Delete</el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                </div>
                <div class="text item" style="margin-bottom: 18px">{{ item.blog_content }}</div>
                <div class="box">
                    <div v-for="(item2,index) in item.picList" :key="index" class="imageBox">
                        <el-image
                                :src="item2"
                                style=""/>
                    </div>
                </div>
                <el-button
                        size="small"
                        style="width: 10%;float: right;color: #D33A31"
                        type="text"
                        @click="getBlogComments(item.id)"
                >Comments
                </el-button>
                <el-dialog
                        :visible.sync="commentDialogVisible"
                        title="Comments"
                        width="50%"
                >
                    <ul v-for="(item3,index) in commentData" :key="index">
                        <li>
                            {{ item3.username }}: {{ item3.content }}
                            <el-link
                                    v-if="item3.username===auth.username"
                                    @click="deletePersonalComment(item3.id, item.id)"
                            >
                                Delete
                            </el-link>
                        </li>
                    </ul>
                    <div style="display: flex">
                        <el-input v-model="addCommentData" placeholder="Comment"/>
                        <el-button @click="addBlogComment(item.id)">Send</el-button>
                    </div>
                </el-dialog>
            </el-card>
        </div>
    </div>
</template>

<script>
import {newRequest} from "../../utils";

export default {
    name: "postHistory",
    components: {},
    data() {
        return {
            auth: {
                username: this.$cookies.get('auth').username,
                userid: this.$cookies.get('auth').userid
            },
            editBlogVisible: false,
            commentData: [],
            personalBlogData: [],
            commentDialogVisible: false,
            addCommentData: '',
            editBlogForm: {
                text: '',
                picFiles: [],
                picFileNumber: []
            }
        }
    },
    methods: {
        getPersonalBlog() {
            const getPersonalBlogLoading = this.$loading({
                lock: true,
                text: 'Loading',
                spinner: 'el-icon-loading',
                background: 'rgba(0,0,0,0.7)'
            })
            newRequest.post(
                '/blog/get_user_blog',
                {
                    userid: this.$cookies.get('auth').userid
                }
            ).then(res => {
                console.log(res.data)
                this.personalBlogData = res.data
                getPersonalBlogLoading.close()
            })
        },
        deletePersonalBlog(id) {
            newRequest.post(
                '/blog/update_blog_state',
                {
                    blog_id: id,
                    state: 3
                }
            ).then(res => {
                if (res.code === 200) {
                    this.$message({
                        showClose: true,
                        type: "success",
                        message: "Delete Blog Success"
                    })
                }
            })
        },
        getBlogComments(id) {
            const getBlogCommentsLoading = this.$loading({
                lock: true,
                text: 'Loading',
                spinner: 'el-icon-loading',
                background: 'rgba(0,0,0,0.7)'
            })
            newRequest.post(
                '/blog/get_blog_comments',
                {
                    blogid: id
                }
            ).then(res => {
                console.log(res)
                getBlogCommentsLoading.close()
                this.commentDialogVisible = true
                console.log(res.data)
                this.commentData = res.data
                console.log(this.commentData)
            })
        },
        addBlogComment(blogId) {
            const addBlogCommentsLoading = this.$loading({
                lock: true,
                text: 'Loading',
                spinner: 'el-icon-loading',
                background: 'rgba(0,0,0,0.7)'
            })
            newRequest.post(
                '/blog/post_blog_comment',
                {
                    user_id: this.auth.userid,
                    blog_id: blogId,
                    comment_content: this.commentData
                }
            ).then(res => {
                console.log(res.data)
                addBlogCommentsLoading.close()
            })
        },
        deletePersonalComment(commentId, blogId) {
            const deleteCommentLoading = this.$loading({
                lock: true,
                text: 'Loading',
                spinner: 'el-icon-loading',
                background: 'rgba(0,0,0,0.7)'
            })
            newRequest.post(
                '/blog/delete_blog_comment',
                {
                    commentid: commentId
                }
            ).then(res => {
                if (res.code === 200) {
                    deleteCommentLoading.close()
                    this.$message({
                        showClose: true,
                        message: 'Delete Success',
                        type: "success"
                    })
                    this.commentDialogVisible = false
                } else {
                    deleteCommentLoading.close()
                    this.$message({
                        showClose: true,
                        message: 'Something Error! Try Again!',
                        type: "error"
                    })
                }
            })
        }
    },
    mounted() {
        this.getPersonalBlog()
    }
}
</script>

<style>
.box {
    display: flex;
    flex-wrap: wrap;
}

.imageBox {
    position: relative;
    overflow: hidden;
    margin-bottom: 2%;
    width: 300px;
}

/* 2/3 */
.imageBox img:nth-child(1):nth-last-child(2),
.imageBox img:nth-child(2):nth-last-child(1),
.imageBox img:nth-child(1):nth-last-child(3),
.imageBox img:nth-child(2):nth-last-child(2),
.imageBox img:nth-child(3):nth-last-child(1) {
    width: 32%;
}

/* 4 */
.imageBox img:nth-child(1):nth-last-child(4),
.imageBox img:nth-child(2):nth-last-child(3),
.imageBox img:nth-child(3):nth-last-child(2),
.imageBox img:nth-child(4):nth-last-child(1) {
    width: 49%;
}

/*  5张以上图片  */
.imageBox img:nth-child(1):nth-last-child(n + 5),
.imageBox img:nth-child(1):nth-last-child(n + 5) ~ img {
    width: 32%;
}
</style>