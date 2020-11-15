<template>
  <div v-if="!activeVideoCall && !incomingCall">
    <Title :title="title" />
    <div class='chat'>
      <div class='chat-header'>
        <div class='chat-back'>
          <i class="fas fa-chevron-left" @click="$router.push('/main/message')"></i>
        </div>
        <div class='chat-profile'>
          <v-avatar style='background-color: white;' size='30'>
            <v-img
                src="https://www.popularitas.com/wp-content/uploads/2018/04/user-hero-blue.png"></v-img>
          </v-avatar>
          {{ $route.params.partner }}
        </div>
        <div class='chat-feature'>
          <i class="fas fa-video" @click="activateVideoCall"></i>
        </div>
      </div>
      <div id="app_chat_list" class='chat-content'>
        <!-- <ChatBubble :user=user />
        <ChatBubble :user=emoticon />
        <ChatBubble :user="!user" />
        <ChatBubble :user=user />
        <ChatBubble :user="user" />
        <ChatBubble :user=emoticon />
        <ChatBubble :user="!user" />
        <ChatBubble :user=user /> -->
        <ChatBubble 
        v-for="log in chatlog" 
        v-bind:key="log.id" 
        v-bind:user="user" 
        v-bind:chatlog="log"/>
      </div>
      <div class="chat-input">
        <ChatInput 
        v-bind:partner="partner"
        v-on:update="refreshLogs"
        />
      </div>
    </div>
  </div>
  <div v-else-if="incomingCall == true">
    <VideoChat 
    v-bind:incomingCall="true"
    v-bind:caller="myPartner" 
    v-bind:callee="user"
    v-bind:callerSignal='callerSignal'
    v-bind:isInitiator="isInitiator"
    v-on:endcall="endCall"/>
  </div>
  <div v-else-if="activeVideoCall == true">
    <VideoChat
    v-bind:incomingCall="false" 
    v-bind:caller="user" 
    v-bind:callee="myPartner"
    v-bind:isInitiator="isInitiator" 
    v-on:endcall="endCall"/>
  </div>
</template>

<script>
import ChatBubble from "../components/message/ChatBubble"
import ChatInput from "../components/message/ChatInput"
import VideoChat from "../components/message/VideoChat"
import Title from "../components/common/Title"

export default {
  props: {
    partner: String,
  },
  data() {
    return {
      title:"Message",
      user: "brian",
      myPartner: this.partner,
      emoticon: 'emoticon',
      chatlog: '',
      chats: [],
      unreadCount: 0,
      activeVideoCall: false,
      isInitiator: true,
      incomingCall: false,
      from: false,
      callerSignal: '',
      refreshSignal: false,
    }
  },
  components: {
    ChatBubble,
    ChatInput,
    Title,
    VideoChat,
  },
  methods: {
    // getChat: function(chatlog){
    //   console.log('chatlog function activated')
    //   this.chatlog = chatlog;
    // },
    getUnreadCount: function(count){
      console.log('unread count function activated')
      console.log('unread count: ' + count)
      this.unreadCount = count;
    },
    refreshLogs: function() {
      this.$socket.emit('fetch-chatlog', {'sender': this.user, 'receiver': this.myPartner});
      this.$socket.on('fetch-chatlog-callback', chatlog => {
        console.log('채팅로그 업데이트중')
        this.chatlog = chatlog
        this.refreshSignal = false;
      })
    },
    activateVideoCall: function(){
      this.activeVideoCall = true;
    },
    endCall: function(){
      this.activeVideoCall = false;
      this.incomingCall = false;
    }
  },
  watch: {
    refreshSignal : function(){
        console.log('내가보고있다.')
        if (this.refreshSignal){
          this.refreshLogs();
        }
    }
  },
  updated: function() {
    var objDiv = document.getElementById("app_chat_list");
          // 채팅창 스크롤 바닥 유지
    if (objDiv.scrollHeight != null){
      objDiv.scrollTop = objDiv.scrollHeight;
      }
    else if (objDiv.scrollHeight == null ) {
      console.log('-----SCREEN AT BOTTOM-----')
    }
  },
  created: function() {
      this.$socket.emit('initialize-socket', this.user)
      this.$socket.on('new-message-pre-flight-receiving side', ()=>{
        console.log("#1. preflight success - receiver")
      })
      this.$socket.on('new-message-pre-flight-sender', ()=>{
        console.log("#1. preflight success - sender")
      })
      const chatInfo = {
          'sender': this.user,
          'receiver': this.myPartner
        };
      //Emit event to receieve chat log
      this.$socket.emit('fetch-chatlog', chatInfo);
      this.$socket.on('fetch-chatlog-callback', chatlog => {
        console.log('got fetched data')
        this.chatlog = Object.values(chatlog)
      })

      //Emit event to receive unread message count <= use it when user is not in chat room to alert unread message
      this.$socket.emit('fetch-unread-count', chatInfo);
      this.$socket.on('fetch-unread-count-callback', count => {
        this.getUnreadCount(count);
      })
      
      this.$socket.on('new-message-fin', (newMessage) => {
        console.log('새로운메세지')
        const newChatlog = this.chatlog
        //새로 대화하는 경우 chatlog
        if (!newChatlog) {
          this.chatlog = [newMessage];
        } else {
          newChatlog.push(newMessage)
          this.chatlog = newChatlog
        }
      })

      //Emit event to erase unread message
      this.$socket.emit('read-message', chatInfo);
      
      //incoming call
      this.$socket.on('incoming-call', data => {
            this.incomingCall = true
            this.isInitiator = false
            this.from = data.from
            this.callerSignal = data.signalData
        })
  }
}
</script>

<style>
.chat {
  height: 78vh;
}

.chat-header {
  height: 10%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
  .chat-back {
    width: 15%;
    cursor: pointer;
  }
  .chat-profile {
    text-align: left;
    width: 70%;
  }
  .chat-feature {
    width: 15%;
    cursor: pointer;
  }
.chat-content {
  height: 80%;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.chat-input {
  height: 10%;
  width: 100%;
  background-color: white;
}
</style>