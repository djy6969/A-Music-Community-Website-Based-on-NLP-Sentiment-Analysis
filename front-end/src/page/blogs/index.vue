<template>
  <div>
    <div class="blog-container">
      <blog-card/>
    </div>
<!--    css back to top button-->
    <div class="el-backtop" @click="showAddBlogDialog">
      <i class="el-icon-plus"/>
    </div>
    <el-dialog
        title="Add Your Feelings Now"
        :visible.sync="visible"
        width="30%"
    >
      <el-form>
        <el-form-item>
          <el-input v-model="addBlogForm.text"
              type="textarea"
              :rows="4"
              placeholder="input your feelings"
          />
        </el-form-item>
        <el-form-item>
          <input type="file" id="file" @change="onUploadFile">
          <el-form-item>
            <el-button @click="onSubmitBlog">Submit</el-button>
          </el-form-item>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import BlogCard from "@/page/blogs/blogCard.vue";
import axios from "axios";

export default {
  name: "Blogs",
  components: {BlogCard},
  data(){
    return{
      visible: false,
      dialogImageUrl: '',
      dialogVisible: false,
      blogData: '',
      addBlogForm:{
        text: '',
        picFiles: []
      }
    }
  },
  methods:{
    showAddBlogDialog(){
      this.visible = true
      console.log('11111')
      console.log(this.visible)
    },
    onUploadFile(){
      this.addBlogForm.picFiles.push(document.getElementById('file').files[0])
    },
    onSubmitBlog(){
      let blogData = new FormData()
      console.log( document.getElementById('file').files[0])
      blogData.append('text', this.addBlogForm.text)
      blogData.append('picList', this.addBlogForm.picFiles)
      axios({
        method: "POST",
        url: 'blog/post_blog',
        headers: { "Content-Type": "multipart/form-data" },
        data: blogData,
      }).then(res=>{
        console.log(res.data)
      })
    }
  }
}
</script>

<style scoped>
.blog-container{
  width: 80%;
  margin: 0 0 auto;
  float:left;
  position:relative;
  left:5%
}
.el-backtop:hover {
  background-color: rgb(240, 240, 240);
}
.el-backtop {
  position: fixed;
  background-color: #fff;
  right: 2%;
  top: 40%;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  color: red;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  box-shadow: 0 0 6px rgba(0,0,0,.12);
  cursor: pointer;
  z-index: 5;
}
</style>