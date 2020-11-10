//node server setup
const { EFAULT } = require('constants');
const express = require('express');
const app = express();
const server = require('http').Server(app);
const io = require('socket.io')(server)

//listening on port 3000
server.listen(3000);
app.set('view engine', 'ejs');

//firebase settings
const firebase = require('firebase');
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

let rooms = []

//on socket connection
io.on('connection', (socket) => {
    console.log(`new socket detected, socket id: ${socket.id}`)
    //Emit initial event to retrieve userid
    
    //Socket Id Update **2020.11.10** function confirmed
    socket.on('socket-init', userId => {
      if (rooms.includes(userId)){
        socket.join(userId)
      } else {
        rooms.push(userId)
        socket.join(userId)
      }
      const socketRef = database.ref('/socketId')
      socketRef.once('value').then(function(snapshot) {
        if (snapshot.hasChild(userId)){
          console.log('new user socket id')
          socketRef.child(userId).set(socket.id);
        } else {
          console.log('update previous socket id')
          socketRef.child(userId).set(socket.id)
        }
      })
    })

    //Sending new message **2020.11.10** function confirmed
    socket.on('new-message', messageInfo => {
      console.log('new message detected')
      const date = new Date()
      const today = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate()
      const time = date.getHours() + ':' + date.getMinutes() + ':' + date.getSeconds()
      const messageFormat = {
        'text': messageInfo.text,
        'sender': messageInfo.sender,
        'reciever': messageInfo.reciever,
        'date': today,
        'time': time,
        'isRead': false
      }
      
      checkPartnerSocketId(messageFormat.reciever)

      //check reciver exists in sender's chat log
      const myMessageLogRef = database.ref(`/Logs/${messageInfo.sender}/Receiver`)
      myMessageLogRef.once('value')
      .then(function(snapshot) {
        //if exists add new message
        //and alert reciever
        if (!snapshot.hasChild(messageFormat.reciever)) {
          myMessageLogRef.child(messageFormat.reciever).set('messages')
        }
        const newKey = myMessageLogRef.child(`${messageFormat.reciever}/messages`).push()
        newKey.set(messageFormat).then(function() {
          console.log('message log recordes successfully')
          //Inform sender that message has been updated
          io.to(messageFormat.sender).emit('new-message-fin')
        })
        .catch(function(error){
          console.log(error)
        })
      })
      //Update receiver's message 
      const receiverMessageLogRef = database.ref('/Logs')
      receiverMessageLogRef.once('value')
      .then(function(snapshot){
        console.log(snapshot.val())
        console.log(`if receiver exists: ${snapshot.hasChild(messageFormat.reciever)}`)
        if (!snapshot.hasChild(messageFormat.reciever)) {
          receiverMessageLogRef.child(`${messageFormat.reciever}/Receiver/${messageFormat.sender}/messages`)
          .push().set(messageFormat)
          receiverMessageLogRef.child(`${messageFormat.reciever}/Receiver/${messageFormat.sender}/unread`)
          .set(1)
        } else {
          const receiverKey = database.ref(`Logs/${messageFormat.reciever}/Receiver/${messageFormat.sender}/messages`).push()
          receiverKey.set(messageFormat)
          //update unread message count
          const unReadCountRef = database.ref(`Logs/${messageFormat.reciever}/Receiver/${messageFormat.sender}/unread`)
          unReadCountRef.transaction(function(unread) {
            return unread + 1;
          })
        }
        io.to(messageFormat.reciever).emit('new-message-fin')
      })
    })
    
    //ChatLog fetcher
    socket.on('fetch-chatlog', chatInfo => {
      const sender = chatInfo.sender;
      const receiver = chatInfo.receiver;
      const chatlogRef = database.ref(`/Logs/${sender}/Receiver/${receiver}`)
      chatlogRef.child('messages').once('value').then(function(snapshot) {
        console.log(snapshot.val());
        io.to(sender).emit('fetch-chatlog-callback', snapshot.val())
      })
    })
})

const checkPartnerSocketId = function(partnerId) {
  const socketRef = database.ref('/socketId').child(partnerId)
  socketRef.once('value').then(function(snapshot){
    console.log('partner socket id ' + snapshot.val())
  })
}