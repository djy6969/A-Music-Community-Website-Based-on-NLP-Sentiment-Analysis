<template>
    <div>
        <div v-for="(item,index) in blogListData" :key="index" class="blog-container">
            <blog-card
                :avatar="item.head"
                :blog-id="item.id"
                :blog-text="item.blog_content"
                :picList="item.picList"
                :username="item.username"
            />
        </div>
        <!--    css back to top button-->
        <div class="el-backtop" @click="showAddBlogDialog">
            <i class="el-icon-plus"/>
        </div>
        <el-dialog
            :visible.sync="visible"
            title="Add Your Feelings Now"
            width="30%"
        >
            <el-form>
                <el-form-item>
                    <el-input v-model="addBlogForm.text"
                              :rows="4"
                              placeholder="input your feelings"
                              type="textarea"
                    />
                </el-form-item>
                <el-form-item>
                    <el-upload
                        :auto-upload="false"
                        :on-change="uploadSuccess"
                        accept=".jpg,.png"
                        action="#"
                    >
                        <div slot="tip" class="el-upload__tip">Only jpg/png files with a maximum size of 200kb can be uploaded
                        </div>
                        <el-button size="small" type="primary">Upload Pictures</el-button>
                    </el-upload>
                    <el-dialog :visible.sync="dialogVisible">
                        <img :src="dialogImageUrl" alt="" width="100%">
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
import {newRequest} from "@/utils";

export default {
    name: "Blogs",
    components: {BlogCard},
    data() {
        return {
            visible: false,
            dialogImageUrl: '',
            dialogVisible: false,
            blogData: '',
            addBlogForm: {
                text: '',
                picFiles: [],
                picFileNumber: ''
            },
            blogListData: []
        }
    },
    methods: {
        showAddBlogDialog() {
            this.visible = true
        },
        uploadSuccess(file, fileList) {
            console.log(file)
            if (file.size / 1024 >= 300) {
                return false
            } else {
                console.log("file " + file)
                console.log("fileList " + fileList)
                this.addBlogForm.picFiles.push(file.raw)
                console.log(this.addBlogForm.picFiles)
            }
        },
        onSubmitBlog() {
            const submitBlogLoading = this.$loading({
                lock: true,
                text: 'Loading',
                spinner: 'el-icon-loading',
                background: 'rgba(0,0,0,0.7)'
            })
            let blogData = new FormData()
            blogData.append('text', this.addBlogForm.text)
            blogData.append('user_id', this.$cookies.get('auth').userid)
            for (let i = 0; i < this.addBlogForm.picFiles.length; i++) {
                let name = `picList[${i}]`
                blogData.append(name, this.addBlogForm.picFiles[i])
                this.addBlogForm.picFileNumber = i + 1
            }
            blogData.append('picNumber', this.addBlogForm.picFileNumber)
            newRequest.post(
                '/blog/post_blog',
                blogData
            ).then(res => {
                if (res.code === 200) {
                    this.$message({
                        showClose: true,
                        message: res.data.meg,
                        type: "success"
                    })
                    submitBlogLoading.close()
                    this.addBlogForm.text = ''
                    this.addBlogForm.picFiles = []
                    this.addBlogForm.picFileNumber = ''
                    location.reload()
                } else {
                    this.$message({
                        showClose: true,
                        message: 'Something Wrong!',
                        type: 'error'
                    })
                }
            })
        },
        beforeUpload(file) {
            const fileSize = file.size / 1024
            console.log('filesize:' + fileSize)
            if (fileSize >= 300) {
                this.$message({
                    showClose: true,
                    message: 'The uploaded file cannot exceed 300kb'
                })
                return false
            }
        },
        getAllBlogsData() {
            const getAllBlogLoading = this.$loading({
                lock: true,
                text: 'Loading',
                spinner: 'el-icon-loading',
                background: 'rgba(0,0,0,0.7)'
            })
            newRequest.get('/blog/get_all_blogs').then((res => {
                console.log(res.data)
                this.blogListData = res.data
                getAllBlogLoading.close()
                console.log(this.blogListData)
            }))
        }
    },
    mounted() {
        this.getAllBlogsData()
    }
}
</script>

<style scoped>
.blog-container {
    width: 80%;
    margin: 0 0 auto;
    float: left;
    position: relative;
    left: 5%
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
    box-shadow: 0 0 6px rgba(0, 0, 0, .12);
    cursor: pointer;
    z-index: 5;
}
</style>