<template>
  <div class="container-profile">
    <div class="profile-header">
      <div class="header-background">
        <h2 class="header-title">마이페이지</h2>
        <div class="container-tabs">
          <button id="tab-notifications" class="btn-tab" @click="openNotifications">알림함</button>
          <button id="tab-userinfo" class="btn-tab" @click="openUserInfo">회원정보 수정</button>
        </div>
        </div>
      <div class="header-contents">
        <div class="profile-img">
          <img src="https://lh3.googleusercontent.com/proxy/VP_-0YKTJ5tMzBv3ZyLJ10TKlSA6nXN0FqW8SW-yWT8RC2lJemZC0c_m4dAn7cEjkJcUfC9qw8oLZ-oI-EytNA6yITpHKHNb16W2c9TbI5Bt7otha74Qo-kDxNfrxNQj1pPtgtqxTwGnKL641yYJVXmVj52qEJsVCPqi08XYPoUxQV8QA6kaAZ--PkmoRV4mvnF_7Ktj48cxg2BsVC7IFTgHMZfhqHKZIAyPvLga_0NVZn604FMWO0wyO4pn6rP2_uIQSHRRqze-T7-2NKpcjccvxQdz1T5HXmq2wjXQ8eMzRLLDrFUeazck9JR1G-sYYD1aqQcRBVfNt8e8s2AZ">
          <button class="btn-img"><i class="fas fa-camera"></i></button>
        </div>
      </div>
    </div>
    <div class="profile-body">
      <NotificationBox v-if="showNotifications" />
      <UserInfo v-if="showUserInfo" />
    </div>
  </div>
</template>

<script>
// import LoginInfo from '../components/profile/LoginInfo.vue'
import NotificationBox from "@/components/profile/NotificationBox.vue"
import UserInfo from "@/components/profile/UserInfo.vue"

export default {
  components: {
    NotificationBox,
    UserInfo,
  },
  data() {
    return {
      title: "Profile",
      showNotifications: true,
      showUserInfo: false,
    }
  },
  methods: {
    openNotifications() {
      this.showNotifications = true;
      this.showUserInfo = false;
      document.querySelector("#tab-notifications").style.borderColor = "rgb(241, 195, 195)"
      document.querySelector("#tab-userinfo").style.borderColor = "transparent"
    },
    openUserInfo() {
      this.showNotifications = false;
      this.showUserInfo = true;
      console.log("click")
      document.querySelector("#tab-notifications").style.borderColor = "transparent"
      document.querySelector("#tab-userinfo").style.borderColor = "rgb(241, 195, 195)"
    },
  }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/profile/profile.scss"
</style>