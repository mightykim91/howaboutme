<template>
  <div class="swiper">
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <v-dialog
          v-model="dialogProfile"
        >
          <ProfileModal @closeModal="dialogProfile = false" :userData="userData" />
        </v-dialog>
        <v-dialog
          v-model="dialogLike"
          width="70vw"
        >
          <LikeModal @closeModal="dialogLike = false" :userData="userData" @like="like" />
        </v-dialog>
        <v-dialog
          v-model="dialogAlreadyLike"
          width="70vw"
        >
          <AlreadyLikeModal @closeModal="dialogAlreadyLike = false" />
        </v-dialog>
          <v-img v-for="(user, idx) in users" :key="idx"
            class='swiper-slide'
            :src=src[idx]
            aspect-ratio="1.2"
          >
            <div :v-model="check"></div>
            <div class='swiper-btns'>
              <v-btn
                class="mx-2"
                fab
                dark
                small
                color="#B2DFDB"
                @click="dialogProfile = true; userData = user;"
              ><i class="fas fa-user main-message"></i>
              </v-btn>
              <div class='swiper-similar'>
                {{ user.user.similarity }}%
              </div>
              <v-btn
                class="mx-2"
                fab
                dark
                small
                color="#EF5350"
                @click="likeBtn(user)"
              >
                <v-icon v-if="user.like" color="lime lighten-3">
                  mdi-heart
                </v-icon>
                <v-icon v-else>
                  mdi-heart
                </v-icon>
              </v-btn>
            </div>
            <div class='swiper-bottom'>
              <h1 class="swiper-bottom-name">{{ user.nickname }}, {{ user.age }} </h1>
              <p class='swiper-bottom-introduce'>{{ user.intro }}</p>
            
            </div>
            </v-img>
          <v-card class='swiper-slide refresh-slide'>
            <div @click='refresh'>
              <img src="@/assets/images/icon/anonymous (1).png">
              <button class="btn-refresh">
                <h2 class="refresh-title">
                  다른 매칭 상대 보기
                </h2>
              </button>
            </div>
            <div class="refresh-content">
              <p>이 버튼을 누르면 현재 매칭 정보는 다시 볼 수 없습니다.</p>
              <p>신중하세요!</p>
            </div>
          </v-card>
      </div>
      <!-- Add Pagination -->
      <div class="swiper-pagination"></div>
    </div>
  </div>
</template>

<script>
import ProfileModal from "../main/ProfileModal"
import LikeModal from "../main/LikeModal"
import AlreadyLikeModal from "../main/AlreadyLikeModal"
import Swiper from 'swiper';
import SwiperCore, { Navigation, Pagination, Scrollbar, A11y, EffectCube, EffectCoverflow } from 'swiper';
// import Swiper styles
import 'swiper/swiper-bundle.css';
import 'swiper/swiper.scss';
import 'swiper/components/navigation/navigation.scss';
import 'swiper/components/pagination/pagination.scss';
import 'swiper/components/scrollbar/scrollbar.scss';
import 'swiper/components/effect-cube/effect-cube.scss';
import axios from "axios"
import UserApi from "@/api/UserApi.js"
import { mapGetters } from 'vuex';

SwiperCore.use([Navigation, Pagination, Scrollbar, A11y, EffectCube, EffectCoverflow ]);

const SERVER_URL = UserApi.BASE_URL

