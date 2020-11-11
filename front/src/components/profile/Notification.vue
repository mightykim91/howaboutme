<template>
  <div class="container-notification">
      <div class="notification-header">
        <div class="profile-img">
          <img src="https://img.insight.co.kr/static/2018/09/22/700/8n6ze13j22kxh0mj9p7f.jpg" @click="moveToProfile">
          <div class="notification-icon"><i class="fas fa-heart"></i></div>
        </div>
      </div>
      <div class="notification-content">
        <!-- <div class='notification-content-username'>
          나연
        </div> -->
        <div class='notification-content-body'>
          <span class="notification-username" @click="moveToProfile">{{ user }}</span>님이 호감을 표시하셨습니다.
        </div>
        <div class="notification-time">
          1시간 전
        </div>
      </div>
  </div>
</template>

<script>
export default {
    name: "Notification",
    data() {
        return {
          user: "태민"
        }
    },
    methods: {
      moveToProfile() {
        console.log("유저페이지로 이동")
      }
    }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/profile/notification.scss"
</style>