<template>
  <el-container>
    <el-header></el-header>
    <el-main>
      <el-form>
        <el-form-item label="User Name">
          <el-input v-model="registerForm.username" />
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="registerForm.password1" />
        </el-form-item>
        <el-form-item label="Check Password">
          <el-input v-model="registerForm.password2" />
        </el-form-item>
        <el-form-item label="email">
          <el-input v-model="registerForm.email" />
        </el-form-item>
        <el-button @click="userRegisterRequest()">Register</el-button>
      </el-form>
    </el-main>
  </el-container>
</template>

<script>
import { ElMessage } from "element-plus";

export default {
  name: "RegisterView",
  data() {
    return {
      registerForm: {
        username: "",
        email: "",
        password1: "",
        password2: "",
      },
    };
  },
  methods: {
    userRegisterRequest() {
      let i = 0;
      const email_format = /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
      const checkEmail = email_format.test(this.registerForm.email);
      if (!checkEmail) {
        i += 1;
        alert("email address must conform to the format");
      }
      const username_format = /^[a-zA-Z0-9_]{5,41}$/;
      const checkUsername = username_format.test(this.registerForm.username);
      if (checkUsername !== true) {
        i += 1;
        ElMessage.error(
          "The username must contain 6 to 32 letters, digits, or underscores (_)"
        );
      }
      const password_format = /^[a-zA-Z0-9_]{5,15}$/;
      const checkPassword = password_format.test(this.registerForm.password);
      if (checkPassword !== true) {
        i += 1;
        ElMessage.error(
          "The password must contain 6 to 16 letters, digits, or underscores (_)"
        );
      }
      if (
        this.registerForm.username === "" ||
        this.registerForm.email === "" ||
        this.registerForm.password === "" ||
        this.registerForm.password2 === ""
      ) {
        ElMessage.error("username and password cannot be null!");
        i += 1;
      }
      if (i === 0) {
        this.axios
          .post("account/register", {
            username: this.registerForm.username,
            password: this.registerForm.password,
            password2: this.registerForm.password2,
            email: this.registerForm.email,
          })
          .then((response) => {
            console.log(response);
            if (response.data.code === -1) {
              ElMessage.error(response.data.message);
            }
          });
        window.location.assign("/login");
        this.$emit("isLoading", false);
      }
    },
  },
};
</script>

<style scoped></style>
