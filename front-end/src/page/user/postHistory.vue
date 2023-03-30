<template>
  <div>
    <div class="blog-container" v-for="(item, index) in personalBlogData" :key="index">
      <el-card class="blog-card" style="background-position: center">
        <div slot="header">
          {{ item.username }}:
        </div>
        <div class="text item" style="margin-bottom: 18px">{{ item.blog_content }}</div>
        <div class="box">
          <div class="imageBox" v-for="(item2,index) in item.picList" :key="index">
            <el-image
                :src="item2"
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
          <ul v-for="(item3,index) in commentData" :key="index">
            <li>{{ item3.username }}:</li>
            <li>{{ item3.comment }}</li>
          </ul>
        </el-dialog>
      </el-card>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "postHistory",
  components: {},
  data() {
    return {
      personalBlogData: []
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
      axios({
        method: 'POST',
        url: '/blog/get_user_blog',
        data: {
          userid: sessionStorage.getItem('userid')
        }
      }).then(res => {
        this.personalBlogData = res.data.data
        getPersonalBlogLoading.close()
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