import 'normalize.css';
import { createPinia } from 'pinia';
// @ts-ignore
import VueVirtualScroller from 'vue-virtual-scroller';
import { createApp } from 'vue';
import App from './App.vue';
import './assets/css/common.css';
import './assets/css/transition.css';
import './index.css';
import router from './router';
const app = createApp(App);

app.use(createPinia());
app.use(VueVirtualScroller);
app.use(router);
app.mount('#app');