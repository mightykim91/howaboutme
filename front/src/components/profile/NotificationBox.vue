<template>
  <div class="container-notificationBox">
      <!-- <Notification v-for="user in users" :key="user.i" :user="user" /> -->
<<<<<<< HEAD
      <Notification v-for="msg in likeMessages" :key="msg.key" :msg="msg" @clickProfile="onClickProfile" />
=======
      <div v-if="newMessages">
        <Notification v-for="msg in newMessages" :key="msg.key" :msg="msg" @clickProfile="onClickProfile" />
      </div>
>>>>>>> d0c527b981307508477cf50a5b22503aa234fd73
      <v-dialog v-model="showProfile">
        <ProfileModal @closeModal="showProfile=false" :userData="user" />
      </v-dialog>
  </div>
</template>

<script>
import Notification from "./Notification"
import ProfileModal from "@/components/main/ProfileModal"
import { mapGetters } from 'vuex';


export default {
    name: "NotificationBox",
    components: {
        Notification,
        ProfileModal,
    },
    computed: {
      ...mapGetters({
        config: "user/config",
        userId: "user/getUserInfo.id",
        nickname: "user/getUserInfo.nickname"
      })
    },
    data() {
        return {
          showProfile: false,
          user: {},
<<<<<<< HEAD
          users: [
            {
              id: 1,
              src: "https://img1.yna.co.kr/etc/inner/KR/2019/10/16/AKR20191016056700005_01_i_P2.jpg",
              nickname: '천우희',
              age: '34',
              gender: 0,
              birth: "1987.01.04",
              height: 161,
              body: "날씬",
              hobby1: "영화보기",
              hobby2: "멍때리기",
              blood: 'A형',
              religion: '무교',
              smoke: '안함',
              drink: '가끔',
              education: '대학생 이상',
              job: '배우',
              area: '경기도',
              intro: 'HELLO',
            },
            {
              id: 2,
              src: "https://www.newstap.co.kr/news/photo/202001/102741_170863_4955.jpg",
              nickname: '수지',
              age: '28',
              gender: 0,
              birth: "1987.01.04",
              height: 161,
              body: "날씬",
              hobby1: "영화보기",
              hobby2: "멍때리기",
              blood: 'A형',
              religion: '무교',
              smoke: '안함',
              drink: '가끔',
              education: '대학생 이상',
              job: '배우',
              area: '경기도',
              intro: 'HELLO',
            },
            {
              id: 3,
              src: "https://sccdn.chosun.com/news/html/2020/08/22/2020082301001930000129551.jpg",
              nickname: '아이유',
              age: '28',
              gender: 0,
              birth: "1987.01.04",
              height: 161,
              body: "날씬",
              hobby1: "영화보기",
              hobby2: "멍때리기",
              blood: 'A형',
              religion: '무교',
              smoke: '안함',
              drink: '가끔',
              education: '대학생 이상',
              job: '배우',
              area: '경기도',
              intro: 'HELLO',
            },
            {
              id: 4,
              src: "https://lh3.googleusercontent.com/proxy/m9B8jQBoPmKpwUP9fkQVqPKm2BJZ6cJnfiMRxx-R1U7EPxt6DYCcBvwtid5KZhQaMytCX2vBnhCDTBgzlDAoKUhELnC9EwxWF9yS4nfyUcOWeJeiM3Wb8dA",
              nickname: '한소희',
              age: '27',
              gender: 0,
              birth: "1987.01.04",
              height: 161,
              body: "날씬",
              hobby1: "영화보기",
              hobby2: "멍때리기",
              blood: 'A형',
              religion: '무교',
              smoke: '안함',
              drink: '가끔',
              education: '대학생 이상',
              job: '배우',
              area: '경기도',
              intro: 'HELLO',
            },
            {
              id: 5,
              src: "https://img.vogue.co.kr/vogue/2019/05/style_5cc94e4e98ff8.jpg",
              nickname: '사나',
              age: '25',
              gender: 0,
              birth: "1987.01.04",
              height: 161,
              body: "날씬",
              hobby1: "영화보기",
              hobby2: "멍때리기",
              blood: 'A형',
              religion: '무교',
              smoke: '안함',
              drink: '가끔',
              education: '대학생 이상',
              job: '배우',
              area: '경기도',
              intro: 'HELLO',
            },
          ],
          likeMessages: [],
=======
          newMessages: []
>>>>>>> d0c527b981307508477cf50a5b22503aa234fd73
        }
    },
    methods: {
      onClickProfile(user) {
        this.user = user;
        this.showProfile = true;
      }
    },
    // 여기 닉네임으로 받나요?? 
    mounted: function(){
      this.$socket.emit('fetch-like-log', { 'user': this.nickname });
      this.$socket.on('fetch-like-log-reply', likeMessages => {
        const newMsg = Object.values(likeMessages);
        //key가 보낸사람 아이디, value가 메세지 내용
        this.likeMessages = newMsg;
      })
    }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/profile/notification.scss"
</style>