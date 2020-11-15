<template>
  <div class="navbar">
      <div class="container-navbar">
          <div class="navbar-item">
              <button class="navbar-btn" @click="moveToMain">
                <!-- <img class="navbar-btn-img" src="@/assets/images/navbar/home.png" alt=""> -->
                <homeSVG v-if="!mainActive" />
                <homefilledSVG v-if="mainActive" />
              </button>
          </div>
          <div class="navbar-item">
              <button class="navbar-btn" @click="moveToChat">
                <!-- <img class="navbar-btn-img" src="@/assets/images/navbar/chat.png" alt=""> -->
                <chatSVG v-if="!chatActive" />
                <chatfilledSVG v-if="chatActive" />
              </button>
              <div class="unread-meesage" v-if="unreadMessage">
                <div>{{ unreadMessage }}</div>
              </div>
              <div v-else>
              </div>
          </div>
          <div class="navbar-item">
              <button class="navbar-btn" @click="moveToProfile">
                <!-- <img class="navbar-btn-img" src="@/assets/images/navbar/user.png" alt=""> -->
                <profileSVG v-if="!profileActive" />
                <profilefilledSVG v-if="profileActive" />
                <i class="navbar-heart fas fa-heart" v-if="unreadSignal"></i>
              </button>
          </div>
      </div>
  </div>
</template>

<script>
import homeSVG from "@/components/image_svg/homeSVG.vue"
import chatSVG from "@/components/image_svg/chatSVG.vue"
import profileSVG from "@/components/image_svg/profileSVG.vue"
import homefilledSVG from "@/components/image_svg/homefilledSVG.vue"
import chatfilledSVG from "@/components/image_svg/chatfilledSVG.vue"
import profilefilledSVG from "@/components/image_svg/profilefilledSVG.vue"

export default {
    name: "Navbar",
    components: {
      homeSVG,
      chatSVG,
      profileSVG,
      homefilledSVG,
      chatfilledSVG,
      profilefilledSVG,
    },
    data() {
      return {
        mainActive: true,
        chatActive: false,
        profileActive: false,
        unreadMessageCount: 4,
        unreadSignal: false,
      }
    },
    computed: {
      unreadMessage() {
        var count = this.unreadMessageCount
        if (count > 99) {
          count = "99+"
        }
        return count 
      }
    },
    methods: {
      moveToMain() {
        this.$router.push("/main")
        this.mainActive = true;
        this.chatActive = false;
        this.profileActive = false;
      },
      moveToChat() {
        this.$router.push("/main/message")
        this.mainActive = false;
        this.chatActive = true;
        this.profileActive = false;
      },
      moveToProfile() {
        this.$router.push("/main/profile")
        this.mainActive = false;
        this.chatActive = false;
        this.profileActive = true;
        this.unreadSignal = false;
      },
    },
<<<<<<< HEAD
    created: function() {
      this.$socket.on('incoming-like-alarm', () => {
        this.unreadSignal = true;
=======
    mounted: function() {
      this.$socket.on('incoming-like-alarm', (data) => {
        console.log(data)
        if (data) {
          this.unreadSignal = true;
        }
>>>>>>> d0c527b981307508477cf50a5b22503aa234fd73
      })
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/main/navbar.scss";
</style>