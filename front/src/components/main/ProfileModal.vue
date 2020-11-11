<template>
  <div>
    <i @click="closeModal" class="far fa-times-circle modal-close"></i>
    <v-card class='profile-modal'>
      <v-img :src="test.src" class="profile-modal-img">
      </v-img>
      <div class='profile-modal-body'>
        <div v-if="state == 'up'">
          <i @click="arrowDown" class="fas fa-arrow-down"></i>
          <!-- <div class="profile-modal-userinfo">
            <div class='character'>
              <div class="icon">
                <i class="far fa-user"></i>
              </div>
              <div class="content">
                천우희
              </div>
            </div>
            <div class='character'>
              <div class="icon">
                <i class="fas fa-id-card-alt"></i>
              </div>
              <div class="content">
                Actor
              </div>
            </div>
            <div class='character'>
              <div class="icon">
                AGE
              </div>
              <div class="content">
                34
              </div>
            </div>
            <div class='character'>
              <div class="icon">
                <i class="fas fa-smoking"></i>
              </div>
              <div class="content">
                No
              </div>
            </div>
          </div> -->
          <div class="profile-modal-userinfo">
            <div style="background-color: rgb(241, 195, 195);">프로필</div>
            <div class="not-about">
              <v-card class='base'>
                <i class="far fa-user icon"></i>
                <div>
                  <div class="each name">
                    {{ test.name }} {{ test.age }}
                  </div>
                  <div class='each height'>
                    <div class='category'>
                      키
                    </div>
                    <div class='content'>
                      161
                    </div>
                  </div>
                  <div class='each religion'>
                    <div class='category'>
                      종교
                    </div>
                    <div class='content'>
                      무교
                    </div>
                  </div>
                  <div class="each birth">
                    <i class="fas fa-birthday-cake category"></i>
                    <div class='content'>1987.04.20</div>
                  </div>
                  <div class="each location">
                    <i class="fas fa-map-marker-alt category"></i>
                    <div class="content">경기도 이천</div>
                  </div>
                </div>
              </v-card>
              <div class='specific'>
                <v-card class='hobby'>
                  취미
                </v-card>
                <v-card class='smoke'>
                  <i class="fas fa-smoking icon category"></i>
                  <div class="">
                    No
                  </div>
                </v-card>
                <v-card class='drink'>
                  <i class="fas fa-beer icon category"></i>
                   2병
                </v-card>
              </div>
            </div>
            <div style="background-color: rgb(241, 195, 195); margin-top: 10px;">자기소개</div>
            <v-card class='about'>
              <div>
                하윙
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
    test: Object,
  },
  data() {
    return {
      state: "up",
      categories: ["Job", "Location", "About"],
      contents: [
        {"Job": 'artist'},
        {"Location": 'Seoul'},
        {"About": "hello i'm"},
      ]
    }
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
  overflow: auto;
}
.profile-modal-userinfo .not-about {
  display: flex;
  height: 80%;
}
.profile-modal-userinfo .base {
  margin: 3px;
  width: 60%;
}
.profile-modal-userinfo .each {
  padding: 5px 0;
}
.profile-modal-userinfo .name {
  font-size: 1.3rem;
}
.profile-modal-userinfo .height {
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
.profile-modal-userinfo .hobby {
  margin: 3px;
  height: 48%;
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
  width: 30%;
  color: rgb(130, 130, 130)
}
.profile-modal-userinfo .content {
  width: 70%;
  font-size: 0.8rem;
}
.profile-modal-userinfo .about {
  margin: 3px;
  height: 40%;
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

.modal-close {
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