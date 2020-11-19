<template>
  <div class='chat-input'>
    <Emoticon @addEmoticon="addEmoticon" />
    <div class='chat-input-other'>
      <!-- <i class="fas fa-plus"></i> -->
    </div>
    <div class="chat-input-message" @click="exit">
      <input class="content" type="text" v-model="chat_text" @keypress.enter="sendBtn">
    </div>
    <div class="chat-input-emoticon" @click="emoticonBtn">
      <i class="far fa-grin"></i>
    </div>
    <div class="chat-input-send" @click="sendBtn">
      <i class="fas fa-paper-plane"></i>
    </div>
  </div>
</template>

<script>
import Emoticon from "../message/Emoticon"
import axios from "axios"
import { mapState, mapGetters } from 'vuex'
// import File from "../message/File"
export default {
  props: {
    partner: String
  },
  computed: {
    ...mapState('user',['userInfo']),
    ...mapGetters({
      config: "user/config"
    })
  },
  data() {
    return {
      chat_text: "",
      myId: '',
      myPartner: ''
    }
  },
  components: {
    Emoticon,
    // File,
  },
  mounted() {
    document.querySelector(".content").focus()
    axios.get("https://k3a507.p.ssafy.io:8000/profiles/", this.config)
    .then(res => {
      this.myId = res.data.nickname
      console.log(this.myId)
    })
  },
  methods: {
    emoticonBtn() {
      var emoticon = document.querySelector(".emoticon")
      emoticon.classList.remove("hide")
    },
    exitEmoticon() {
      document.querySelector('.emoticon').classList.add('hide')
    },
    exit() {
      this.exitEmoticon()
    },
    sendBtn() {
      this.exitEmoticon()
      console.log(this.chat_text)
      if (this.chat_text) {
        const messageInfo = {
          'sender': this.myId,
          'reciever': this.partner,
          'text': this.chat_text
        }
        this.$socket.emit('new-message', messageInfo)
        this.textReset()
        document.querySelector(".content").focus()
      }
    },
    addEmoticon(emoticon) {
      const messageInfo = {
        'sender': this.myId,
        'reciever': this.partner,
        'text': emoticon
      }
      this.$socket.emit('new-message', messageInfo)
      this.$socket.on('new-message-fin', () => {
        this.emitUpdate()
      })
    },
    textReset() {
      this.chat_text = ''
    }
  },
}
</script>

<style>
.chat-input {
  display: flex;
  align-items: center;
}
.chat-input-other {
  width: 5%;
  font-size: 1.2rem;
  color: #fca69d;
  cursor: pointer;
}
.chat-input-message {
  width: 60%;
  margin-left: 5%;
  margin-right: 5%;
  text-align: left;
  font-size: 0.8rem;  
  border-bottom: rgb(230, 230, 230) 2px solid;
}
.chat-input-message .content {
  width: 100%;
  outline: none;
}
.chat-input-emoticon {
  width: 12%;
  font-size: 1.25rem;
  color: #fca69d;
  cursor: pointer;
}
.chat-input-send {
  width: 13%;
  font-size: 1.25rem;
  color: #fca69d;
  cursor: pointer;
}
</style>