<template>
  <div class="container">
    <div class="checkout-faqs" id="checkout-faqs">
      <div class="alert bgc-lighter wow fadeInUp delay-0-4s">
        <div id="collapse4" class="collapse content show">
          <form
            id="checkout-form"
            class="checkout-form"
            name="checkout-form"
            action="#"
            method="post"
          >
            <div class="row">
              <div class="col-md-6">
                <div class="form-group">
                  <input
                    type="text"
                    v-model="this.userLoginForm.username"
                    placeholder="User Name"
                    required=""
                  />
                </div>
              </div>
              <div class="col-md-6">
                <div class="form-group">
                  <input
                    type="text"
                    v-model="this.userLoginForm.password"
                    placeholder="Password"
                  />
                </div>
              </div>
            </div>
          </form>
        </div>
        <button
          type="button"
          class="theme-btn w-100"
          @click="userLoginRequest()"
        >
          Login
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
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
              this.$cookies.set("Auth", "user");
              window.location.href = "/";
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
