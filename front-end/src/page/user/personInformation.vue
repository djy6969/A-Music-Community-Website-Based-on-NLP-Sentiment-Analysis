<template>
  <div class="personalInformationBox">
    <el-row>
      <el-col :span="8">
        <el-image  src=personInformationForm.avatar></el-image>
      </el-col>
      <el-col :span="16">
        <el-card class="box-card">
          <div class="text-item">
            <span>UserName: {{ personInformationForm.username }}</span>
          </div>
          <div class="text-item">
            <span>Nick Name: {{ personInformationForm.nickname }}</span>
          </div>
          <div class="text-item">
            <span>E-Mail: {{ personInformationForm.email }}</span>
          </div>
          <div class="text-item">
            <span>Telephone Number: {{ personInformationForm.tel }}</span>
          </div>
        </el-card>
      </el-col>
    </el-row>
    <el-dialog
        :title="dialogData.dialogName"
        :visible.sync="dialogData.showDialog"
    >
      <el-form>
        <el-form-item>
          <el-input v-model="dialogData.changeInput" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogData.showDialog = false">Cancel</el-button>
        <el-button type="primary" @click="updateNewPersonalData">Sure</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "personInformation",
  components: {},
  data() {
    return {
      dialogData: {
        showDialog: false,
        dialogName: '',
        changeTarget: '',
        changeInput: ''
      },
      personInformationForm: {
        username: 'username',
        nickname: 'nickname',
        email: 'email',
        tel: 'tel',
        password: 'pas',
        avatar: ''
      }
    }
  },
  methods: {
    editPersonalData(target, name) {
      this.dialogData.dialogName = 'New ' + name
      this.dialogData.changeTarget = target
      this.dialogData.showDialog = true
    },
    updateNewPersonalData(){
      axios({
        method: "POST",
        url: '',
        data:{
          targetName: this.dialogData.changeTarget,
          targetText: this.dialogData.changeInput
        }
      })
    },
    getPersonalData(){
      const getPersonalDataLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      axios({
        method: 'POST',
        url: ''
      }).then(res=>{
        console.log(res.data)
        getPersonalDataLoading.close()
      })
      }
    },
  mounted() {
  }
}
</script>

<style>
.personalInformationBox{
  border: 5px solid;
  border-image: linear-gradient(45deg, #ffadad, #ffd6a5, #fdffb6, #9bf6ff);
}
.text-item{
  flex-wrap: wrap;
  margin-bottom: 18px;
}
</style>