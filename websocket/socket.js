//node server setup
const { EFAULT } = require('constants');
const express = require('express');
const app = express();
const cors = require('cors');
const {v4:uuidv4} = require('uuid');


app.set('view engine', 'ejs');

const server = require('http').Server(app);
const io = require('socket.io')(server, {
  cors: {
    //
    // origin: 'http://k3a507.p.ssafy.io',
    origin: true,
    methods: ['GET', 'POST']
  }
});
//TEST
//server.listen(8000);

//DEPLOY
server.listen(3030);

app.get('/', function(req, res) {
 res.json({message: "welcome to websocket for ssafy 507"})
})
//firebase settings
const firebase = require('firebase');
const { triggerAsyncId } = require('async_hooks');
const firebaseConfig = {
    apiKey: "AIzaSyD9WPO1cEjEfezvW2pkT40ePYLfCk_PDVU",
    authDomain: "chatlogs-84503.firebaseapp.com",
    databaseURL: "https://chatlogs-84503.firebaseio.com",
    projectId: "chatlogs-84503",
    storageBucket: "chatlogs-84503.appspot.com",
    messagingSenderId: "805207672985",
    appId: "1:805207672985:web:7dbc9a8f6c5432b5661008",
    measurementId: "G-2BGTLCPGZF"
  };
firebase.initializeApp(firebaseConfig);
const database = firebase.database();

