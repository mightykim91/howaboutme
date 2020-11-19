import axios from "axios";

import cookies from "vue-cookies";
import USERAPI from "@/api/UserApi"
import router from '@/router';


export default {
  namespaced: true,
  state: {
    profile_saved:false,
    image_saved:false,
    authToken: null,
    // authToken: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ilx1ZDE0Y1x1YzJhNFx1ZDJiOFx1YWNjNFx1YzgxNTExIiwiZXhwIjoxNjA1ODYyNzM4LCJlbWFpbCI6InRlc3QxMUB0ZXN0LmNvbSIsIm9yaWdfaWF0IjoxNjA1MjU3OTM4fQ.fFSK0Yt9wBNF9F-uRUShbSjQ9AkC8p1DajS2RnsNhA0",
    // authToken: null,
    // userInfo: Object,
    userInfo: {
      id: 103,
    },
    unreadMessage: 0,
    preference: {},
    // userInfo: {
    //   gender: "",
    //   birth: "",
    //   nickname: "",
    //   area: "",
    //   hobby1: "",
    //   hobby2: "",
    //   height: "",
    //   blood: "",
    //   religion: "",
    //   drink: "",
    //   smoke: "",
    //   education: "",
    //   body: "",
    //   job: "",
    //   intro: "",
    // },
  },
  getters: {
    isLoggedIn: (state) => !!state.authToken,
    // isLoggedIn: (state) => !!state.authToken,
    config: (state) => ({
      headers: {
        Authorization: `JWT ${state.authToken}`,
      },
    }),
    getUserInfo(state) {
      return state.userInfo;
    },
    getAuthToken(state) {
      return state.authToken;
    },
    getNickname(state) {
      return state.userInfo.nickname;
    },
    getSimilarity(state) {
      return state.userInfo.user.similarity;
    },
    getPreference(state) {
      return state.preference;
    }
  },
  mutations: {
    SET_ACTIVE_USER(state, res) {
      state.userInfo = res.data.profile;
    },
    SET_PROFILE(state,userInfo) {
      state.userInfo = userInfo
    },
    SET_PREFERENCE(state,preference) {
      state.preference = preference
    },
    setSimilarity(state, similarity) {
      state.userInfo.user.similarity = similarity
    },
    SET_SIMILARITY(state, similarity) {
      state.userInfo.user.similarity = similarity
    },
    unreadMessageCount(state, res) {
      state.unreadMessage += res;
    },
    initialPreferences({ getters, commit }) {
      var initialBodies = getters.getPreference.body;
      var initialEdus = getters.getPreference.education;
      var initialJobs = getters.getPreference.job;
      var initialReligions = getters.getPreference.religion;
      var body = []
      var education = []
      var job = []
      var religion = []
      for (var initBody of initialBodies) {
        body.push(initBody.name)
      }
      for (var initEdu of initialEdus) {
        education.push(initEdu.name)
      }
      for (var initJob of initialJobs) {
        job.push(initJob.name)
      }
      for (var initReligion of initialReligions) {
        religion.push(initReligion.name)
      }
      commit('control/setRegion', getters.getPreference.region, { root: true })
      commit('control/setMaxAge', getters.getPreference.maxAge, { root: true })
      commit('control/setMinAge', getters.getPreference.minAge, { root: true })
      commit('control/setMaxHeight', getters.getPreference.maxHeight, { root: true })
      commit('control/setMinHeight', getters.getPreference.minHeight, { root: true })
      commit('control/setBody', body, { root: true })
      commit('control/setEducation', education, { root: true })
      commit('control/setJob', job, { root: true })
      commit('control/setReligion', religion, { root: true })
      commit('control/setDrink', getters.getPreference.drink, { root: true })
      commit('control/setSmoke', getters.getPreference.smoke, { root: true })
    }
  },
  actions: {
    login({ commit,state }, res) {
      cookies.set("auth-token", res.data.token);
      state.authToken = res.data.token
      if(res.data.preference) {
        commit("SET_PREFERENCE", res.data.preference)
        commit("SET_PROFILE", res.data.profile)
        commit("initalPreference")
        state.profile_saved = true
        state.image_saved = true
        router.push({name:"Main"})
      }else{
        if (res.data.user.profile_saved === 1) {
          state.profile_saved = true
          commit("SET_PROFILE", res.data.profile)
          if (res.data.user.image_saved === 1){
            state.image_saved = true
            router.push({name:"Main"})
          }else{
            router.push({name:"Upload"})
          }
        }
        else if (res.data.user.profile_saved === 0){
          router.push({name:"UserInfo"})
        }
      }
      // router.push({name:"Loading"})

    },
    addUserInfo({commit,getters},UserData){
      return new Promise((resolve, reject) => {
        axios.post(USERAPI.BASE_URL + '/profiles/', UserData, getters.config)
          .then((res)=>{
            commit("SET_PROFILE", res.data)
            
            resolve()
          })
          .catch(()=>{
            reject()
          })
        })
    },
    updateProfile({getters}, userData) {
      axios.put(`${USERAPI.BASE_URL}/profiles/`, userData, getters.config)
      .then(() => {
        this.userInfo = userData
        alert("수정 완료 되었습니다")
        this.$router.go();
      })
      .catch(err => {
        console.log(err)
      })
  
    },
    setSimilarity({commit}, similarity) {
      commit('SET_SIMILARITY',similarity)
    },
    // initialPreferences({ getters, commit }) {
    //   var initialBodies = getters.getPreference.body;
    //   var initialEdus = getters.getPreference.education;
    //   var initialJobs = getters.getPreference.job;
    //   var initialReligions = getters.getPreference.religion;
    //   var body = []
    //   var education = []
    //   var job = []
    //   var religion = []
    //   for (var initBody of initialBodies) {
    //     body.push(initBody.name)
    //   }
    //   for (var initEdu of initialEdus) {
    //     education.push(initEdu.name)
    //   }
    //   for (var initJob of initialJobs) {
    //     job.push(initJob.name)
    //   }
    //   for (var initReligion of initialReligions) {
    //     religion.push(initReligion.name)
    //   }
    //   commit('control/setRegion', getters.getPreference.region, { root: true })
    //   commit('control/setMaxAge', getters.getPreference.maxAge, { root: true })
    //   commit('control/setMinAge', getters.getPreference.minAge, { root: true })
    //   commit('control/setMaxHeight', getters.getPreference.maxHeight, { root: true })
    //   commit('control/setMinHeight', getters.getPreference.minHeight, { root: true })
    //   commit('control/setBody', body, { root: true })
    //   commit('control/setEducation', education, { root: true })
    //   commit('control/setJob', job, { root: true })
    //   commit('control/setReligion', religion, { root: true })
    //   commit('control/setDrink', getters.getPreference.drink, { root: true })
    //   commit('control/setSmoke', getters.getPreference.smoke, { root: true })
    // }
  },
}
