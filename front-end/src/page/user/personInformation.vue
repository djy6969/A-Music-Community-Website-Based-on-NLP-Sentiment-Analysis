<template>
  <div class="personalInformationBox">
    <el-row type="flex">
      <el-col :span="8" style="height: 100%">
        <el-image
            v-if="this.personInformationForm.avatar !== 'https://ipa-012.ucd.ie/image/default.png'"
            :src="personInformationForm.avatar"
        />
        <el-upload
            v-if="this.personInformationForm.avatar === 'https://ipa-012.ucd.ie/image/default.png'"
            style="height: 100%;"
            action="#"
            :show-file-list="false"
            :on-change="changeUserAvatar"
        >
          <i class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-col>
      <el-col :span="16"  style="height: 100%">
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
    updateNewPersonalData() {
      axios({
        method: "POST",
        url: '',
        data: {
          targetName: this.dialogData.changeTarget,
          targetText: this.dialogData.changeInput
        }
      })
    },
    getPersonalData() {
      const getPersonalDataLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      axios({
        method: 'POST',
        url: '/account/get_user_info',
        data:{
          user_id: sessionStorage.getItem('userid')
        }
      }).then(res => {
        console.log(res.data)
        this.personInformationForm.username = sessionStorage.getItem('Auth')
        this.personInformationForm.email = res.data.data.email
        this.personInformationForm.nickname = res.data.data.nickname
        this.personInformationForm.tel = res.data.data.tel
        this.personInformationForm.avatar = res.data.data.head_protrait
        console.log(this.personInformationForm.avatar)
        getPersonalDataLoading.close()
      })
    },
    changeUserAvatar(file){
      const changeUserAvatarLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      let avatarForm = new FormData()
      avatarForm.append('head', file.raw)
      console.log(avatarForm.head)
      console.log(file.raw)
      avatarForm.append('user_id', sessionStorage.getItem('userid'))
      axios({
        method: 'POST',
        url: '/account/upload_head_portrait',
        headers: { "Content-Type": "multipart/form-data" },
        data: avatarForm
      }).then(res=>{
        this.personInformationForm.avatar = res.data.data
        console.log(this.personInformationForm.avatar)
        changeUserAvatarLoading.close()
      })
    }
  },
  mounted() {
    this.getPersonalData()
  }
}
</script>

<style>
.personalInformationBox {
  border: 5px solid;
  border-image: linear-gradient(45deg, #ffadad, #ffd6a5, #fdffb6, #9bf6ff);
}

.text-item {
  flex-wrap: wrap;
  margin-bottom: 18px;
}
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>