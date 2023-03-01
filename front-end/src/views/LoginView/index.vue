<template>
  <el-container>
    <el-header></el-header>
    <el-main>
      <UserLoginSection />
      <ClerkLoginSection />
    </el-main>
  </el-container>
</template>

<script>
import UserLoginSection from "@/views/LoginView/UserLoginSection.vue";
import ClerkLoginSection from "@/views/LoginView/ClerkLoginSection.vue";

export default {
  name: "LoginView",
  components: { ClerkLoginSection, UserLoginSection },
};
</script>

<style scoped></style>