let socketId = {}
let socketByNickName = {}
let sockets = {}
//on socket connection
io.on('connection', (socket) => {
    console.log(`new socket detected, socket id: ${socket.id}`)
    socket.emit('get-socket-id', socket.id)
    if (!sockets[socket.id]) {
        sockets[socket.id] = socket.id;
    }
    var USER_ID = ''
    var USER_NICKNAME = ''

    io.sockets.emit('allUsers',sockets)

    socket.on('disconnect', ()=>{
      console.log(`${socket.id} disconnected`)
      delete sockets[socket.id];
    })

    socket.on('initialize-socket', data => {
      console.log(data)
      if (data === undefined || data === null){
        console.log("DATA IS MISSING")
      }
      else {
        const userId = data.userId;
        USER_ID = data.userId;
        USER_NICKNAME = data.userNickname
        const userNickname = data.userNickname
        console.log('------INITIALIZING SOCKET------')
        if (userId === undefined || userId === null) {
          console.log('INITIALIZATION ERROR: missing user id')
        }
        else {
          socketId[userId] = socket.id
          socketByNickName[userNickname] = socket.id
          socket.join(userId)
          const rooms = io.sockets.adapter.rooms
          if (rooms.has(userId)) {
            console.log(`CONFIRMED: ${userId} is in ${userId}`)
          }
        }
        console.log('------INITIALIZING SOCKET FINISHED------')
        console.log(USER_ID, USER_NICKNAME)
    }
    })
    
    //Function for new message
    //Sending new message **2020.11.10** function confirmed
    socket.on('new-message', messageInfo => {
      //Pre-flight event emit
      io.to(socketId[messageInfo.reciever]).emit('new-message-pre-flight-receiving side')
      io.to(socketId[messageInfo.sender]).emit('new-message-pre-flight-sender')

      const date = new Date()
      const today = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate()
      const time = date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
      const messageFormat = {
        'text': messageInfo.text,
        'sender': messageInfo.sender,
        'receiver': messageInfo.reciever,
        'date': today,
        'time': time,
        'isRead': false
      }
      console.log('------The following new message detected------')
      console.log(messageFormat)
      //check receiver exists in sender's chat log
      const myMessageLogRef = database.ref(`/Logs/${messageInfo.sender}/Receiver`)
      myMessageLogRef.once('value')
      .then(function(snapshot) {
        //Empty User Error Handler
        if (messageFormat.sender === undefined || messageFormat.receiver === undefined) {
          console.log('ERROR: user is undefined. Check sender is logged in')
        }
        else if (!snapshot.hasChild(messageFormat.receiver)) {
          myMessageLogRef.child(messageFormat.receiver).set('messages')
        }
        let senderMessageFormat = messageFormat
        senderMessageFormat.isRead = true
        const newKey = myMessageLogRef.child(`${messageFormat.receiver}/messages`).push()
        newKey.set(senderMessageFormat)
        //io.to(socketId[messageFormat.sender]).emit('new-message-fin')
      })
      .catch(function(error) {
        console.log('writting to sender database failed.')
      })
      //Update receiver's message 
      const receiverMessageLogRef = database.ref('/Logs')
      receiverMessageLogRef.once('value')
      .then(function(snapshot){
        if (messageFormat.sender === undefined || messageFormat.receiver === undefined) {
          console.log('ERROR: user is undefined. Check sender is logged in')
        }
        else if (!snapshot.hasChild(messageFormat.receiver)) {
          receiverMessageLogRef.child(`${messageFormat.receiver}/Receiver/${messageFormat.sender}/messages`)
          .push().set(messageFormat)
          receiverMessageLogRef.child(`${messageFormat.receiver}/Receiver/${messageFormat.sender}/unread`)
          .set(1)
        } else {
          const receiverKey = database.ref(`Logs/${messageFormat.receiver}/Receiver/${messageFormat.sender}/messages`).push()
          receiverKey.set(messageFormat)
          //update unread message count
          const unReadCountRef = database.ref(`Logs/${messageFormat.receiver}/Receiver/${messageFormat.sender}/unread`)
          unReadCountRef.transaction(function(unread) {
            return unread + 1;
          })
        }
        
        if (messageFormat.sender != undefined && messageFormat.receiver != undefined) {
          io.to(socketByNickName[messageFormat.sender]).to(socketByNickName[messageFormat.receiver]).emit('new-message-fin', messageFormat)
        }
      })
      .catch(function(error){
        console.log('writting to receiver database failed.')
      })
    })
    
    //채팅 로그 가져오기
    socket.on('fetch-chatlog', chatInfo => {
      console.log(`------FETCHING CHAT LOG OF ${USER_NICKNAME} WITH ${chatInfo.receiver}------`)
      const sender = chatInfo.sender;
      const receiver = chatInfo.receiver;
      const chatlogRef = database.ref('/Logs/' + sender + '/Receiver/' + receiver)
      chatlogRef.child('messages').once('value').then(function(snapshot) {
        console.log(snapshot.val())
        io.to(socketByNickName[USER_NICKNAME]).emit('fetch-chatlog-callback', snapshot.val())
        //socket.emit('fetch-chatlog-callback', snapshot.val())
      })
      .catch(function(error){
        console.log('ERROR: chatlog fetching error')
      })
      console.log('------END OF CHAT LOG FETCH------')
    });

    //Unread message count fetcher
    socket.on('fetch-unread-count', chatInfo => {
      console.log('------FETCHING UREAD MESSAGE COUNT------')
      const sender = chatInfo.sender;
      const receiver = chatInfo.receiver;
      const unreadRef = database.ref(`/Logs/${sender}/Receiver/${receiver}/unread`)
      unreadRef.once('value').then(function(snapshot) {
        console.log('unread value: ' + snapshot.val())
        io.to(socketByNickName[sender]).emit('fetch-unread-count-callback', snapshot.val());
      })
      console.log('------END OF UNREAD MESSAGE COUNT------')
    });

    //function to read all messages
    socket.on('read-message', chatInfo => {
      console.log('------START OF READING ALL MESSAGES------')
      const sender = chatInfo.sender;
      const receiver = chatInfo.receiver;
      const unreadRef = database.ref(`/Logs/${sender}/Receiver/${receiver}/unread`)
      unreadRef.transaction(function(unread){
        return unread*0;
      })

      //Mark all messages to read.
      const messageRef = database.ref(`/Logs/${sender}/Receiver/${receiver}/messages`)
      messageRef.once('value').then(function(snapshot){
        snapshot.forEach(function(childSnapshot){
          const isReadRef = messageRef.child(childSnapshot.key + '/isRead')
          isReadRef.transaction(function(isRead){
            return isRead = true
          })
        })
      })
      .catch(function(error){
        console.log('------ERROR: READING ALL MESSAGES ERROR: ' + error)
      })
      console.log('------END OF READING ALL MESSAGES------')
    })

    //채팅방 fetcher
    socket.on('fetch-chatroom', user => {
      console.log('------FETCHING USERS ALL CHAT ROOM------' + user)
      const chatRoomRef = database.ref(`/Logs/${USER_NICKNAME}/Receiver`)
      chatRoomRef.once('value').then(function(snapshot){
        io.to(socketByNickName[USER_NICKNAME]).emit('fetch-chatroom-callback', {rooms: snapshot.val()});
      })
      .catch(function(error){
        console.log('------ERROR: FETCHING ALL CHAT ROOM ERROR: ' + error);
      })
    });

    //영상통화 발신시 발동되는 함수
    socket.on('callUser', data => {
      console.log("got a call request")
      const caller = data.caller; const callee = data.callee; const signal = data.signalData;
      console.log(caller + " is calling " + data.callee)
      console.log(sockets[callee])
      console.log(sockets)
      io.to(sockets[callee]).emit('incoming-call', {signalData: signal, from: caller});
    })

    socket.on('acceptCall', data => {
      const signal = data.signalData; const to = data.caller;
      console.log(`${to}에게 연결되었다고 알리기`)
      console.log(sockets[to])
      io.to(sockets[to]).emit('callAccepted', signal)
    })

    //좋아요 알림 DB저장 함수
    //경로: FROM (LikeModal) TO (NavBar)
    socket.on('likeAlarm', data => {
      //좋아요 보낸 유저
      console.log(`------RECEIVED LIKE ALARM FROM ${data.sender}, WHO LIKES ${data.receiver}------`)
      const sender = data.senderId;
      const nickname = data.senderNickname;
      //받는사람
      const receiver = data.receiver;
      //Front의 NavBar로 전송할 내용
      const alarmInfo = {
        'fromId': sender,
        'fromNickName': nickname,
        'receiver': receiver
      }
      //받는사람한테 보내기
      io.to(socketByNickName[receiver]).emit('incoming-like-alarm');

      //TEST용 전소켓 메세지
      //io.sockets.emit('incoming-like-alarm')
      //DB에 저장
      const likeRef = database.ref(`/Logs/${receiver}/`)
      const message = {
          text: `${sender}님이 당신을 좋아합니다.`,
          isRead: false,
          senderId: `${sender}`,
          senderNickName: `${nickname}`
        }
      likeRef.once('value').then(function(snapshot) {
        if (!snapshot.hasChild('likeLog')){
        likeRef.set('likeLog')
        likeRef.child(`likeLog/${sender}`).set(message)
        } else {
          likeRef.child(`likeLog/${sender}`).set(message)
        }
      })
      .catch(function(error){
        console.log('ERROR: SAVING LIKE ALARM TO DATABASE FAILED' + error)
      })
      console.log('------FINISHED SENDING LIKE ALARM TO RECEIVER------')
    });

    //좋아요 메세지 로그 호출 함수
    socket.on('fetch-like-log', data => {
      console.log(`------FETCHING LIKE MESSAGE LOG: ${USER_ID}------`)
      const user = data.user;
      //const user = 'suzi';
      if (user) {
        const logRef = database.ref(`Logs/${USER_ID}/likeLog`)
        logRef.once('value').then(function(snapshot) {
          if (snapshot.val() === null || snapshot.val() === undefined){
            console.log(`------NO DATA------`)
          } else {
            const likeLogArray = Object.values(snapshot.val())
            console.log(likeLogArray)
            io.to(socketId[USER_ID]).emit('fetch-like-log-reply', likeLogArray)
            //io.sockets.emit('fetch-like-log-reply', likeLogArray)
            console.log('------FINISHED FETCHING LIKE MESSAGE LOG------')
          }
        })
        .catch(function(error){
          console.log('ERROR: FETCHING LIKE MESSAGE LOG ERROR: ' + error)
        })
      }
      else {
        console.log('ERROR: FETCHING MESSAGE LOG ERROR => USER IS NOT PRESENTED')
      }
    })
})

