<template>
  <div class="swiper">
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <v-dialog
          v-model="dialog"
        >
          <ProfileModal @closeModal="dialog = false" :test="test" />
        </v-dialog>
        <v-img v-for="user in users" :key="user.i"
          class='swiper-slide'
          :src=user.src
          aspect-ratio="1.2"
          @click="dialog = true; test = user;"
        >
          <div class='swiper-btns'>
            <v-btn
              class="mx-2"
              fab
              dark
              small
              color="green"
              @click="$router.push('/chat/test')"
            ><i class="fas fa-comment main-message"></i>
            </v-btn>
            <div class='swiper-similar'>
              78%
            </div>
            <v-btn
              class="mx-2"
              fab
              dark
              small
              color="pink"
              @click="likeBtn"
            >
              <v-icon v-if="like" color="yellow">
                mdi-heart
              </v-icon>
              <v-icon v-else>
                mdi-heart
              </v-icon>
            </v-btn>
          </div>
          <div class='swiper-bottom'>
            <h1 class="swiper-bottom-name">{{ user.name }}, {{ user.age }} </h1>
            <p class='swiper-bottom-introduce'>이곳은 자기소개를 작성하는 곳입니다.</p>
          </div>
          </v-img>
      </div>
      <!-- Add Pagination -->
      <div class="swiper-pagination"></div>
    </div>
  </div>
</template>

<script>
import ProfileModal from "../main/ProfileModal"
import Swiper from 'swiper';
import SwiperCore, { Navigation, Pagination, Scrollbar, A11y, EffectCube, EffectCoverflow } from 'swiper';
// import Swiper styles
import 'swiper/swiper-bundle.css';
import 'swiper/swiper.scss';
import 'swiper/components/navigation/navigation.scss';
import 'swiper/components/pagination/pagination.scss';
import 'swiper/components/scrollbar/scrollbar.scss';
import 'swiper/components/effect-cube/effect-cube.scss';

SwiperCore.use([Navigation, Pagination, Scrollbar, A11y, EffectCube, EffectCoverflow ]);

export default {
  components: {
    ProfileModal
  },
  data() {
    return {
      like: false,
      dialog: false,
      test: {},
      users: [
        {
          src: "https://img1.yna.co.kr/etc/inner/KR/2019/10/16/AKR20191016056700005_01_i_P2.jpg",
          name: '천우희',
          age: '34',
        },
        {
          src: "https://www.newstap.co.kr/news/photo/202001/102741_170863_4955.jpg",
          name: '수지',
          age: '28',
        },
        {
          src: "https://sccdn.chosun.com/news/html/2020/08/22/2020082301001930000129551.jpg",
          name: '아이유',
          age: '28',
        },
        {
          src: "https://lh3.googleusercontent.com/proxy/m9B8jQBoPmKpwUP9fkQVqPKm2BJZ6cJnfiMRxx-R1U7EPxt6DYCcBvwtid5KZhQaMytCX2vBnhCDTBgzlDAoKUhELnC9EwxWF9yS4nfyUcOWeJeiM3Wb8dA",
          name: '한소희',
          age: '27',
        },
        {
          src: "https://img.vogue.co.kr/vogue/2019/05/style_5cc94e4e98ff8.jpg",
          name: '사나',
          age: '25',
        },
      ]
    }
  },
  
  methods: {
    likeBtn() {
      this.like = !this.like
      console.log(this.like)
    },
    swiperDetail() {

    }
  },
  mounted() {
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
        loop: true,

      });
    },
}
</script>

<style>
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
    margin: 1.4rem 0 0 2.2rem;
    text-align: left;
    color: rgb(80, 80, 80);
  }
  .swiper-bottom-introduce {
    margin: 0.5rem 2.2rem 0 2.2rem !important;
    text-align: left;
    color: gray;
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

</style>