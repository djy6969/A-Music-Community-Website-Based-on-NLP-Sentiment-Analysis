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
      <el-col :span="16" style="height: 100%">
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
          <el-button @click="dialogData.showDialog=true">Change Information</el-button>
        </el-card>
      </el-col>
    </el-row>
    <el-dialog
        :title="dialogData.dialogName"
        :visible.sync="dialogData.showDialog"
    >
      <el-form>
        <el-form-item label="Choose which to edit">
          <el-select v-model="dialogData.changeTarget" placeholder="please input">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Input">
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
import { newRequest } from "@/utils";

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
      },
      options:[
        {
          label: 'username',
          value: 'username'
        },
        {
          label: 'nickname',
          value: 'nickname'
        },
        {
          label: 'email',
          value: 'email',
        },
        {
          label: 'tel',
          value: 'tel'
        }
      ]
    }
  },
  methods: {
    updateNewPersonalData() {
      newRequest.post(
          '',
          {
            targetName: this.dialogData.changeTarget,
            targetText: this.dialogData.changeInput,
            userid: sessionStorage.getItem('userid')
          }
        ).then(res=>{
          console.log(res)
      })
    },
    getPersonalData() {
      const getPersonalDataLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      newRequest.post(
          '/account/get_user_info',
          {
            user_id: this.$cookies.get('auth').userid
          }
      ).then(res => {
        console.log(res.data)
        this.personInformationForm.username = this.$cookies.get('auth').username
        this.personInformationForm.email = res.data.email
        this.personInformationForm.nickname = res.data.nickname
        this.personInformationForm.tel = res.data.tel
        this.personInformationForm.avatar = res.data.head_protrait
        console.log(this.personInformationForm.avatar)
        getPersonalDataLoading.close()
      })
    },
    changeUserAvatar(file) {
      const changeUserAvatarLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      let avatarForm = new FormData()
      avatarForm.append('head', file.raw)
      avatarForm.append('user_id', sessionStorage.getItem('userid'))
      newRequest.post(
          '/account/upload_head_portrait',
          {
            avatarForm
          }
      ).then(res => {
        this.personInformationForm.avatar = res.data
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