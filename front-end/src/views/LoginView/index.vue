<template>
  <div class="col-xl-6 col-lg-10">
    <div class="about-four-content mb-65 rel z-1 wow fadeInLeft delay-0-2s">
      <div class="section-title mb-50">
        <span class="sub-title mb-15">About Company</span>
        <h2>Best Talent, Competitive Cost, Incredible IT Service</h2>
        <span class="bg-text">About</span>
      </div>
      <ul class="nav nav-pills nav-fill mb-35">
        <li class="nav-item">
          <a class="nav-link active" data-bs-toggle="tab" href="#about-tap1"
            >User Login</a
          >
        </li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="tab" href="#about-tap2"
            >Clerk Login</a
          >
        </li>
      </ul>
      <div class="tab-content">
        <div class="tab-pane fade show active" id="about-tap1">
          <UserLoginSection />
        </div>
        <div class="tab-pane fade" id="about-tap2">
          <ClerkLoginSection />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import UserLoginSection from "@/views/LoginView/UserLoginSection.vue";
import ClerkLoginSection from "@/views/LoginView/ClerkLoginSection.vue";

export default {
  name: "LoginView",
  components: {ClerkLoginSection, UserLoginSection},
};
</script>

<style scoped></style>
