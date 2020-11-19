<template>
  <div class="container-notificationBox">
      <!-- <Notification v-for="user in users" :key="user.i" :user="user" /> -->
      <div v-if="newMessages[0]">
        <Notification v-for="msg in newMessages" :key="msg.key" :msg="msg" @clickProfile="onClickProfile" />
      </div>
      <div class="notifications-empty" v-else>
        <img class='icon' src="@/assets/images/icon/heart.png" alt="">
        <div class='text'>메시지함이 비었습니다.</div>
      </div>
      <v-dialog v-model="showProfile">
        <ProfileModal @closeModal="showProfile=false" :userData="user" />
      </v-dialog>
  </div>
</template>

<script>
import Notification from "./Notification"
import ProfileModal from "@/components/main/ProfileModal"
import { mapGetters, mapState } from 'vuex';


export default {
    name: "NotificationBox",
    components: {
        Notification,
        ProfileModal,
    },
    computed: {
      ...mapGetters({
        config: "user/config",
      }),
      ...mapState('user',['userInfo'])
    },
    data() {
        return {
          showProfile: false,
          user: {},
          newMessages: []
        }
    },
    methods: {
      onClickProfile(user) {
        this.user = user;
        this.showProfile = true;
      }
    }, 
    mounted: function(){
      console.log(this.userInfo.id)
      this.$socket.emit('fetch-like-log', { 'user': this.userInfo.id });
      this.$socket.on('fetch-like-log-reply', likeMessages => {
        console.log(likeMessages)
        const newMsg = Object.values(likeMessages);
        //key가 보낸사람 아이디, value가 메세지 내용
        this.newMessages = newMsg;
      })
    }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/profile/notification.scss"
</style>