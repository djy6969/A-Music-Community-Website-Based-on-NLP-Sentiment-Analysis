<template>
  <el-card class="blog-card" style="background-position: center">
    <div slot="header">
      {{username}}
    </div>
    <ul class="list-group list-group-flush">
      <li class="list-group-item">
        <div class="pictureContainer">
          <img src="">
        </div>
      </li>
      <li class="list-group-item">{{blogText}}</li>
    </ul>
    <el-button
        size="small"
        type="text"
        style="width: 10%;float: right;color: #D33A31"
        @click="dialogVisible"
    >Comments</el-button>
    <el-dialog
        title="Comments"
        :visible.sync="commentDialogVisible"
        width="50%"
    >
      <ul v-for="(item,index) in commentData" :key="index">
        <li>
          {{item.username}} :
          {{item.comment}}
        </li>
      </ul>
    </el-dialog>
  </el-card>
</template>

<script>
import axios from "axios";

export default {
  name: "blogCard",
  props:[
    'username',
    'blogText',
    'blogId'
  ],
  data(){
    return{
      commentData: '',
      commentDialogVisible: false,
    }
  },
  methods:{
    dialogVisible(){
      this.commentDialogVisible = true
      console.log('activate dialogVisible()')
    },
    getBlogComments(){
      axios({
        method: 'GET',
        url: ''
      }).then(res=>{
        console.log(res.data)
      })
    }
  },
  mounted() {
    this.getBlogComments()
  }
}
</script>

<style scoped>

</style>