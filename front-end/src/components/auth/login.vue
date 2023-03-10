<template>
  <div class="login-container">
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
    <el-button type="primary" style="width:20%;margin-bottom:30px;">Exit</el-button>
  </div>
</template>
<script>

import axios from "axios";

export default {
  name: "userLogin",
  components: {},
  data() {
    return {
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
    loginRequest() {
      console.log('111')
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
    }
  }
}
</script>

<style>
#poster {
  z-index: 999;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}

body {
  margin: 0px;
  padding: 0px;
}

.login-container {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 350px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
  padding: 35px 35px 15px 35px;
}
</style>