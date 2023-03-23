<template>
  <div>
    <div class="blog-container" v-for="(item,index) in blogListData" :key="index">
      <blog-card :blog-text="item.blogText" :username="item.username" />
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
          <el-upload
              action="#"
              :on-change="uploadSuccess"
              :auto-upload="false"
          >
            <el-button size="small" type="primary">Upload Pictures</el-button>
          </el-upload>
          <el-dialog :visible.sync="dialogVisible">
            <img width="100%" :src="dialogImageUrl" alt="">
          </el-dialog>
        </el-form-item>
        <el-form-item>
          <el-button @click="onSubmitBlog">Submit</el-button>
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
      fileList: [{}],
      addBlogForm:{
        text: '',
        picFiles: [],
        picFileNumber: ''
      },
      blogListData: [
        {
          'blogText': 'blogText1',
          'username': 'username1'
          },
        {
          'blogText': 'blogText2',
          'username': 'username2'
        }
      ]
    }
  },
  methods:{
    showAddBlogDialog(){
      this.visible = true
    },
    uploadSuccess(file, fileList){
      console.log("file "+ file)
      console.log("fileList "+ fileList)
      this.addBlogForm.picFiles.push(file.raw)
      console.log(this.addBlogForm.picFiles)
    },
    onSubmitBlog(){
      let blogData = new FormData()
      blogData.append('text', this.addBlogForm.text)
      for (let i=0; i< this.addBlogForm.picFiles.length; i++){
        let name = `picList[${i}]`
        blogData.append(name, this.addBlogForm.picFiles[i])
        this.addBlogForm.picFileNumber = i
      }
      blogData.append('picNumber', this.addBlogForm.picFileNumber)
      axios({
        method: "POST",
        url: 'blog/post_blog',
        headers: { "Content-Type": "multipart/form-data" },
        data: blogData,
      }).then(res=>{
        console.log(res.data)
      })
    },
    getBlogsData(){
      axios({
        method: 'GET',
        url: 'blog/get_blogs',
        params: {

        }
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