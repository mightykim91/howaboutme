import {database} from './socket.js';
import {v4 as uuidv4} from 'uuid';

export default class webRTC {

    constructor(userInfo, socket, io){
        this.caller = userInfo.caller;
        this.callee = userInfo.callee;
        this.socket = socket;
        this.io = io;
    }
    //방생성
    isRoomExist(){
        const roomNumberRef = database.ref(`/Logs/${caller}/Receiver/${callee}/videochatroom`);
        roomNumberRef.once('value').then(function(snapshot) {
            const roomNumber = snapshot.val();
            if (roomNumber != null) {
                return roomNumber;
            } else {
                const newRoomNumber = uuidv4();
                roomNumberRef.set(newRoomNumber);
                return newRoomNumber;
            }
        })
    };
    
    joinRoom(){
        const roomNumber = this.isRoomExist();
        this.socket.join(roomNumber);
    }
}