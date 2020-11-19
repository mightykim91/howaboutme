import Login from "@/views/user/Login.vue";
import Signup from "@/views/user/Signup.vue";
import UserInfo from "@/views/user/UserInfo.vue";
import Upload from "@/views/user/Upload.vue";
import Loading from "@/views/user/Loading.vue";

export default [
  //user
  {
    path: "login",
    name: "Login",
    component: Login,
  },
  {
    path: "signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "userinfo",
    name: "UserInfo",
    component: UserInfo,
  },
  {
    path: "upload",
    name: "Upload",
    component: Upload,
  },
  {
    path: "loading",
    name: "Loading",
    component: Loading,
  },
  ];
  