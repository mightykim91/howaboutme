import Vue from 'vue'
import VueSweetalert2 from 'vue-sweetalert2';
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify';
import VueCookie from "vue-cookie";
import axios from "axios";
import Vue2TouchEvents from 'vue2-touch-events'

// If you don't need the styles, do not connect
import 'sweetalert2/dist/sweetalert2.min.css';

 
import io from 'socket.io-client';
//const socket = io('https://k3a507.p.ssafy.io:3000', {secure:true});
var socket = io('http://localhost:3000');

//Initialize socket
Vue.prototype.$socket = socket;
Vue.config.productionTip = false
Vue.prototype.$http = axios;

Vue.use(VueCookie);
Vue.use(Vue2TouchEvents)
Vue.use(VueSweetalert2);

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
