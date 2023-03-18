<template>
  <el-card class="blog-card" style="background-position: center">
    <div slot="header">
      <span>Header</span>
    </div>
    <div>
      ifhjalfjvs
    </div>
  </el-card>
</template>

<script>
import axios from "axios";

export default {
  name: "blogCard",
  methods:{
    getBlogRequest(){
      axios({
        method: 'GET',
        url: ''
      })
    }
  }
}
</script>

<style scoped>

</style>