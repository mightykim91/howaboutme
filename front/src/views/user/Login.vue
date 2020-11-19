<template>

  <div id="login">
    <div class="nonlogin-slogan d-none d-sm-flex">
      <h2 class="text-center">원활한 서비스 이용을 위해<br>화면 너비를 600픽셀 미만으로 설정해주세요 :)<br /></h2>
    </div>
    <v-form class="d-flex d-sm-none login-form" v-model="valid">
      <v-container>
        <v-row>
          <div class="login-slogan">
            <h2>계정에<br />로그인하세요.</h2>
            <small>더 이상, 사진에 속지 마세요!</small>
          </div>
        </v-row>
        <div class="text-center">
          <img class="login-btn" @click="googleLogin" src="@/assets/images/icon/googlelogin.png">
          <img class="login-btn" @click="kakaoLogin" src="@/assets/images/icon/kakaologin.png">
          <!-- <v-img class="login-btn" @click="naverLogin" src="@/assets/images/icon/naverlogin.png"></v-img> -->
          <!-- <v-btn @click="googleLogin"><img class="login-btn" src="@/assets/images/icon/googlelogin.png"></v-btn>
          <v-btn @click="kakaoLogin"><img class="login-btn" src="@/assets/images/icon/kakaologin.png"></v-btn>
          <v-btn @click="naverLogin"><img class="login-btn" src="@/assets/images/icon/naverlogin.png"></v-btn> -->
        </div>
      </v-container>
    </v-form>
  </div>
</template>
<script>
import KEY from "@/api/SecretKey";
import USERAPI from "@/api/UserApi";
import axios from "axios";
import { mapActions,mapState } from "vuex";

export default {
  name: "Login",
  data() {
    return {};
  },
  methods: {
    ...mapActions('user',['login']),
    ...mapState('user',['profile_saved']),
    googleLogin() {
      // console.log('000')
      axios.get(USERAPI.BASE_URL + "/accounts/login/google/").then((res) => {
        console.log(res.data)
        // window.open(res.data.url);
        location.href=res.data.url
        // this.$router.push({name:"Loading"})
        // this.$router.push(res.data.url)
      });
    },
    naverLogin() {
      axios.get(USERAPI.BASE_URL + "/accounts/login/naver/").then((res) => {
        // window.open(res.data.url)
        // console.log(res.data.url)
        // const request_url = "https://nid.naver.com/oauth2.0/authorize?cliend_id=" + KEY.NAVER_CLIENT_ID + "&redirect_uri=http://localhost:8080/user/login&response_type=code"
        // console.log(request_url)
        location.href=res.data.url
      });
    },
    kakaoLogin() {
      axios.get(USERAPI.BASE_URL + "/accounts/login/kakao/").then((res) => {
        location.href=res.data.url
      });
    },
  },
  created() {
    console.log(this.$route.hash.split("&")[0].split("=")[1]);
    console.log(this.$route.hash.length);
    if (this.$route.query.code !== undefined) {
      console.log(this.$route.query.code.length);
      if (this.$route.query.code.length === 18) {
        // this.$router.push({name:"Loading"})

        // console.log('naver')
        // const headers = {
        //     'Content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        //     'Access-Control-Allow-Origin':'*'
        // }
        // const body = {
        //     'grant_type': 'authorization_code',
        //     'client_id': KEY.NAVER_CLIENT_ID,
        //     'client_secret': KEY.NAVER_SECRET_KEY,
        //     'code': this.$route.query.code,
        //     'state':this.$route.query.state,
        // }
        // // const request_url = 'https://nid.naver.com/oauth2.0/token?'+'grant_type=authorization_code&'+'client_id='+KEY.NAVER_CLIENT_ID+'&client_secret='+KEY.NAVER_SECRET_KEY+'&code='+this.$route.query.code
        // axios.get('https://nid.naver.com/oauth2.0/token',{
        //   headers:headers,
        //   params:body
        // })
        // .then(res => console.log(res))
        // .catch(err => console.log(err.response))
        const body = {
          token: this.$route.hash.split("&")[0].split("=")[1],
        };
        axios
          .post(USERAPI.BASE_URL + "/accounts/login/naver/callback/", body)
          .then((res) => {
            console.log(res);
          });
      } else if (this.$route.query.code.length === 86) {
        console.log("kakao");
        const headers = {
          "Content-type": "application/x-www-form-urlencoded; charset=utf-8",
        };
        const body = {
          grant_type: "authorization_code",
          client_id: KEY.KAKAO_API_KEY,
          redirect_uri: USERAPI.FRONT_BASE_URL + "/user/login",
          code: this.$route.query.code,
        };
        const request_url =
          "https://kauth.kakao.com/oauth/token?" +
          "grant_type=authorization_code&client_id=" +
          KEY.KAKAO_API_KEY +
          "&redirect_uri="+USERAPI.FRONT_BASE_URL+"/user/login&" +
          "code=" +
          this.$route.query.code;
        axios
          .post(request_url, body, headers)
          .then((res) => {
            console.log(res);
            axios
              .post(
                USERAPI.BASE_URL + "/accounts/login/kakao/callback/",
                res.data
              )
              .then((res) => {
                // console.log('hi')
                // console.log(res)
                this.login(res)
                // this.$router.push({name:"Loading"})
              })
              // .then(() => {
              //   console.log('hihi')
              //   if (this.$store.state.profile_saved === true){
              //     console.log(this.$store.state.userInfo)
              //     if (this.$store.state.image_saved === true){
              //       this.$router.push({name:'Main'})
              //     }else{
              //       console.log('사진첩저장')
              //     }
              //   } else{
              //     this.$router.push({name:'Userinfo'})
              //   }
              // });
          })
          .catch((err) => console.log(err.response));
      } else {
        console.log("google");

        const body = {
          code: this.$route.query.code,
          client_id: KEY.GOOGLE_CLIENT_ID,
          client_secret: KEY.GOOGLE_SECRET_KEY,
          redirect_uri: USERAPI.FRONT_BASE_URL + "/user/login",
          grant_type: "authorization_code",
        };
        const headers = {
          "Content-type": "application/x-www-form-urlencoded",
        };
        axios
          .post("https://www.googleapis.com/oauth2/v4/token", body, headers)
          .then((res) => {
            console.log(res);
            axios
              .post(
                USERAPI.BASE_URL + "/accounts/login/google/callback/",
                res.data
              )
              .then((res) => {
                // console.log('hi')
                // console.log(res)
                this.login(res)
                // this.$router.push({name:"Loading"})

              })
              // .then(() => {
              //   console.log('hihi')
              //   if (this.$store.state.profile_saved === true){
              //     console.log(this.$store.state.userInfo)
              //     if (this.$store.state.image_saved === true){
              //       this.$router.push({name:'Main'})
              //     }else{
              //       console.log('사진첩저장')
              //     }
              //   } else{
              //     this.$router.push({name:'Userinfo'})
              //   }
              // });
          });
      }
    } else if (this.$route.hash.length > 0) {
      console.log("hi");
      const body = {
        token: this.$route.hash.split("&")[0].split("=")[1],
      };
      axios
        .post(USERAPI.BASE_URL + "/accounts/login/naver/callback/", body)
        .then((res) => {
          console.log(res);
          this.$cookie.set("token", res.data.token);
        })
        // .then(() => {
        //   window.close();
        // });
    } else {
      console.log("no");
    }
  },
};
</script>
<style scoped src="../../assets/scss/login.scss" lang="scss">
