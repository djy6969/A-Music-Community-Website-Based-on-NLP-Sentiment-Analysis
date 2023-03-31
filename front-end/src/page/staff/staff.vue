<template>
  <div class="staff-container">
    <el-button @click="onCreateNLP">NLP Creation</el-button>
    <el-form>
    <el-form-item>
      <el-input v-model="input"/>
      <el-button @click="this.analysisRequest">Enter</el-button>
    </el-form-item>
  </el-form>
    <p>{{result}}</p>
    <el-table
        :data="resultData"
    >
<!--      <el-table-column-->
<!--          type="index"-->
<!--          width="50"-->
<!--          -->
<!--      >-->
<!--      </el-table-column>-->
      <el-table-column
        prop="Text"
        label="Input Text"
        width="180">
      </el-table-column>
      <el-table-column
        prop="Result"
        label="result"
        width="180">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "staff",
  data(){
    return{
      input: '',
      resultData:[]
    }
  },
  methods:{
    onCreateNLP(){
      axios({
        method: 'GET',
        url: '/nlp_creation'
      }).then(res=>{
        this.$message({
            showClose:true,
            message:res.data.msg,
            type: "success"
        })
      })
    },
    analysisRequest(){
      axios({
        method: "POST",
        url: '/nlp_predict',
        data:{
          text: this.input
        }
      }).then(res=>{
        this.resultData.unshift({
          Text: this.input,
          Result: res.data.data.result
        })
        console.log(res.data)
      })
    }
  }
}
</script>

<style scoped>

</style>