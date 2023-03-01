<template>
  <header class="main-header header-one menu-white">
    <!--Header-Upper-->
    <div class="header-upper bgc-black">
      <div class="container clearfix">
        <div class="header-inner rel d-flex align-items-center">
          <div class="logo-outer">
            <div class="logo">
              <a href="index.html"
                ><img
                  src="@/assets/images/logos/logo-one.png"
                  alt="Logo"
                  title="Logo"
              /></a>
            </div>
          </div>

          <div class="nav-outer mx-auto clearfix">
            <!-- Main Menu -->
            <nav class="main-menu navbar-expand-lg">
              <div class="navbar-header">
                <div class="mobile-logo">
                  <a href="/">
                    <img
                      src="@/assets/images/logos/logo-one.png"
                      alt="Logo"
                      title="Logo"
                    />
                  </a>
                </div>

                <!-- Toggle Button -->
                <button
                  type="button"
                  class="navbar-toggle"
                  data-bs-toggle="collapse"
                  data-bs-target=".navbar-collapse"
                >
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                  <span class="icon-bar"></span>
                </button>
              </div>

              <div class="navbar-collapse collapse clearfix">
                <ul class="navigation clearfix">
                  <li class="dropdown">
                    <a href="#">Home</a>
                    <ul>
                      <li><a href="/">IT Company</a></li>
                      <li><a href="/">IT Solutions</a></li>
                      <li><a href="/">IT Services</a></li>
                      <li><a href="/">IT Agency</a></li>
                    </ul>
                  </li>
                  <li class="dropdown">
                    <a href="#">services</a>
                    <ul>
                      <li><a href="/">Services One</a></li>
                      <li><a href="/">Services Two</a></li>
                      <li>
                        <a href="/">service details</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown">
                    <a href="#">Project</a>
                    <ul>
                      <li><a href="/">Project Grid</a></li>
                      <li>
                        <a href="/">Project Masonry.</a>
                      </li>
                      <li>
                        <a href="/">Project Details</a>
                      </li>
                    </ul>
                  </li>
                  <li class="dropdown">
                    <a href="#">shop</a>
                    <ul>
                      <li><a href="/">shop grid</a></li>
                      <li>
                        <a href="/">product details</a>
                      </li>
                      <li><a href="/">cart page</a></li>
                      <li><a href="/">checkout</a></li>
                    </ul>
                  </li>
                  <li class="dropdown">
                    <a href="#">blog</a>
                    <ul>
                      <li><a href="/">blog standard</a></li>
                      <li><a href="/">blog details</a></li>
                    </ul>
                  </li>
                  <li class="dropdown">
                    <a href="#">pages</a>
                    <ul>
                      <li><a href="/">About us</a></li>
                      <li><a href="/">Contact us</a></li>
                      <li><a href="/">Team</a></li>
                      <li><a href="/">faqs</a></li>
                      <li><a href="/">Pricing Plan</a></li>
                      <li><a href="/">404 error</a></li>
                    </ul>
                  </li>
                </ul>
              </div>
            </nav>
            <!-- Main Menu End-->
          </div>

          <!-- Nav Search -->
          <div class="nav-search py-10">
            <button class="far fa-search"></button>
            <form action="#" class="hide">
              <input
                type="text"
                placeholder="Search"
                class="searchbox"
                required=""
              />
              <button type="submit" class="searchbutton far fa-search"></button>
            </form>
          </div>

          <!-- Menu Button -->
          <div class="menu-btns">
            <a v-show="checkAuth" href="/userLogin" class="theme-btn"
              >Log In <i class="fas fa-long-arrow-right"></i></a>
            <a v-show="!checkAuth" href="/personalPage" class="theme-btn"
              >Go to the Personal Page <i class="fas fa-long-arrow-right"></i></a>

          </div>
        </div>
      </div>
    </div>
    <!--End Header Upper-->
  </header>
</template>

<script>
export default {
  name: "HeaderView",
  computed:{
    checkAuth() {
      return this.$cookies.get("Auth") == null
    },
  },
};
</script>

<style scoped></style>
