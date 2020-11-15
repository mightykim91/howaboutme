<template>
  <div class="profile-background"> 
  <div class="container-profile">
    <div class="profile-header">
      <div class="header-background">
        <div class="header-title"><span class="nickname">{{ nickname }}</span></div>
        <div class="container-tabs">
          <button id="tab-notifications" class="btn-tab" @click="openNotifications">알림함</button>
          <button id="tab-userinfo" class="btn-tab" @click="openUserInfo">회원정보 수정</button>
        </div>
      </div>
      <div class="header-contents">
        <div class="profile-img">
          <img :src="myImageURL">
          <button class="btn btn-uploadimg" v-if="showUserInfo" @click="openProfilePic"><i class="fas fa-camera"></i></button>
        </div>
        <div class="img-similarity">
          <!-- 유사도: {{ similarity }}% -->
        </div>
      </div>
    </div>
    <div class="profile-body">
      <NotificationBox v-if="showNotifications" />
      <UserInfo v-if="showUserInfo" />
    </div>
  </div>
  <ProfilePic />
  </div>
</template>

<script>
import { mapGetters } from "vuex";

// import LoginInfo from '../components/profile/LoginInfo.vue'
import NotificationBox from "@/components/profile/NotificationBox.vue"
import UserInfo from "@/components/profile/UserInfo.vue"
import ProfilePic from "@/components/profile/ProfilePic.vue"

export default {
  components: {
    NotificationBox,
    UserInfo,
    ProfilePic,
  },
  data() {
    return {
      showNotifications: true,
      showUserInfo: false,
    }
  },
  computed: {
    ...mapGetters({
      nickname: "user/getNickname",
      // similarity: "user/getSimilarity",
    }),
    myImageURL() {
      // return `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${this.nickname}?alt=media`
      return `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${this.nickname}?alt=media`
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
      document.querySelector("#tab-notifications").style.borderColor = "transparent"
      document.querySelector("#tab-userinfo").style.borderColor = "rgb(241, 195, 195)"
    },
    openProfilePic() {
      document.querySelector(".container-profilepic").classList.remove("hide");
    }
  }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/profile/profile.scss"
</style>