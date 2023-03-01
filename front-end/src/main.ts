import { createApp } from "vue";
import App from "./App.vue";
import ElementPlus from "element-plus";
import router from "./router";
import axios from "axios";
import "element-plus/dist/index.css";
import "tailwindcss/tailwind.css";

import "./assets/css/flaticon.min.css";
import "./assets/css/fontawesome-5.14.0.min.css";
import "./assets/css/bootstrap.min.css";
import "./assets/css/magnific-popup.min.css";
import "./assets/css/nice-select.min.css";
import "./assets/css/animate.min.css";
import "./assets/css/slick.min.css";
import "./assets/css/style.css";
import "./assets/js/jquery-3.6.0.min.js";
import "./assets/js/bootstrap.min.js";
import "./assets/js/appear.min.js";
import "./assets/js/slick.min.js";
import "./assets/js/jquery.magnific-popup.min.js";
import "./assets/js/jquery.nice-select.min.js";
import "./assets/js/imagesloaded.pkgd.min.js";
import "./assets/js/circle-progress.min.js";
import "./assets/js/isotope.pkgd.min.js";
import "./assets/js/script.js";
// @ts-ignore
import cookies from "vue-cookies";


const app = createApp(App);

app.config.globalProperties.$cookies = cookies
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://127.0.0.1:5000/";

app.use(ElementPlus);
app.use(router);

app.mount("#app");
