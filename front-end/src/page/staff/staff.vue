<template>
  <el-form>
    <el-form-item>
      <el-input v-model="input"/>
    </el-form-item>
    <el-button @click="this.analysisRequest">Enter</el-button>
  </el-form>
</template>

<script>
import axios from "axios";

export default {
  name: "staff",
  data(){
    return{
      input: '',
      result: ''
    }
  },
  methods:{
    analysisRequest(){
      axios({
        method: "POST",
        url: 'account/analysis',
        data:{
          input: this.input
        }
      }).then(res=>{
        this.result = res.data.msg
        alert(this.result)
      })
    }
  }
}
</script>

<style scoped>

</style>