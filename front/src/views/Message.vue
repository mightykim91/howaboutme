<template>
  <div>
    <Title :title="title" />
    <div class="message-body">
      <div v-if="rooms[0]">
        <MessageEach 
        v-for="(room, idx) in rooms"
        v-bind:room="room" 
        v-bind:key="idx"
        :number="idx"
        />
      </div>
      <div class="message-empty" v-else>
        <img class='icon' src="../assets/images/icon/box.png" alt="">
        <div class='text'>메시지함이 비었습니다.</div>
      </div>
    </div>
  </div>
</template>

<script>
import MessageEach from '../components/message/MessageEach.vue'
import Title from '../components/common/Title'
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      title: 'Message',
      rooms: [],
      user: this.nickname
    }
  },
  computed: {
    ...mapGetters ({
      nickname: "user/userInfo.nickname"
    })
  },
  components: {
    MessageEach,
    Title
  },
  methods: {
  },
  mounted() {
    this.$socket.emit('initialize-socket')
    this.$socket.emit('fetch-chatroom', this.user)
    this.$socket.on('fetch-chatroom-callback', rooms => {
      this.rooms = Object.values(rooms);
    })
    console.log(this.rooms)
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