import axios from "axios";
import UserApi from "@/api/UserApi.js"

import cookies from "vue-cookies";
// import router from '@/router';


export default {
  namespaced: true,
  state: {
    profile_saved:false,
    image_saved:false,
    // authToken: cookies.get("auth-token"),
    authToken: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ilx1ZDE0Y1x1YzJhNFx1ZDJiOFx1YWNjNFx1YzgxNTExIiwiZXhwIjoxNjA1ODYyNzM4LCJlbWFpbCI6InRlc3QxMUB0ZXN0LmNvbSIsIm9yaWdfaWF0IjoxNjA1MjU3OTM4fQ.fFSK0Yt9wBNF9F-uRUShbSjQ9AkC8p1DajS2RnsNhA0",
    userInfo: Object,
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
    }
  },
  mutations: {
    SET_UNACTIVE_USER(state, res) {
      cookies.set("auth-token", res.data.token);
    },
    SET_ACTIVE_USER(state, res) {
      cookies.set("auth-token", res.data.token);
      state.userInfo = res.data.profile;
      if (res.data.user.profile_saved === 1){
        state.profile_saved = true
        if (res.data.user.image_saved === 1){
          state.image_saved = true
        }
      }
    },
  },
  actions: {
    login({ commit }, res) {
      if (res.data.user.profile_saved === 1) {
        console.log('프로필정보 있음')
        commit("SET_ACTIVE_USER", res);
        console.log('프로필정보 저장')

        // if (res.data.user.image_saved === 1){
          // router.push({name:"Main"})
        // }else{
          // router.push({name})
          // console.log('사진등록 페이지로 푸쉬')
        // }
      }else if(res.data.user.profile_saved === 0){
        console.log('프로필정보 없음')

        commit("SET_UNACTIVE_USER", res);
        // router.push({name:"Userinfo"})
      }
    },
    updateProfile(userData, getters) {
      axios.put(`${UserApi.BASE_URL}/profiles/`, userData, getters.config)
      .then(res => {
        this.userInfo = userData
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
};
