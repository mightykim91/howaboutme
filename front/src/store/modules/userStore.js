import axios from "axios";

import cookies from "vue-cookies";
import USERAPI from "@/api/UserApi"
import router from '@/router';


export default {
  namespaced: true,
  state: {
    profile_saved:false,
    image_saved:false,
    // authToken: cookies.get("auth-token"),
    authToken: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMDIsInVzZXJuYW1lIjoiXHViMGE4XHViM2Q5XHVhZGRjZ29vZ2xlIiwiZXhwIjoxNjA1OTYzOTc5LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNjA1MzU5MTc5fQ.xB_N9qx9AK6GSTx03FnNWhQWgaakg_XqY2Vy8NCQeN0",
    // authToken: null,
    // userInfo: Object,
    userInfo: {
    },
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
        Authorization: `${state.authToken}`,
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
      return state.userInfo.similarity;
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
      state.similarity = similarity
    }
  },
  actions: {
    login({ commit,state }, res) {
      cookies.set("auth-token", res.data.token);
      state.authToken = res.data.token
      if(res.data.preference) {
        commit("SET_PREFERENCE", res.data.preference)
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
      .then(res => {
        this.userInfo = userData
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  
    }
    },
}
