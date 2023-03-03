<template>
  <div class="page-wrapper">
    <HeaderView />
    <div class="checkout-form-area py-130">
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
                  <div class="col-lg-12 pt-15">
                    <h5>Register to get a new account</h5>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <input
                        type="text"
                        v-model="registerForm.username"
                        placeholder="User Name"
                        required=""
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <input
                        type="email"
                        v-model="registerForm.email"
                        placeholder="Email Address"
                        required=""
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <input
                        type="text"
                        v-model="registerForm.password1"
                        placeholder="Password"
                      />
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <input
                        type="text"
                        class="form-control"
                        v-model="registerForm.password2"
                        placeholder="Check Password"
                      />
                    </div>
                  </div>
                </div>
              </form>
            </div>
            <button
              type="button"
              class="theme-btn w-100"
              @click="userRegisterRequest()"
            >
              Register
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ElMessage } from "element-plus";
import HeaderView from "@/components/HeaderView.vue";

export default {
  name: "RegisterView",
  components: { HeaderView },
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
