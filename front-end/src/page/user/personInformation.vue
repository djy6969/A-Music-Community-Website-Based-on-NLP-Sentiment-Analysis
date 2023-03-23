<template>
  <div>
    <el-row>
      <el-col span="8">
        <el-image :size="size" src=personInformationForm.avatar></el-image>
      </el-col>
      <el-col span="16">
        <ul class="list-group">
          <li class="list-group-item">
            <span>UserName:</span>
            <p>{{ personInformationForm.username }}</p>
            <el-link @click="editPersonalData('username', 'User Name')">edit</el-link>
          </li>
          <li class="list-group-item">
            <span>Nick Name:</span>
            <p>{{ personInformationForm.nickname }}</p>
            <el-link @click="editPersonalData('nickname', 'Nick Name')">edit</el-link>
          </li>
          <li class="list-group-item">
            <span>E-Mail</span>
            <p>{{ personInformationForm.email }}</p>
            <el-link @click="editPersonalData('email','E-Mail')">edit</el-link>
          </li>
          <li class="list-group-item">
            <span>Telephone Number:</span>
            <p>{{ personInformationForm.tel }}</p>
            <el-link @click="editPersonalData('tel', 'Telephone Number')">edit</el-link>
          </li>
          <li class="list-group-item">
            Password:
            <p>{{ personInformationForm.password }}</p>
            <el-link @click="editPersonalData('password', 'Password')">edit</el-link>
          </li>
        </ul>
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
    }
  }
}
</script>

<style>
</style>