<template>
  <div class='main'>
    <Header />
    <HeartAnimation />
    <Slider />
  </div>
</template>

<script>
import Slider from "../components/main/Slider"
import HeartAnimation from "../components/main/HeartAnimation"
import Header from "../components/common/Header.vue"
import { mapState } from 'vuex'

export default {
  components: {
    Slider,
    Header,
    HeartAnimation
  },
  computed: {
    ...mapState('user',['userInfo'])
  },
  mounted: function(){
    this.$socket.emit('initialize-socket', {userId: this.userInfo.id, userNickname: this.userInfo.nickname})
  }
}
</script>

<style>
.main {
  background-color: #fefff8;
}
</style>