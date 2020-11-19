<template>
  <div>
    <i @click="closeModal" class="far fa-times-circle profile-modal-close"></i>
    <v-card class='profile-modal'>
      <v-img :src="src" class="profile-modal-img">
      </v-img>
      <div class='profile-modal-body'>
        <div v-if="state == 'up'">
          <i @click="arrowDown" class="fas fa-arrow-down"></i>
          <div class="profile-modal-userinfo">
            <div style="background-color: rgb(241, 195, 195);">프로필</div>
            <div class="not-about">
              <v-card class='base'>
                <div>
                  <div class="each titlea">
                    <h2 class="name">
                      {{ userData.nickname }}
                    </h2>
                    <div class="age">
                      {{ userData.age }}
                    </div>
                    <!-- <div class='blood'>
                      {{ userData.blood }}
                    </div> -->
                  </div>
                  <div class='each height'>
                    <div class='category'>
                      키
                    </div>
                    <div class='content'>
                      {{ userData.height }}
                    </div>
                  </div>
                  <div class='each job'>
                    <div class='category'>
                      직업
                    </div>
                    <div class='content'>
                      {{ userData.job.name }}
                    </div>
                  </div>
                  <div class='each body'>
                    <div class='category'>
                      체형
                    </div>
                    <div class='content'>
                      {{ userData.body.name }}
                    </div>
                  </div>
                  <div class='each religion'>
                    <div class='category'>
                      종교
                    </div>
                    <div class='content'>
                      {{ userData.religion.name }}
                    </div>
                  </div>
                  <div class="each birth">
                    <i class="fas fa-birthday-cake category"></i>
                    <div class='content'>{{ userData.birth }}</div>
                  </div>
                  <div class="each location">
                    <i class="fas fa-map-marker-alt category"></i>
                    <div class="content">{{ userData.area.name }}</div>
                  </div>
                </div>
              </v-card>
              <div class='specific'>
                <v-card class='hobby'>
                  <div class="titlea category">
                    취미
                  </div>
                  <div class="content">
                  {{ userData.hobby1 }}

                  </div>
                  <div class="content">
                    {{ userData.hobby2 }}

                  </div>
                </v-card>
                <v-card class='smoke'>
                  <i class="fas fa-smoking icon category"></i>
                  <div class="content">
                      {{ userData.smoke }}
                  </div>
                </v-card>
                <v-card class='drink'>
                  <i class="fas fa-beer icon category"></i>
                  <div class="content">
                   {{ userData.drink }}
                  </div>
                </v-card>
              </div>
            </div>
            <div style="background-color: rgb(241, 195, 195); margin-top: 10px;">자기소개</div>
            <v-card class='about'>
              <div class='intro'>
                {{ userData.intro }}
              </div>
            </v-card>
          </div>
        </div>
        <div v-else @click="arrowUp" class='arrow-up'>
          <i class="fas fa-arrow-up"></i>
          <h3 class='arrow-up'>프로필 보기</h3>
        </div>
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    userData: Object,
    nickname: String,
  },
  data() {
    return {
      state: "up",
      categories: ["Job", "Location", "About"],
      contents: [
        {"Job": 'artist'},
        {"Location": 'Seoul'},
        {"About": "hello i'm"},
      ],
      src: `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${ this.nickname }?alt=media`
    }
  },
  computed: {
  },
  methods: {
    closeModal() {
      this.$emit('closeModal')
      this.arrowUp()
    },
    arrowDown() {
      document.querySelector(".profile-modal-img").style.height = "78vh"
      document.querySelector(".profile-modal-body").style.height = "7vh"
      this.state = "down"
    },
    arrowUp() {
      document.querySelector(".profile-modal-img").style.height = "40vh"
      document.querySelector(".profile-modal-body").style.height = "45vh"
      this.state = "up"
    }
  },
  watch: {
    nickname() {
      this.src =  `https://firebasestorage.googleapis.com/v0/b/focused-zephyr-294413.appspot.com/o/${ this.nickname }?alt=media`
    }
  }
}
</script>

<style>
.profile-modal {
  padding: 5px;  
  border-radius: 20px 20px !important;
  height: 100% ;
}
.profile-modal-img {
    border-radius: 20px 20px !important;
    background-position: center;
    background-size: cover;
    width: 100vw;
    height: 40vh;
    /* background: white; */
    position: relative;
    display: flex;
    padding: 1rem;
}
.profile-modal-body {
  position: relative;
  top: -40px;
  background-color: white;
  height: 45vh;
  border-radius: 40px;
  padding: 0 1rem;
}
.profile-modal-userinfo {
  width: 100%;
  padding: 1vh;
  height: 42vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
.profile-modal-userinfo .not-about {
  display: flex;
  min-height: 80%;

}
.profile-modal-userinfo .base {
  margin: 3px;
  width: 60%;
}
.profile-modal-userinfo .each {
  padding: 3px 0;
}
.profile-modal-userinfo .titlea {
  display: flex;
  justify-content: center;
}
.profile-modal-userinfo .titlea .name {
  font-size: 1rem !important;
}
.profile-modal-userinfo .titlea .age {
  padding-left: 10px;
  font-size: 0.8rem;
  color: gray;
  display: flex;
  align-items: flex-end;
}
.profile-modal-userinfo .titlea .blood {
  position: absolute;
  right: 0;
  padding-right: 10px;
  font-size: 1rem;
}
.profile-modal-userinfo .height {
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .job {
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .body {
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .religion {
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .birth {
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .location {
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .specific {
  width: 40%;
}
.profile-modal-userinfo .specific content {
  font-size: 1rem;
}
.profile-modal-userinfo .hobby {
  margin: 3px;
  height: 48%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.profile-modal-userinfo .hobby .titlea {
  font-size: 1rem;
  color: black;
  margin-bottom: 4px;

}
.profile-modal-userinfo .smoke {
  margin: 3px;
  height: 23%;
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .drink {
  margin: 3px;
  height: 23%;
  display: flex;
  align-items: center;
}
.profile-modal-userinfo .category {
  width: 40%;
  color: rgb(130, 130, 130)
}
.profile-modal-userinfo .content {
  width: 70%;
  font-size: 0.8rem;
}
.profile-modal-userinfo .about {
  margin: 3px;
  min-height: 40%;
  display: flex;
  text-align: start;
  align-items: center;
  padding: 10px;
}
.profile-modal-userinfo .icon {
  font-size: 1.3rem;
  margin: 10px;
}
/* .profile-modal-userinfo {
  width: 100%;
  padding: 1vh;
  height: 42vh;
}
.profile-modal-userinfo .character {
  height: 16%;
  display: flex;
  align-items: center;
  width: 90%;
  margin: auto;
  border-bottom: rgb(210, 210, 210) 2px solid;
}
.profile-modal-userinfo .icon {
  width: 30%;
  font-size: 1.2rem;
}
.profile-modal-userinfo .content {
  width: 70%;
  text-align: left;
} */

.profile-modal-close {
  color: gray !important;
  background: white;
  font-size: 2rem;
  border-radius: 0.9rem 0.9rem;
  position: absolute;
  top: 5vh;
  right: 3vw;
  z-index: 10;
}
.fa-arrow-down {
  padding: 0.7rem;
  font-size: 1.4rem;
  color: gray;
  width: 100%;
}
.fa-arrow-up {
  padding: 0.7rem;
  font-size: 1.4rem;
  color: gray;
}
.arrow-up {
  color: gray;
}
</style>