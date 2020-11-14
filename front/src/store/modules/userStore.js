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
    // authToken: "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Ilx1ZDE0Y1x1YzJhNFx1ZDJiOFx1YWNjNFx1YzgxNTExIiwiZXhwIjoxNjA1ODYyNzM4LCJlbWFpbCI6InRlc3QxMUB0ZXN0LmNvbSIsIm9yaWdfaWF0IjoxNjA1MjU3OTM4fQ.fFSK0Yt9wBNF9F-uRUShbSjQ9AkC8p1DajS2RnsNhA0",
    authToken: null,
    // userInfo: Object,
    userInfo: {},
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
    }
  },
  actions: {
    login({ commit,state }, res) {
      router.push({name:"Loading"})
      cookies.set("auth-token", res.data.token);
      state.authToken = res.data.token
      if(res.data.preference) {
        commit("SET_PREFERENCE", res.data.preference)
      }else{
        if (res.data.user.profile_saved === 1) {
          state.profile_saved = true
          commit("SET_PROFILE", res.data.profile);
          if (res.data.user.image_saved === 1){
            state.image_saved = true
            router.push({name:"Main"})
          }else{
            router.push({name:"Upload"})
          }
        }
        // else if(res.data.user.profile_saved === 0){
        //   console.log('프로필정보 없음')
        //   commit("SET_UNACTIVE_USER", res);
        //   // router.push({name:"Userinfo"})
        // }
      }
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

    updateProfile(userData, getters) {
      axios.put(`${USERAPI.BASE_URL}/profiles/`, userData, getters.config)
      .then(res => {
        this.userInfo = userData
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
  
    }
  }
}
