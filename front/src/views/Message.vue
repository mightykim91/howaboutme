<template>
  <div>
    <Title :title="title" />
    <div class="message-body">
      <div v-if="rooms">
        <MessageEach 
        v-for="(room, idx) in rooms"
        v-bind:room="room" 
        v-bind:key="idx"
        :number="idx"
        />
      </div>
      <div v-else class="message-empty">
        <img class='icon' src="../assets/images/icon/box.png" alt="">
        <div class='text'>메시지함이 비었습니다.</div>
      </div>
    </div>
  </div>
</template>

<script>
import MessageEach from '../components/message/MessageEach.vue'
import Title from '../components/common/Title.vue'
import { mapState } from 'vuex'

export default {
  data() {
    return {
      rooms: [],
    }
  },
  computed: {
    ...mapState ('user',['userInfo']),
    title() {
      return 'Message'
    } 
  },
  components: {
    MessageEach,
    Title
  },
  methods: {
  },
  mounted() {
    this.$socket.emit('fetch-chatroom', this.userInfo.nickname)
    this.$socket.on('fetch-chatroom-callback', rooms => {
      Object.fromEntries(Object.entries(rooms).map(([key, value]) => {
        this.rooms.push([key, value])
      }))
    })
    // this.$socket.emit('initialize-socket', {userId: this.userInfo.id, userNickname: this.userInfo.nickname})
  }

}
</script>

<style>
.message-body {
  height: 78vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.message-empty .icon {
  margin: 50% 0px 10% 0px;
  width: 30%;
  height: 30%;
}
.message-empty .text {
  color: gray;
}
</style>