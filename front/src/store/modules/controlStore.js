import axios from "axios";
import UserApi from "@/api/UserApi.js"



export default {
  namespaced: true,
  state: {
    controlInfo: {
      area: "모든 지역",
      max_age: 50,
      min_age: 20,
      max_height: 200,
      min_height: 140,
      body: [],
      education: [],
      job: [],
      religion: [],
      drink: "상관 없음",
      smoke: "상관 없음",
    },
  },
  getters: {
    getControlInfo(state) {
      return state.controlInfo;
    },
  },
  mutations: {
    setRegion(state, region) {
      state.controlInfo.area = region;
    },
    setMaxAge(state, max_age) {
      state.controlInfo.max_age = max_age;
    },
    setMinAge(state, min_age) {
      state.controlInfo.min_age = min_age;
    },
    setMaxHeight(state, max_height) {
      state.controlInfo.max_height = max_height;
    },
    setMinHeight(state, min_height) {
      state.controlInfo.min_height = min_height;
    },
    setBody(state, body) {
      state.controlInfo.body = body;
    },
    setEducation(state, education) {
      state.controlInfo.education = education;
    },
    setJob(state, job) {
      state.controlInfo.job = job;
    },
    setReligion(state, religion) {
      state.controlInfo.religion = religion;
    },
    setDrink(state, drink) {
      state.controlInfo.drink = drink;
    },
    setSmoke(state, smoke) {
      state.controlInfo.smoke = smoke;
    },
    setPreferences(state, controlInfo) {
      state.controlInfo = controlInfo;
    }
  },
  actions: {
    updateControls({getters, rootGetters}) {
      axios.put(`${UserApi.BASE_URL}/preferences/`, getters.getControlInfo, rootGetters['user/config'])
      .then ((res) => {
        console.log(res)
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
};
