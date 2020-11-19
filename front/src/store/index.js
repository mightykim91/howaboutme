import Vue from "vue";
import Vuex from "vuex";

import createPersistedState from "vuex-persistedstate";
import controlStore from "@/store/modules/controlStore";
import userStore from "@/store/modules/userStore";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    control: controlStore,
    user: userStore,
  },
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
      paths: [
        "control",
        "user"
      ],
    }),
  ],
});
