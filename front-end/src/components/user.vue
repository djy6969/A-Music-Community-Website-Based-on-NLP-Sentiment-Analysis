<template>
  <div class="user">
    <!-- 登录前 -->
    <div @click="onOpenModal" class="login-trigger" v-if="!isLogin">
      <i class="user-icon iconfont icon-yonghu" />
      <p class="user-name">Login</p>
    </div>
    <!-- 登录后 -->
    <div @click="onLogout" class="logined-user" v-else>
      <img v-lazy="$utils.genImgUrl(user.avatarUrl, 80)" class="avatar" />
      <p class="user-name">{{ user.nickname }}</p>
    </div>

    <!-- 登录框 -->
     <user-login style="z-index: 999;position: absolute;right: 35%" v-show="visible"></user-login>
  </div>
</template>

<script type="text/ecmascript-6">
import { confirm } from "@/base/confirm"
import {
  mapActions as mapUserActions,
  mapState as mapUserState,
  mapGetters as mapUserGetters
} from "@/store/helper/user"
import UserLogin from "@/components/auth/login.vue";
import axios from "axios";

export default {
  components: {UserLogin},
  data() {
    return {
      visible: false,
      loginVisible: false,
      loading: false,
      uid: "",
    }
  },
  methods: {
    onOpenModal() {
      this.visible = true
    },
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
    onLogout() {
      confirm("确定要注销吗？", () => {
        axios({
          method: 'GET',
          url: '/account/logout',
        })
      })
    },
    checkLogin(){
      const user_cookie = this.$cookies.get("Fianna_music_communicity")
      if (user_cookie !== null){
        this.isLogin = true
        this.visible = false
      }
    },
    openLoginSection(){
      this.loginVisible = true
    },
    ...mapUserActions(["login", "logout"])
  },
  computed: {
    ...mapUserState(["user"]),
    ...mapUserGetters(["isLogin"])
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