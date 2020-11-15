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
                :src="src"></v-img>
          </v-avatar>
          {{ $route.params.partner }}
        </div>
        <div class='chat-feature'>
          <i class="fas fa-video" @click="activeVideoCall=true"></i>
        </div>
      </div>
      <div id="app_chat_list" class='chat-content'>
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
    <video playsInline muted id="my-video" autoPlay></video>
    <button v-if="callAccepted == false" @click="acceptCall">Accept Call</button>
    <video playsInline id="partner-video" autoPlay></video>
  </div>
  <div v-else-if="activeVideoCall == true">
    <p v-for="user in users" v-bind:key="user.id" @click='callPeer(user)'>
        {{user}}
    </p>
    <video playsInline muted id="my-video" autoPlay></video>
    <video playsInline id="partner-video" autoPlay></video>
    <div v-if="users">
    </div>
    <button @click='endCall'>Exit</button>
  </div>
</template>

<script>
import ChatBubble from "../components/message/ChatBubble"
import ChatInput from "../components/message/ChatInput"
import Title from "../components/common/Title"
<<<<<<< HEAD
import Peer from "simple-peer"
=======
import { mapGetters } from 'vuex'

>>>>>>> d0c527b981307508477cf50a5b22503aa234fd73
export default {
  props: {
    partner: String,
  },
  computed: {
    ...mapGetters ({
      nickname: "user/userInfo.nickname"
    }),
    src: `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${this.partner}?alt=media`
  },
  data() {
    return {
      title:"Message",
      user: this.nickname,
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
      stream: '',
      mySocketId: this.$socket.id,
      users: '',
      callAccepted:'',
    }
  },
  components: {
    ChatBubble,
    ChatInput,
    Title,
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
    getStream: (stream) => {
      this.stream = stream
    },
    endCall: function(){
      this.activeVideoCall = false;
      this.incomingCall = false;
      this.stream.getTracks().forEach(function(track){
        track.stop()
      });
    },
    callPeer: function(receiver){
      this.activeVideoCall = true
      navigator.mediaDevices.getUserMedia({audio: false, video: true}).then(stream => {
            this.stream = stream;
            const myvideo = document.querySelector('#my-video')
            if (myvideo) {
              myvideo.srcObject = this.stream
            }
        })
      console.log('Apply for calling')
      const myPeer = new Peer({
          initiator: true,
          trickle: false,
          config: {
              iceServers: [
              {
                  urls: "stun:numb.viagenie.ca",
                  username: "sultan1640@gmail.com",
                  credential: "98376683"
              },
              {
                  urls: "turn:numb.viagenie.ca",
                  username: "sultan1640@gmail.com",
                  credential: "98376683"
              }
              ]
          }, 
          stream: this.stream
      });
      myPeer.on('signal', data => {
          console.log('피어 시그널 시작!')
          const callInfo = {
              caller: this.$socket.id,
              callee: receiver,
              signalData: data
          }
          this.$socket.emit('callUser', callInfo);
      })

      myPeer.on('stream', stream => {
          console.log('스트림수신')
          const partnerVideo = document.querySelector('#partner-video');
          console.log('partner-video-stream')
          console.log(stream)
          if (partnerVideo) {
              partnerVideo.srcObject = stream;
          }
      })

      this.$socket.on('callAccepted', signal => {
          console.log('전화연결됨')
          if (myPeer) {
              console.log(myPeer)
          }
          this.callAccepted = true;
          myPeer.signal(signal);
      })
    },
    acceptCall: function(){
            console.log('answering phone call')
            this.callAccepted = true;
            const myPeer = new Peer({
                initiator: false,
                trickle: false,
                stream: this.stream,
            })

            myPeer.on("signal", data => {
                console.log('accepting call....')
                this.$socket.emit("acceptCall", {signalData: data, caller: this.from}, () => {
                    console.log('acceptCall Event fired!')
                })
            })

            myPeer.on('stream', stream => {
                const partnerVideo = document.querySelector('#partner-video');
                partnerVideo.srcObject = stream
            })

            myPeer.signal(this.callerSignal);
        },
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
        if (chatlog === null || chatlog === undefined){
          console.log('****There is no chats to display****' + new Date())
          this.chatlog = []
        } else {
          console.log('****Fetching chat log completed****' + new Date())
          this.chatlog = Object.values(chatlog)
        }
      })

      //Emit event to receive unread message count <= use it when user is not in chat room to alert unread message
      this.$socket.emit('fetch-unread-count', chatInfo);
      this.$socket.on('fetch-unread-count-callback', count => {
        this.getUnreadCount(count);
      })
      
      this.$socket.on('new-message-fin', (newMessage) => {
        console.log('****새로운 메세지를 수신했습니다.****')
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
            console.log('*****전화가 왔습니다*****')
            this.incomingCall = true
            this.from = data.from
            this.callerSignal = data.signalData
        })
      this.$socket.on('get-socket-id', id => {
          this.mySocketId = id;
          console.log(this.$socket.id)
      })
      this.$socket.on('allUsers', users => {
        this.users = users
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
  /* background-color: rgb(240, 240, 240); */
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