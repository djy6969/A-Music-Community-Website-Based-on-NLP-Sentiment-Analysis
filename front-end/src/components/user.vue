<template>
  <div class="user">
    <!-- 登录前 -->
    <div @click="visible = true" class="login-trigger" v-show="!isLogin">
      <i class="user-icon iconfont icon-yonghu" />
      <p class="user-name">Login</p>
    </div>
    <!-- 登录后 -->
    <el-dropdown>
      <div class="logined-user" v-show="isLogin">
        <h1>User</h1>
        <p class="user-name">{{ username }}</p>
      </div>
      <el-dropdown-menu>
        <el-dropdown-item @click.native="toPersonalPage">Personal Page</el-dropdown-item>
        <el-dropdown-item @click.native="toAddBlogPage">Add a Blog</el-dropdown-item>
        <el-dropdown-item @click.native="onLogout" >Log Out</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>



    <!-- 登录框 -->
    <el-dialog
        :visible.sync="visible"
        width="30%"
    >
      <el-tabs>
      <el-tab-pane label="Log In">
        <el-form ref="loginForm"
                 :model="loginForm"
                 class="login-form" autocomplete="on" label-position="left">
          <el-form-item prop="username">
            <el-input
                ref="username"
                v-model="loginForm.username"
                placeholder="Username"
                name="username"
                type="text"
                tabindex="1"
                autocomplete="on"
            />
          </el-form-item>
            <el-form-item prop="password">
              <el-input
                  ref="password"
                  v-model="loginForm.password"
                  placeholder="Password"
                  name="password"
                  tabindex="2"
                  autocomplete="on"
              />
            </el-form-item>
          <el-button type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="loginRequest">Login
          </el-button>
        </el-form>
      </el-tab-pane>
      <el-tab-pane label="Register">
        <el-form
            ref="loginForm"
            :model="registerForm"
            class="login-form" autocomplete="on" label-position="left">
          <el-form-item>
            <el-input
                ref="username"
                v-model="registerForm.username"
                placeholder="Username"
                name="username"
                type="text"
                tabindex="1"
                autocomplete="on"
            />
          </el-form-item>
          <el-form-item>
            <el-input
                ref="password"
                v-model="registerForm.password"
                placeholder="Password"
                name="password"
                tabindex="2"
                autocomplete="on"
            />
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="registerForm.tel"
              placeholder="Telephone Number"
            />
          </el-form-item>
          <el-form-item>
            <el-input
                v-model="registerForm.email"
                placeholder="Email Address"
            />
          </el-form-item>
          <el-form-item>
            <el-input
              v-model="registerForm.nickname"
              placeholder="Nickname"/>
          </el-form-item>
          <el-button type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="registerRequest">Register</el-button>
        </el-form>
      </el-tab-pane>
    </el-tabs>
    </el-dialog>
  </div>
</template>

<script type="text/ecmascript-6">
import {
  mapActions as mapUserActions,
  mapState as mapUserState,
} from "@/store/helper/user"
import axios from "axios";

export default {
  components: {},
  data() {
    return {
      visible: false,
      loginVisible: false,
      loading: false,
      uid: "",
      username: '',
      isLogin: '',
      loginForm: {
        username: '',
        password: ''
      },
      registerForm: {
        username: '',
        password: '',
        email: '',
        tel: '',
        nickname: ''
      }
    }
  },
  methods: {
    onCloseModal() {
      this.visible = false
    },
    async onLogin(uid) {
      this.loading = true
      const success = await this.login(uid).finally(() => {
        this.loading = false
      })
      if (success) {
        this.onCloseModal()
      }
    },
    loginRequest() {
      axios({
        method: 'POST',
        url: "account/login",
        data:{
          username: this.loginForm.username,
          password: this.loginForm.password
        }
      }).then(res=>{
        console.log(res.data)
        if (res.data.code===-1){
          this.$message({
            showClose:true,
            message:res.data.msg,
            type:'warning'
          })
        }
        if(res.data.code === 200) {
          this.$message({
            showClose:true,
            message:'Login Success',
            type: "success"
          })
          sessionStorage.setItem('Auth', this.loginForm.username)
          location.reload()
        }
      })
    },
    registerRequest() {
      axios({
        method: 'POST',
        url: "account/register",
        data:{
          username: this.registerForm.username,
          password: this.registerForm.password,
          password2: this.registerForm.password,
          email: this.registerForm.email,
          tel: this.registerForm.tel,
          nickname: this.registerForm.nickname
        }
      }).then(res=>{
        this.data = res.data
        // eslint-disable-next-line no-console
        console.log(res.data)
        if (res.data.code===-1){
          this.$message({
            showClose:true,
            message:res.data.msg,
            type:'warning'
          })
        }
        else {
          this.$message({
            showClose:true,
            message:'Register Success',
            type: "success"
          })
        }
      })
    },
    onLogout() {
      sessionStorage.removeItem('Auth')
      console.log("Log Out")
      axios({
        method: 'GET',
        url: 'account/logout'
      })
      location.reload()
    },
    toAddBlogPage(){
      this.$router.push('/addBlog')
    },
    toPersonalPage(){
      this.$router.push('/staff')
    },
    checkLogin(){
      const user_cookie = sessionStorage.getItem('Auth')
      console.log(user_cookie)
      if (user_cookie !== null){
        this.isLogin = true
        this.visible = false
        this.username = user_cookie
      }
    },
    ...mapUserActions(["login", "logout"])
  },
  computed: {
    ...mapUserState(["user"]),
  },
  mounted() {
    this.checkLogin()
    console.log(this.isLogin)
  }
}
</script>

<style lang="scss" scoped>
.user {
  padding: 16px;
  padding-bottom: 0;
  margin-bottom: 12px;

  .login-trigger {
    display: flex;
    align-items: center;
    cursor: pointer;
  }
  .user-icon {
    font-size: 24px;
  }

  .user-name {
    margin-left: 8px;
  }

  .logout {
    transform: translateY(1px);
    margin-left: 8px;
    color: var(--font-color-shallow-grey);
  }

  .login-body {
    .input {
      margin-bottom: 16px;
    }

    .login-help {
      .help {
        margin-bottom: 4px;
      }
    }
  }

  .login-btn {
    width: 100%;
    padding: 8px 0;
  }

  .logined-user {
    display: flex;
    align-items: center;
    cursor: pointer;

    .avatar {
      @include round(40px);
    }
  }
}
</style>