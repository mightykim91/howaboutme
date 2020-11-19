<template>
    <div v-if="incomingCall == false">
        <video playsInline muted id="my-video" autoPlay></video>
        <video v-if="callAccepted == true" playsInline id="partner-video" autoPlay></video>
        <p v-if="calling == true">전화를 거는 중</p>
        <button @click='exit'>Exit</button>
    </div>
    <div v-else-if="incomingCall == true">
        <button v-if="callAccepted == false" @click="acceptCall">Accept Call</button>
        <!-- <div v-else>
            <video playsInline muted id="my-video" autoPlay></video>
            <video v-if="callAccepted == true" playsInline id="partner-video" autoPlay></video>
        </div> -->
    </div>
</template>

<script>
const Peer = require('simple-peer');
//const {v4:uuidv4} = require('uuid');

export default {
    props: {
        incomingCall: Boolean,
        isInitiator: Boolean,
        caller:String,
        callee:String,
        callerSignal:Object,
    },
    data(){
        return {
            stream: '',
            calling: false, 
            callAccepted: false,
            from: '',
        }
        
    },
    methods: {
        setStream: function(stream){
            const myVideo = document.querySelector('#my-video');
            this.stream = stream;
            if (myVideo) {
                myVideo.srcObject = stream;
            }
        },
        callPeer: function(){
            console.log('Apply for calling')
            const myPeer = new Peer({
                initiator: true,
                trickle: false,
                config: {
                    // iceServers: [
                    // {
                    //     urls: "stun:numb.viagenie.ca",
                    //     username: "sultan1640@gmail.com",
                    //     credential: "98376683"
                    // },
                    // {
                    //     urls: "turn:numb.viagenie.ca",
                    //     username: "sultan1640@gmail.com",
                    //     credential: "98376683"
                    // }
                    // ]
                }, 
                stream: this.stream
            });
            myPeer.on('signal', data => {
                console.log('피어 시그널 시작!')
                const callInfo = {
                    caller: this.caller,
                    callee: this.callee,
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
                if (myPeer()) {
                    console.log(myPeer())
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
                this.$socket.emit("acceptCall", {signalData: data, caller: this.caller}, () => {
                    console.log('acceptCall Event fired!')
                })
            })

            myPeer.on('stream', stream => {
                const partnerVideo = document.querySelector('#partner-video');
                partnerVideo.srcObject = stream
            })

            myPeer.signal(this.callerSignal);
        },

        exit: function(){
            this.$emit('endcall');
            this.stream.getTracks().forEach(function(track){
                track.stop();
            })
        }
        
    },
    mounted: function(){
        navigator.mediaDevices.getUserMedia({audio: false, video: true}).then(stream => {
            this.setStream(stream);
        })

        if (this.isInitiator) {
            console.log(`${this.caller}가 ${this.callee}에게 화상통화 연결을 요청합니다.`)
            this.calling = true
            this.callPeer()
        }
    }
}
</script>

<style>

</style>