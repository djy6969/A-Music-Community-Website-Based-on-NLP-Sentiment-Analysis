<template>
  <div class="user">
    <!-- 登录前 -->
    <div @click="onOpenModal" class="login-trigger" v-if="!isLogin">
      <i class="user-icon iconfont icon-yonghu" />
      <p class="user-name">未登录</p>
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
import storage from "good-storage"
import { UID_KEY, isDef } from "@/utils"
import { confirm } from "@/base/confirm"
import {
  mapActions as mapUserActions,
  mapState as mapUserState,
  mapGetters as mapUserGetters
} from "@/store/helper/user"
import UserLogin from "@/components/auth/login.vue";
import axios from "axios";

export default {
  // 自动登录
  created() {
    const uid = storage.get(UID_KEY)
    if (isDef(uid)) {
      this.onLogin(uid)
    }
  },
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
    openLoginSection(){
      this.loginVisible = true
    },
    ...mapUserActions(["login", "logout"])
  },
  computed: {
    ...mapUserState(["user"]),
    ...mapUserGetters(["isLogin"])
  },
  components: {UserLogin}
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