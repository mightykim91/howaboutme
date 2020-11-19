<template>
  <div class='chat-input'>
    <Emoticon @addEmoticon="addEmoticon" />
    <File @addFile="addFile" /> 
     <div class='chat-input-other' @click="fileBtn">
      <i class="fas fa-plus"></i>
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
import File from "../message/File"
export default {
  props: {
    partner: String
  },
  data() {
    return {
      chat_text: "",
      myId: 'yeonsu',
      myPartner: this.partner
    }
  },
  components: {
    Emoticon,
    File,
  },
  methods: {
    emoticonBtn() {
      var emoticon = document.querySelector(".emoticon")
      emoticon.classList.remove("hide")
      this.exitFile()
    },
    fileBtn() {
      var file = document.querySelector(".file")
      file.classList.remove("hide")
      this.exitEmoticon()
    },
    exitEmoticon() {
      document.querySelector('.emoticon').classList.add('hide')
    },
    exitFile() {
      document.querySelector('.file').classList.add('hide')
    },
    exit() {
      this.exitEmoticon()
      this.exitFile()
    },
    sendBtn() {
      this.exitEmoticon()
      if (this.chat_text) {
        const messageInfo = {
          'sender': this.myId,
          'reciever': this.myPartner,
          'text': this.chat_text
        }
        this.$socket.emit('new-message', messageInfo)
        this.$socket.on('new-message-fin', () => {
          console.log('new message saved to database')
          this.$emit('update')
        })
        this.textReset()
      }
    },
    addEmoticon(emoticon) {
      const messageInfo = {
        'sender': this.myId,
        'reciever': this.myPartner,
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
  width: 15%;
  font-size: 1.2rem;
  color: #fca69d;
  cursor: pointer;
}
.chat-input-message {
  width: 60%;
  text-align: left;
  font-size: 0.8rem;
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