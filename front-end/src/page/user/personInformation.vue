<template>
    <div class="personalInformationBox">
        <el-row type="flex">
            <el-col :span="8" style="height: 100%">
                <el-image
                        :src="personInformationForm.avatar"
                        @click="dialogVisible=true"
                />
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
                    <el-radio v-model="dialogData.changeTarget" label="nickname">Nick Name</el-radio>
                    <el-radio v-model="dialogData.changeTarget" label="email">E-Mail</el-radio>
                    <el-radio v-model="dialogData.changeTarget" label="tel">Telephone Number</el-radio>
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
         <el-dialog
            title="Listen "
            :visible.sync="dialogVisible"
        >
                    <el-upload
                        :on-change="changeUserAvatar"
                        :show-file-list="false"
                        action="#"
                        style="height: 100%;"
                    >
                        <i class="el-icon-plus avatar-uploader-icon"></i>
                    </el-upload>
                </el-dialog>
    </div>
</template>

<script>
import { newRequest } from "@/utils";

export default {
    name: "personInformation",
    components: {},
    data() {
        return {
            dialogVisible: false,
            dialogData: {
                showDialog: false,
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
        }
    },
    methods: {
        updateNewPersonalData() {
            newRequest.post(
                '/account/update_user_information',
                {
                    targetName: this.dialogData.changeTarget,
                    targetText: this.dialogData.changeInput,
                    userid: this.$cookies.get('auth').userid
                }
                // eslint-disable-next-line no-unused-vars
            ).then(res => {
                location.reload()
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
        updateUserAvatar(){
            this.dialogVisible = true
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
            avatarForm.append('user_id', this.$cookies.get('auth').userid)
            console.log(this.$cookies.get('auth').userid)
            newRequest.post(
                '/account/upload_head_portrait',
                avatarForm
            ).then(res => {
                console.log(res.data)
                this.personInformationForm.avatar = res.data
                let username = this.$cookies.get('auth').username
                let userid = this.$cookies.get('auth').userid
                let role = this.$cookies.get('auth').role
                this.$cookies.set('auth',
                    {
                        username: username,
                        userid: userid,
                        avatarUrl: res.data,
                        role: role
                    })
                changeUserAvatarLoading.close()
                location.reload()
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