<template>
  <div class="user">
    <Loading
        :loading="userLoading"
        v-if="userLoading"
    />
    <!-- 登录前 -->
    <div @click="visibleData.loginVisible = true" class="login-trigger" v-show="!isLogin">
      <i class="user-icon iconfont icon-yonghu"/>
      <p class="user-name">Login</p>
    </div>
    <!-- 登录后 -->
    <el-dropdown>
      <div class="logined-user" v-show="isLogin">
        <el-avatar :src="userData.avatarUrl"/>
        <p class="user-name">{{ username }}</p>
      </div>
      <el-dropdown-menu>
        <el-dropdown-item v-show="userData.role==='user'" @click.native="toPersonalPage">Personal Page
        </el-dropdown-item>
        <el-dropdown-item v-show="userData.role==='staff'" @click.native="toStaffPage">Staff</el-dropdown-item>
        <el-dropdown-item @click.native="onLogout">Log Out</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <!-- 登录框 -->
    <div class="mask-layer">
      <div class="login-box" v-show="visibleData.loginVisible">
        <div class="align">
          <span class="red" @click="visibleData.loginVisible=false"></span>
        </div>
        <form>
          <div class="user-box">
            <input type="text" name="" required="" v-model="loginForm.username">
            <label>Username</label>
          </div>
          <div class="user-box">
            <input type="password" name="" required="" v-model="loginForm.password">
            <label>Password</label>
            <p href="#" style="float: right" @click="visibleData.registerVisible=true">
              No Account?
            </p>
            <center>
              <a href="#" @click="loginRequest">
                User Login
                <span></span>
              </a>
            </center>
          </div>
        </form>
      </div>
      <div class="login-box" v-show="visibleData.registerVisible">
        <div class="align">
          <span class="red" @click="visibleData.registerVisible=false"></span>
        </div>
        <form>
          <div class="user-box">
            <input type="text" name="" required="" v-model="registerForm.username">
            <label>Username</label>
          </div>
          <div class="user-box">
            <input type="text" name="" required="" v-model="registerForm.password">
            <label>Password</label>
          </div>
          <div class="user-box">
            <input type="text" name="" required="" v-model="registerForm.email">
            <label>Email</label>
          </div>
          <div class="user-box">
            <input type="text" name="" required="" v-model="registerForm.nickname">
            <label>Nickname</label>
          </div>
          <div class="user-box">
            <input type="password" name="" required="" v-model="registerForm.tel">
            <label>Telephone Number</label>
            <center>
              <a href="#" @click="loginRequest">
                User Login
                <span></span>
              </a>
            </center>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script type="text/ecmascript-6">
import {
  mapActions as mapUserActions,
  mapState as mapUserState,
} from "@/store/helper/user"
import Loading from "@/base/loading.vue";
import {newRequest} from "../utils";

