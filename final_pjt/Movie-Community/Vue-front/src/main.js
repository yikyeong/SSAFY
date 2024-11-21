import Vue from 'vue'
import moment from "moment"
import VueMomentJS from "vue-momentjs"
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)
Vue.use(VueMomentJS, moment)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
