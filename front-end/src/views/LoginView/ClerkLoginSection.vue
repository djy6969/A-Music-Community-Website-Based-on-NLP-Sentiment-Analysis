<template>
  <el-main>
    <el-form>
      <el-form-item label="User Name">
        <el-input v-model="this.clerkLoginForm.username" />
      </el-form-item>
      <el-form-item label="Password">
        <el-input v-model="this.clerkLoginForm.password" />
      </el-form-item>
      <el-button @click="clerkLoginRequest()" />
    </el-form>
  </el-main>
</template>

<script lang="ts">
import { ElMessage } from "element-plus";

export default {
  name: "ClerkLoginSection",
  data() {
    return {
      clerkLoginForm: {
        clerkName: "",
        password: "",
      },
    };
  },
  methods: {
    clerkLoginRequest() {
      let i = 0;
      const username_format = /^[a-zA-Z0-9_]{6,32}$/;
      const checkUsername = username_format.test(this.clerkLoginForm.username);
      if (checkUsername !== true) {
        ElMessage({
          message:
            "The username must contain 6 to 32 letters, digits, or underscores (_)",
          type: "warning",
        });
        this.isLoading = false;
        i += 1;
      }
      const password_format = /^[a-zA-Z0-9_]{5,15}$/;
      const checkPassword = password_format.test(this.loginForm.password);
      if (checkPassword !== true) {
        ElMessage({
          message:
            "The password must contain 6 to 16 letters, digits, or underscores (_)",
          type: "warning",
        });
        this.isLoading = false;
        i += 1;
      }
      if (
        this.loginForm.username === "" ||
        this.loginForm.email === "" ||
        this.loginForm.password === ""
      ) {
        ElMessage({
          message: "The username and password cannot be null!",
          type: "warning",
        });
        this.isLoading = false;
        i += 1;
      }
      if (i === 0) {
        this.$axios
          .post("account/login", {
            username: this.clerkLoginForm.username,
            password: this.clerkLoginForm.password,
          })
          .then((response) => {
            if (response.data.code === 200) {
              this.$cookies.set("Auth", "clerk")
              window.location.href = "/account";
              this.$emit("isLoading", false);
            } else if (response.data.code === -1) {
              ElMessage({
                message:
                  "Please enter the correct login user name and password",
                type: "warning",
              });
            } else if (response.data.msg === "账号被禁用了，请联系管理员解决") {
              this.isLoading = false;
              ElMessage({
                message:
                  "The account is disabled. Please contact the administrator",
                type: "warning",
              });
            }
          });
      }
    },
  },
};
</script>

<style scoped></style>