export default {
  components: {Loading},
  data() {
    return {
      userLoading: false,
      visibleData: {
        loginVisible: false,
        registerVisible: false
      },
      isLogin: false,
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
      },
      userData: {
        username: '',
        avatarUrl: '',
        role: ''
      }
    }
  },
  methods: {
    onCloseModal() {
      this.visible = false
    },
    onOpenRegister() {
      this.visibleData.loginVisible = false
      this.visibleData.registerVisible = true
    },
    loginRequest() {
      const loginLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      console.log(this.loginForm.username)
      newRequest.post('/account/login',
          {
            username: this.loginForm.username,
            password: this.loginForm.password
          }
      ).then(res => {
        console.log(res)
        if (res.code === -1) {
          loginLoading.close()
          this.$message({
            showClose: true,
            message: res.data.msg,
            type: 'warning'
          })
        }
        if (res.code === 200) {
          this.$cookies.set(
              'auth',
              {
                username: this.loginForm.username,
                userid: res.data.id,
                avatarUrl: res.data.url,
                role: res.data.role
              }
          )
          loginLoading.close()
          this.$message({
            showClose: true,
            message: 'Login Success',
            type: "success"
          })
          location.reload()
        }
      })
    },
    registerRequest() {
      const registerLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      newRequest.post(
          "/account/register",
          {
            username: this.registerForm.username,
            password: this.registerForm.password,
            password2: this.registerForm.password,
            email: this.registerForm.email,
            tel: this.registerForm.tel,
            nickname: this.registerForm.nickname,
          }
      ).then(res => {
        this.data = res.data
        if (res.data.code === -1) {
          registerLoading.close()
          this.$message({
            showClose: true,
            message: res.data.msg,
            type: 'warning'
          })
        } else {
          registerLoading.close()
          this.$message({
            showClose: true,
            message: 'Register Success',
            type: "success"
          })
        }
      })
    },
    onLogout() {
      const logoutLoading = this.$loading({
        lock: true,
        text: 'Loading',
        spinner: 'el-icon-loading',
        background: 'rgba(0,0,0,0.7)'
      })
      this.$cookies.remove('auth')
      newRequest.get(
          '/account/logout'
      )
      location.reload()
      logoutLoading.close()
    },
    toStaffPage() {
      this.$router.push('/staff')
    },
    toPersonalPage() {
      this.$router.push('/user')
    },
    checkLogin() {
      const userCookie = this.$cookies.get('auth')
      if (userCookie !== null) {
        this.isLogin = true
        this.visible = false
        this.userData.username = userCookie.username
        this.userData.avatarUrl = userCookie.avatarUrl
        this.userData.role = userCookie.role
      }
    },
    ...mapUserActions(["login", "logout"])
  },
  computed: {
    ...mapUserState(["user"]),
  },
  mounted() {
    this.checkLogin()
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


  .logined-user {
    display: flex;
    align-items: center;
    cursor: pointer;

    .avatar {
      @include round(40px);
    }
  }
}

.login-box {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 400px;
  padding: 40px;
  transform: translate(-50%, -50%);
  background: rgba(24, 20, 20, 0.987);
  box-sizing: border-box;
  box-shadow: 0 15px 25px rgba(0, 0, 0, .6);
  border-radius: 10px;
  z-index: 4;
}

.login-box .align {
  padding: 1rem;
  display: flex;
  flex-direction: row;
  gap: 5px;
  align-self: flex-start;
}

.red {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #ff605c;
  box-shadow: -5px 5px 5px rgba(0, 0, 0, 0.280);
}

.login-box .user-box {
  position: relative;
}

.login-box .user-box input {
  width: 100%;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  margin-bottom: 30px;
  border: none;
  border-bottom: 1px solid #fff;
  outline: none;
  background: transparent;
}

.login-box .user-box label {
  position: absolute;
  top: 0;
  left: 0;
  padding: 10px 0;
  font-size: 16px;
  color: #fff;
  pointer-events: none;
  transition: .5s;
}

.login-box .user-box input:focus ~ label,
.login-box .user-box input:valid ~ label {
  top: -20px;
  left: 0;
  color: #bdb8b8;
  font-size: 12px;
}

.login-box form a {
  position: relative;
  display: inline-block;
  padding: 10px 20px;
  color: #ffffff;
  font-size: 16px;
  text-decoration: none;
  text-transform: uppercase;
  overflow: hidden;
  transition: .5s;
  margin-top: 40px;
  letter-spacing: 4px
}

.login-box a:hover {
  background: #0000ff;
  color: #fff;
  border-radius: 5px;
  box-shadow: 0 0 5px #0000ff,
  0 0 25px #0000ff,
  0 0 50px #0000ff,
  0 0 100px #0000ff;
}

.login-box a span {
  position: absolute;
  display: block;
}

@keyframes btn-anim1 {
  0% {
    left: -100%;
  }

  50%, 100% {
    left: 100%;
  }
}

.login-box a span:nth-child(1) {
  bottom: 2px;
  left: -100%;
  width: 100%;
  height: 2px;
  background: linear-gradient(90deg, transparent, #0000ff);
  animation: btn-anim1 2s linear infinite;
}
</style>