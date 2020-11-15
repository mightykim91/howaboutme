<template>
  <div>
    <div class='like-modal' v-if="state">
      <div class="like-modal-title">
        사용 가능 코인 : {{ coin }} <i class="fas fa-coins"></i>
      </div>
      <div class="like-modal-body">
        <div class='text'><p class='coin'>코인 2개</p>로</div>
        <div class='text'><p class="name">{{ userData.nickname }}</p>님에게</div>
        <div class="text">하트를 보내시겠습니까?</div>
      </div>
      <div class="like-modal-btns">
        <div class="like-modal-obtn" @click="okBtn">
          하트 보내기
        </div>
        <div class="like-modal-xbtn" @click="exitBtn">
          취소

        </div>
      </div>
    </div>
    <div v-else class='like-modal'>
      <div class='like-modal-charge'>
        <i @click="exitBtn" class="far fa-times-circle modal-close"></i>
        <img class="like-modal-sorry" src="../../assets/images/icon/sorry.png" alt="">
        <h2 style="color: gray">Sorry..</h2>
        <div class='text'>코인이 부족하네요..</div>
      </div>
      <div class='like-modal-chargebtn' @click="chargeBtn">충전하기</div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import USERAPI from "@/api/UserApi";
import { mapGetters } from 'vuex';

export default {
  props: {
    userData: Object,
  },
  computed: {
    ...mapGetters({
      config: "user/config",
      user: "user/getUserInfo.id",
      nickname: "user/getUserInfo.nickname"
    })
  },
  data() {
    return {
      coin: 2,
      state: true,
      myId: '',
      myNickname: '',
      //김연수 추가
      partner: this.userData.id,
      // user: 'yeonsu'
    }
  },
  methods: {
    okBtn() {
      if (this.coin > 0) {
        //하트 알람 보내기
        this.$socket.emit('likeAlarm', {senderId: this.myId, senderNickname: this.myNickname ,receiver: this.partner});

        this.coin = this.coin - 2
        document.querySelector('.heart-animation').classList.remove('hide')
        // console.log(this.userData.id)
        axios.post(USERAPI.BASE_URL + "/accounts/like/", { id: this.userData.id} ,this.config)
        .then(() => {
          this.$emit("like", this.userData.id)
        })
        .catch(err => {
          console.log(err.response)
        })
        setTimeout(() => {
          document.querySelector('.heart-animation').classList.add('hide')
        }, 2000);
      this.exitBtn()
      }
      else {
        this.state = false
      }
    },
    chargeBtn() {
      this.coin = this.coin + 10
      this.state = true
    },
    exitBtn() {
      this.state = true
      this.$emit('closeModal')
    }
  },
  mounted() {
    axios.get("https://k3a507.p.ssafy.io:8000/profiles/", this.config)
    .then(res => {
      this.myId = res.data.id
      this.myNickname = res.data.nickname
      console.log(this.myId, this.myNickname)
    })
  }

}
</script>

<style>
.like-modal {
  height: 30vh;
  background-color: white;
  position: relative;
}
.like-modal-title {
  height: 25%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: rgb(230, 230, 230) 2px solid;
  color: gray;
}
.fa-coins {
  margin-left: 5px;
  color: #ffd700;
}
.like-modal-body {
  height: 50%;
  width: 100%;
  margin: auto;
  color: gray;
  font-size: 0.8rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.like-modal-body .text {
  display: flex;
  align-items: flex-end;
}
.like-modal-body .coin {
  color: #80CBC4;
  font-size: 1rem;
}
.like-modal-body .name {
  color: #B2DFDB;
  font-size: 1rem;
  margin-right: 4px !important;
}
.like-modal-btns {
  height: 25%;
  width: 100%;
  display: flex;
}
.like-modal-obtn { 
  width: 50%;
  background-color: #B2DFDB;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}
.like-modal-xbtn {
  width: 50%;
  background-color: #E0E0E0;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.like-modal-sorry {
  width: 60px;
  height: 60px;
  margin-bottom: 10px;
}
.like-modal-charge {
  height: 80%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.like-modal-charge .modal-close {
  color: gray !important;
  background: white;
  font-size: 1.5rem;
  border-radius: 0.7rem 0.7rem;
  position: absolute;
  top: 2vh;
  right: 3vw;
  z-index: 10;
}
.like-modal-charge .text {
  font-size: 0.7rem;
  color: gray;
}
.like-modal-chargebtn {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 20%;
  background-color: #B2DFDB;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>