<template>
  <div class="home">
    <div class="home-title">
      <div class='header'>
        나는 어때
      </div>
      <div class='content'>
        더 이상, 사진에 속지 마세요 !
      </div>
      <div class='border'></div>
    </div>
    <div class="home-content">
      <div class="animation">
        <img class='man' src="../assets/images/icon/man.png" alt="">
        <div class="small-heart hide">
          <div class="small-heart-l"></div>
          <div class="small-heart-r"></div>
        </div>
        <img class='woman' src="../assets/images/icon/woman.png" alt="">
      </div>
    </div>
    <div class="home-footer">
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { mapGetters } from 'vuex';

export default {
  name: 'Home',
  components: {
  },
  data() {
    return {

    }
  },
  methods: {
    start() {
      setTimeout(() => {
        document.querySelector('.small-heart').classList.remove('hide')
      }, 2200);
        setTimeout(() => {
          this.$router.push('/user/login')
        }, 3500);
      }
  },
  computed: {
    ...mapGetters({
      isLoggedIn: "user/isLoggedIn"
    }) 
  },
  mounted() {
    this.start()
  }
}
</script>
<style>
@font-face {
    font-family: 'KOTRA_BOLD-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.1/KOTRA_BOLD-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
  .home {
    font-family: 'KOTRA_BOLD-Bold';
    width: 100vw;
    height: 100vh;
    background-color: rgb(241, 195, 195);
  }
  .home-title {
    width: 100%;
    height: 50%;
    /* padding: 1rem; */
    /* background-color: red; */
    color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
  }
  .home-title .header {
    color: rgb(255, 255, 220);
    font-size: 4rem;
  }
  .home-title .content {
    font-size: 0.9rem;
  }
  .home-title .border {
    margin-top: 20px;
    width: 10%;
    border-bottom: rgb(255, 255, 220) 2px solid;
  }
  .home-content {
    width: 100%;
    height: 35%;
    margin-top: 20px;
    /* background-color: blue; */
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .home-content .animation {
    position: relative;
    display: flex;
    align-items: flex-end;
    width: 60%;
    height: 6vh;
    /* background-color: white; */
    /* border-bottom: rgb(255, 255, 210) 2px solid; */
  }
  .home-content .animation .man {
    position: absolute;
    left: -10%;
    width: 60px;
    height: 60px;
    animation-name: man-move;
    animation-duration: 2s;
    animation-delay: 0.5s;
    animation-fill-mode: forwards;
  }
  .home-content .animation .woman {
    position: absolute;
    right: -10%;
    width: 60px;
    height: 60px;
    animation-name: woman-move;
    animation-duration: 2s;
    animation-delay: 0.5s;
    animation-fill-mode: forwards;
  }
  @keyframes beat {
    50% {
      transform: rotate(45deg) scale(1.3);
    }
  }
  @keyframes man-move {
    from {
      left: -10%;
    }
    to {
      left: 24%;
    }
  }
  @keyframes woman-move {
    from {
      right: -10%;
    }
    to {
      right: 18%;
    }
  }
  .hide {
    display: none;
  }
  .small-heart {
    z-index: 100;
    background-color: #EF5350;
    height: 20px;
    width: 20px;
    position: absolute;
    left: 48%;
    top: -80%;
    transform: rotate(45deg);
    animation: beat 1s infinite;
  }
  .small-heart-l {
    background-color: #EF5350;
    height: 10px;
    width: 20px;  
    position: relative;
    border-radius: 20px 20px 0 0;
    bottom: 10px;
  }
  .small-heart-r {
    background-color: #EF5350;
    height: 10px;
    width: 20px;
    position: relative;
    border-radius: 20px 20px 0 0;
    bottom: 5px;
    right: 15px;
    transform: rotate(-90deg);
    
  }
  .home-footer {
    width: 100%;
    height: 15%;
    /* background-color: green; */
  }
</style>