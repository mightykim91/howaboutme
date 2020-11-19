<template>
  <v-layout class='message'
      v-touch="{
        left: () => swipe('Left'),
        right: () => swipe('Right'),
      }"
    >
    <div class='message-each' @click="$router.push(`/main/chat/${room[0]}`)">
      <div class='message-profile-img'>
        <v-avatar style='background-color: white;' class='mx-auto' size='50'>
          <v-img
              :src=src></v-img>
        </v-avatar>
      </div>
      <div class='message-content'>
        <div class='message-content-username'>
          {{ room[0] }}
        </div>
        <div class='message-content-body'>
          {{ recentText }}
        </div>
      </div>
      <div class="message-new">
        <div class="message-new-time">
          {{ recentDate }}
        </div>
        <div v-if="unread > 0" class="message-new-number">
          <v-avatar color="#fca69d" size="20">
            {{ unread }}
          </v-avatar>
        </div>
      </div>
    </div>
    <div class='message-delete hide'>
      <h4 class='text' @click='deleteMessage'>삭제</h4>
    </div>
  </v-layout>

</template>

<script>
import { mapMutations } from 'vuex'

export default {
  props:{
    room: Array,
    number: Number,
  },
  data() {
    return {
      partner: '',
      recentText: '',
      recentDate: '',
      unread: 0,
      src: '',
    }
  },
  computed: {
  },
  methods : {
    ...mapMutations({
        unreadMessageCount: "user/unreadMessageCount"
    }),
    deleteMessage() {
      this.$socket.emit('delete', this.room[0])
    },
    swipe(direction) {
      const message = document.querySelectorAll('.message-delete')[this.number]
      if (direction == "Left") {
        message.classList.remove('hide')
      }
      else {
        message.classList.add('hide')
      }
    }
  },
  mounted: function(){
    console.log(this.room)
    this.unreadMessageCount(this.room[1].unread)
    const recentMsg = this.room[1].messages
    this.unread = this.room[1].unread
    // console.log(Object.values(recentMsg)[0])
    var len = Object.values(recentMsg).length
    console.log("len",len)
    this.partner = Object.values(recentMsg)[0].reciever
    this.recentText = Object.values(recentMsg)[len-1].text
    this.recentDate = Object.values(recentMsg)[0].date
    this.src = `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${this.room[0]}?alt=media`

  }
}
</script>

<style>
.message {
  display: flex;
}
.message-each {
  width: 100%;
  height: 12vh;
  display: flex;
  border: white solid 1px;
  cursor: pointer;
  border-bottom: gray 0.2px solid;
}
.message-profile-img {
  width: 25%;
  display: flex;
  align-items: center;
}
.message-content {
  width: 50%;
}
.message-content-username {
  height: 40%;
  display: flex;
  align-items: flex-end;
  font-size: 0.7rem;
  padding-left: 3px;
}
.message-content-body {
  height: 60%;
  text-align: start;
  font-size: 0.65rem;
}
.message-new {
  width: 25%;
}
.message-new-time {
  height: 40%;
  color: gray;
  font-size: 0.7rem;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}
.message-new-number {
  height: 60%;
  padding: 5px 20px 0 0;
  display: flex;
  justify-content: flex-end;
  font-size: 0.5rem;
  color: white;
}
.message-delete {
  width: 20%;
  background-color: rgb(241, 195, 195);
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 10px 0 0 10px;
}
.message-delete .text {
  color: white;
}
.hide {
  display: none;
}
</style>