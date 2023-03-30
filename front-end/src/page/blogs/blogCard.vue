<template>
  <el-card class="blog-card" style="background-position: center">
    <div slot="header">
      {{ username }}:
    </div>
    <div class="text item" style="margin-bottom: 18px">{{ blogText }}</div>
    <div class="box">
      <div class="imageBox" v-for="(item,index) in picList" :key="index">
        <el-image
            :src="item"
            style=""/>
      </div>
    </div>

    <el-button
        size="small"
        type="text"
        style="width: 10%;float: right;color: #D33A31"
        @click="getBlogComments"
    >Comments
    </el-button>
    <el-dialog
        title="Comments"
        :visible.sync="commentDialogVisible"
        width="50%"
    >
      <ul v-for="(item,index) in commentData" :key="index">
        <li>{{ item.username }}:</li>
        <li>{{ item.comment }}</li>
      </ul>
      <div style="display: flex">
        <el-input placeholder="Comment"/>
        <el-button @click="addBlogComment">Send</el-button>
      </div>
    </el-dialog>
  </el-card>
</template>

<script>
import axios from "axios";

export default {
  name: "blogCard",
  props: [
    'username',
    'blogText',
    'blogId',
    'picList'
  ],
  data() {
    return {
      commentData: '',
      commentDialogVisible: false,
    }
  },
  methods: {
    getBlogComments() {
      const getBlogCommentsLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      axios({
        method: 'POST',
        url: '/blog/get_blog_comments',
        data: {
          blogid: this.blogId
        }
      }).then(res => {
        console.log(res.data)
        getBlogCommentsLoading.close()
        this.commentDialogVisible = true
        this.commentData = res.data.comments
      })
    },
    addBlogComment(){
      const addBlogCommentsLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      axios({
        method: 'POST',
        url:'',
        data:{

        }
      }).then(res=>{
        console.log(res.data)
        addBlogCommentsLoading.close()
      })
    }
  },
  mounted() {
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