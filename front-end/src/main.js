import Vue from 'vue'
import App from './App.vue'
import router from './router'

import '@/style/index.scss'
import '@/utils/rem'
import '@/utils/axios'
import store from './store/index'
import global from './utils/global'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import VueCookies from 'vue-cookies'
import VueSocketIO from "vue-socket.io";
import SocketIO from "socket.io-client";
import TRTC from 'trtc-js-sdk';

// axios
import axios from "axios"
axios.defaults.withCredentials = true
axios.defaults.baseURL = 'https://ipa-012.ucd.ie/api/'
// axios.defaults.baseURL = 'https://127.0.0.1:5000/api/'

import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon, FontAwesomeLayers, FontAwesomeLayersText} from '@fortawesome/vue-fontawesome'
library.add(fas, far, fab)
Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.component('font-awesome-layers', FontAwesomeLayers)
Vue.component('font-awesome-layers-text',FontAwesomeLayersText)

Vue.use(
    new VueSocketIO({
      debug: true,
      connection: SocketIO("http://ipa-012.ucd.ie/", {transports: ['polling']}),
      autoConnect: false,
      extraHeaders: {
          'Access-Control-Allow-Origin': '*'
      }
    })
)
Vue.use(ElementUI);
Vue.use(VueCookies)
Vue.config.productionTip = false
Vue.use(global)

// data visualization
// 将自动注册所有组件为全局组件
import dataV from '@jiaminghi/data-view'
Vue.use(dataV)

// import echarts from "echarts"
// Vue.prototype.$echarts = echarts
TRTC.Logger.setLogLevel(TRTC.Logger.LogLevel.DEBUG);
new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')