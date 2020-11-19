<template>
  <div class="container-notification">
      <div class="notification-header">
        <div class="profile-img">
          <img :src="src" @click="moveToProfile">
          <div class="notification-icon"><i class="fas fa-heart"></i></div>
        </div>
      </div>
      <div class="notification-content">
        <div class='notification-content-body'>
          <span class="notification-username">{{ msg.senderNickName }}</span>님이 호감을 표시하셨습니다.
          <div style="display: flex; jusitfy-content:center; align-items:center; border: gray 2px solid; padding: 2px; border-radius: 1px 1px;" @click="$router.push(`/main/chat/${msg.senderNickName}`)">대화하기</div>
        </div>
        <div class="notification-time">
          1시간 전
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Notification",
    components: {
    },
    data() {
        return {
          showProfile: false,
          user: {},
          src: '',
        }
    },
    props: {
      msg: Object,
    },
    methods: {
      moveToProfile() {
        this.$emit("clickProfile", this.user);
      },
      getUserProfile() {
        axios.get(`https://j3a507.p.ssafy.io/profiles/${this.msg.id}/`, this.config)
        .then (res => {
          this.user = res.data
        })
        .catch (err => {
          console.log(err.response)
        })
      }
    },
    mounted() {
      this.getUserProfile()
      this.src = `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${this.msg.senderNickName}?alt=media`
      console.log(this.msg)
    }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/profile/notification.scss"
</style>