export default {
  components: {
    ProfileModal,
    LikeModal,
    AlreadyLikeModal,
  },
  data() {
    return {
      dialogProfile: false,
      dialogLike: false,
      dialogAlreadyLike: false,
      userData: {},
      src: ["2","2","2","2","2"],
      users: [
        {age:"",area:{id:"",name:""},birth:"",blood:"",body:{id:"",name:""},drink:"",education:{id:"",name:""},gender:"",height:"",hobby1:"",hobby2:"",id:"",intro:"",job:{id:"",name:""},like:false,nicknmae:"",religion:"",smoke:"",user:{id:"",similarity:""}},
        {age:"",area:{id:"",name:""},birth:"",blood:"",body:{id:"",name:""},drink:"",education:{id:"",name:""},gender:"",height:"",hobby1:"",hobby2:"",id:"",intro:"",job:{id:"",name:""},like:false,nicknmae:"",religion:"",smoke:"",user:{id:"",similarity:""}},
        {age:"",area:{id:"",name:""},birth:"",blood:"",body:{id:"",name:""},drink:"",education:{id:"",name:""},gender:"",height:"",hobby1:"",hobby2:"",id:"",intro:"",job:{id:"",name:""},like:false,nicknmae:"",religion:"",smoke:"",user:{id:"",similarity:""}},
        {age:"",area:{id:"",name:""},birth:"",blood:"",body:{id:"",name:""},drink:"",education:{id:"",name:""},gender:"",height:"",hobby1:"",hobby2:"",id:"",intro:"",job:{id:"",name:""},like:false,nicknmae:"",religion:"",smoke:"",user:{id:"",similarity:""}},
        {age:"",area:{id:"",name:""},birth:"",blood:"",body:{id:"",name:""},drink:"",education:{id:"",name:""},gender:"",height:"",hobby1:"",hobby2:"",id:"",intro:"",job:{id:"",name:""},like:false,nicknmae:"",religion:"",smoke:"",user:{id:"",similarity:""}},
        ],
      check: true,
    }
  },
  computed: {
    ...mapGetters({
      config: "user/config"
    }),
  },
  
  methods: {
    like(id) {
      for (var i = 0; i < 5; i++) {
        if(this.users[i].id == id) {
        this.users[i].like = true
        }
      }
    },
    likeBtn(user) {
      if (user.like) {
        this.dialogAlreadyLike = true
      }
      else {
        this.dialogLike = true
      }
      this.userData = user
    },
    swiperDetail() {

    },
    getPartner() {
      axios.get(SERVER_URL+'/profiles/partners/', this.config)
      .then((res) => {
        for (var i=0; i < 5; i++) {
          this.src[i] = `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${res.data[i].nickname}?alt=media`
          this.users[i] = res.data[i]
        }
        this.check = !this.check
      })
      .catch((err) => {
        console.log(err.response)
      })
    },
    refresh() {
      this.$router.go()
    }
  },
  mounted() {
    this.getPartner() 
    new Swiper('.swiper-container', {
      effect: 'coverflow',
      grabCursor: true,
      centeredSlides: true,
      slidesPerView: 'auto',
      coverflowEffect: {
        rotate: 50,
        stretch: 0,
        depth: 400,
        modifier: 1,
        slideShadows: true,
      },
    });
    },
}
</script>

<style lang="scss">
  .swiper {
    font-size: 14px;
    color: #000;
    margin: 0;
    margin-top: 15vh;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 50vh;
    height: 70vh;
  }

  .swiper-container {
    width: 100%;
    padding-top: 50px;
    padding-bottom: 50px;
  }

  .swiper-slide {
    background-position: center;
    background-size: cover;
    width: 80vw;
    height: 70vh;
    background: white;
    border-radius: 10px 10px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 0 0 20px 0 rgb(140, 140, 140);
  }
  .swiper-similar {
    background-color: rgb(30, 30, 30, 0.8);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 20px 20px;
    width: 20vw;
    font-size: 1.2rem;
  }
  .swiper-btns {
    display: flex;
    justify-content: space-around;
    position: absolute;
    bottom: 17vh;
    width: 100%;
  }

  .swiper-bottom {
    position: absolute;
    bottom: 0px;
    width: 100%;
    height: 20vh;
    background-color: white;
    border-radius: 40px 40px 0 0;
    z-index: -1;
  }
  .swiper-bottom-name {
    margin: 1.5rem 0 0 2.2rem;
    text-align: left;
    color: rgb(80, 80, 80);
  }
  .swiper-bottom-introduce {
    margin: 0.5rem 2.2rem 0 2.2rem !important;
    height: 30%;
    overflow: hidden;
    text-align: left;
    color: gray;
    -webkit-line-clamp: 2;
  }

  .main-name {
    margin: 0;
    font-size: 1rem;
    color: #78909C;
  }

  .main-region {
    margin: 0;
    color: gray;
    font-size: 0.8rem;
  }
  
  .main-message {
    font-size: 20px;
  }

  .refresh-slide {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #faeded !important;
    img {
      width: 50%;
    }
    .btn-refresh {    
      // margin-bottom: 12px;
      border-radius: 6px;
      // box-shadow: 3px 3px 30px white;
      outline: none;
      h2 {
        color: #1e1e1ecc;
      }
    }
    p {
      color: rgb(172, 170, 170);
      font-size: 0.7rem;
    }
  }

</style>