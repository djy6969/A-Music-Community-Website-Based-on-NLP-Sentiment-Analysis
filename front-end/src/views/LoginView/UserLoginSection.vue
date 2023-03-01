<template>
  <el-main>
    <el-form>
      <el-form-item label="User Name">
        <el-input v-model="this.userLoginForm.username" />
      </el-form-item>
      <el-form-item label="Password">
        <el-input v-model="this.userLoginForm.password" />
      </el-form-item>
      <el-button @click="userLoginRequest()" />
    </el-form>
  </el-main>
</template>

<script>
import { ElMessage } from "element-plus";

export default {
  name: "UserLoginSection",
  data() {
    return {
      userLoginForm: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    userLoginRequest() {
      let i = 0;
      const username_format = /^[a-zA-Z0-9_]{6,32}$/;
      const checkUsername = username_format.test(this.userLoginForm.username);
      if (checkUsername !== true) {
        ElMessage({
          message:
            "The username must contain 6 to 32 letters, digits, or underscores (_)",
          type: "warning",
        });
        i += 1;
      }
      const password_format = /^[a-zA-Z0-9_]{5,15}$/;
      const checkPassword = password_format.test(this.userLoginForm.password);
      if (checkPassword !== true) {
        ElMessage({
          message:
            "The password must contain 6 to 16 letters, digits, or underscores (_)",
          type: "warning",
        });
        i += 1;
      }
      if (
        this.userLoginForm.username === "" ||
        this.userLoginForm.email === "" ||
        this.userLoginForm.password === ""
      ) {
        ElMessage({
          message: "The username and password cannot be null!",
          type: "warning",
        });
        i += 1;
      }
      if (i === 0) {
        this.axios
          .post("account/login", {
            username: this.userLoginForm.username,
            password: this.userLoginForm.password,
          })
          .then((response) => {
            if (response.data.code === 200) {
              window.location.href = "/";
              this.$emit("isLoading", false);
            } else if (response.data.code === -1) {
              ElMessage({
                message: response.data.message,
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
