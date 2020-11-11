import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import controlStore from "@/store/modules/controlStore";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    control: controlStore,
  },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
      paths: ["control"],
    }),
  ],
})
