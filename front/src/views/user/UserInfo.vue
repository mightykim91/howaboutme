<template>
  <div>
    <Title :title="title" />
    <div class="my-5 mx-auto" style="max-width: 300px">
      <v-row class="my-2" justify="center">
        <v-btn
          height="38px"
          width="300px"
          rounded
          color="deep-orange lighten-5"
          dark
          @click.stop="dialog_gender = true"
        >
          <div class="info-key">성별</div>
          <div class="info-value">
            {{ this.UserData.gender }}
          </div>
        </v-btn>
        <v-dialog v-model="dialog_gender" max-width="280">
          <Gender @closeGender="closeGender" @getGender="getGender" />
        </v-dialog>
      </v-row>
      <v-row class="my-2" justify="center">
        <v-btn
          height="38px"
          style="margin: 0 auto"
          width="300px"
          rounded
          color="deep-orange lighten-5"
          dark
          @click.stop="dialog_birth = true"
        >
          <div class="info-key">생일</div>
          <div class="info-value">
            {{ this.UserData.birth }}
          </div>
        </v-btn>
        <v-dialog v-model="dialog_birth" max-width="280">
          <Birth @closeBirth="closeBirth" @getBirth="getBirth" />
        </v-dialog>
      </v-row>
      <v-row class="my-2" justify="center">
        <v-btn
          height="38px"
          width="300px"
          rounded
          color="deep-orange lighten-5"
          dark
          @click.stop="dialog_nickname = true"
        >
          <div class="info-key">닉네임</div>
          <div class="info-value">
            {{ this.UserData.nickname }}
          </div>
        </v-btn>
        <v-dialog v-model="dialog_nickname" max-width="280">
          <Nickname @closeNickname="closeNickname" @getNickname="getNickname" />
        </v-dialog>
      </v-row>
      <v-row class="my-2" justify="center">
        <v-btn
          height="38px"
          width="300px"
          rounded
          color="deep-orange lighten-5"
          dark
          @click.stop="dialog_area = true"
        >
          <div class="info-key">관심지역</div>
          <div class="info-value">
            {{ this.UserData.area }}
          </div>
        </v-btn>
        <v-dialog v-model="dialog_area" max-width="280">
          <Area @closeArea="closeArea" @getArea="getArea" />
        </v-dialog>
      </v-row>
      <v-row class="my-2" justify="center">
        <v-btn
          height="38px"
          width="300px"
          rounded
          color="deep-orange lighten-5"
          dark
          @click.stop="dialog_hobby = true"
        >
          <div class="info-key">취미</div>
          <div v-if="this.hobbies.length === 1" class="info-value">
            {{ this.UserData.hobby1 }}
          </div>
          <div v-if="this.hobbies.length === 2" class="info-value">
            {{ this.UserData.hobby1 }}, {{ this.UserData.hobby2 }}
          </div>
        </v-btn>
        <v-dialog v-model="dialog_hobby" max-width="280">
          <Hobby @closeHobby="closeHobby" @getHobby="getHobby" />
        </v-dialog>
      </v-row>
      <v-divider class="my-3 mb-2"></v-divider>
      <v-row justify="center">
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_height = true"
          >
            <div class="info-key">키</div>
            <div class="info-value info-value-half">
              {{ this.UserData.height }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_height" max-width="280">
            <Height @closeHeight="closeHeight" @getHeight="getHeight" />
          </v-dialog>
        </v-col>
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_blood = true"
          >
            <div class="info-key">혈액형</div>
            <div class="info-value info-value-half">
              {{ this.UserData.blood }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_blood" max-width="280">
            <Blood @closeBlood="closeBlood" @getBlood="getBlood" />
          </v-dialog>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_religion = true"
          >
            <div class="info-key">종교</div>
            <div class="info-value info-value-half">
              {{ this.UserData.religion }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_religion" max-width="280">
            <Religion
              @closeReligion="closeReligion"
              @getReligion="getReligion"
            />
          </v-dialog>
        </v-col>
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_drink = true"
          >
            <div class="info-key">음주</div>
            <div class="info-value info-value-half">
              {{ this.UserData.drink }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_drink" max-width="280">
            <Drink @closeDrink="closeDrink" @getDrink="getDrink" />
          </v-dialog>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_smoke = true"
          >
            <div class="info-key">흡연</div>
            <div class="info-value info-value-half">
              {{ this.UserData.smoke }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_smoke" max-width="280">
            <Smoke @closeSmoke="closeSmoke" @getSmoke="getSmoke" />
          </v-dialog>
        </v-col>
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_education = true"
          >
            <div class="info-key">학력</div>
            <div class="info-value info-value-half">
              {{ this.UserData.education }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_education" max-width="280">
            <Education
              @closeEducation="closeEducation"
              @getEducation="getEducation"
            />
          </v-dialog>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_body = true"
          >
            <div class="info-key">체형</div>
            <div class="info-value info-value-half">
              {{ this.UserData.body }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_body" max-width="280">
            <Body @closeBody="closeBody" @getBody="getBody" />
          </v-dialog>
        </v-col>
        <v-col class="px-0 py-1 col-6">
          <v-btn
            height="38px"
            width="140px"
            rounded
            color="deep-orange lighten-5"
            dark
            @click.stop="dialog_job = true"
          >
            <div class="info-key">직업</div>
            <div class="info-value info-value-half">
              {{ this.UserData.job }}
            </div>
          </v-btn>
          <v-dialog v-model="dialog_job" max-width="280">
            <Job @closeJob="closeJob" @getJob="getJob" />
          </v-dialog>
        </v-col>
      </v-row>
      <v-row class="my-1 mb-1" justify="center">
        <v-btn
          width="300px"
          height="60px"
          rounded
          color="deep-orange lighten-5"
          dark
          @click.stop="dialog_intro = true"
        >
          <div class="info-key">간단 자기소개</div>
          <div class="info-value info-value-intro">
            {{ this.UserData.intro }}
          </div>
        </v-btn>
        <v-dialog v-model="dialog_intro" max-height="100" max-width="280">
          <Intro @closeIntro="closeIntro" @getIntro="getIntro" />
        </v-dialog>
      </v-row>
      <!-- <v-btn
        width="300px"
        class="info-btn mx-auto my-1"
        color="red lighten-3"
        dark
        v-if="isValid"
        @click="emitUserInfo"
      >
        다음
      </v-btn>
      <v-btn
        style="
          height: 48px;
          width: 48px;
          position: fixed;
          top: 30px;
          right: 20px;
        "
        color="#F27F7F"
        fab
        dark
        v-else
        @click="emitUserInfo"
      >
        다음
      </v-btn> -->
      <v-btn
        width="300px"
        height="38px"
        rounded
        class="info-btn mx-auto my-3"
        color="#DDDDDD"
        dark
        @click="emitUserInfo"
      >
        다음
      </v-btn>
    </div>
  </div>
</template>

<script>
import Title from "../../components/common/Title";

import Gender from "../../components/user/Gender.vue";
import Birth from "../../components/user/Birth.vue";
import Nickname from "../../components/user/Nickname.vue";
import Area from "../../components/user/Area.vue";
import Hobby from "../../components/user/Hobby.vue";
import Height from "../../components/user/Height.vue";
import Blood from "../../components/user/Blood.vue";
import Religion from "../../components/user/Religion.vue";
import Drink from "../../components/user/Drink.vue";
import Smoke from "../../components/user/Smoke.vue";
import Education from "../../components/user/Education.vue";
import Body from "../../components/user/Body.vue";
import Job from "../../components/user/Job.vue";
import Intro from "../../components/user/Intro.vue";

export default {
  components: {
    Title,
    Gender,
    Birth,
    Nickname,
    Area,
    Hobby,
    Height,
    Blood,
    Religion,
    Drink,
    Smoke,
    Education,
    Body,
    Job,
    Intro,
  },
  name: "Userinfo",
  data() {
    return {
      title: "프로필등록",
      UserData: {
        gender: "",
        birth: "",
        nickname: "",
        area: "",
        hobby1: "",
        hobby2: "",
        height: "",
        blood: "",
        religion: "",
        drink: "",
        smoke: "",
        education: "",
        body: "",
        job: "",
        intro: "",
      },
      hobbies: [],
      dialog_gender: true,
      dialog_birth: false,
      dialog_nickname: false,
      dialog_area: false,
      dialog_hobby: false,
      dialog_height: false,
      dialog_blood: false,
      dialog_religion: false,
      dialog_drink: false,
      dialog_smoke: false,
      dialog_education: false,
      dialog_body: false,
      dialog_job: false,
      dialog_intro: false,
    };
  },
  computed: {
    isValid() {
      return (
        this.UserData.gender &&
        this.UserData.birth &&
        this.UserData.nickname &&
        this.UserData.area &&
        this.UserData.hobby1 &&
        this.UserData.height &&
        this.UserData.blood &&
        this.UserData.religion &&
        this.UserData.drink &&
        this.UserData.smoke &&
        this.UserData.education &&
        this.UserData.body &&
        this.UserData.job &&
        this.UserData.intro
      );
    },
  },
  methods: {
    emitUserInfo() {
      if (this.isValid) {
        console.log("요청보내기!");
      } else {
        alert("모든 항목은 필수입니다.");
      }
    },
    getGender(gender) {
      this.UserData.gender = gender;
    },
    closeGender() {
      this.dialog_gender = false;
      this.dialog_birth = true;
    },
    getBirth(birth) {
      this.UserData.birth = birth;
    },
    closeBirth() {
      this.dialog_birth = false;
      this.dialog_nickname = true;
    },
    getNickname(nickname) {
      this.UserData.nickname = nickname;
    },
    closeNickname() {
      this.dialog_nickname = false;
      this.dialog_area = true;
    },
    getArea(area) {
      this.UserData.area = area;
    },
    closeArea() {
      this.dialog_area = false;
      this.dialog_hobby = true;
    },
    getHobby(hobbies) {
      this.hobbies = hobbies;
      this.UserData.hobby1 = hobbies[0];
      this.UserData.hobby2 = hobbies[1];
    },
    closeHobby() {
      this.dialog_hobby = false;
      this.dialog_height = true;
    },
    getHeight(height) {
      this.UserData.height = height;
    },
    closeHeight() {
      this.dialog_height = false;
      this.dialog_blood = true;
    },
    getBlood(blood) {
      this.UserData.blood = blood;
    },
    closeBlood() {
      this.dialog_blood = false;
      this.dialog_religion = true;
    },
    getReligion(religion) {
      this.UserData.religion = religion;
    },
    closeReligion() {
      this.dialog_religion = false;
      this.dialog_drink = true;
    },
    getDrink(drink) {
      this.UserData.drink = drink;
    },
    closeDrink() {
      this.dialog_drink = false;
      this.dialog_smoke = true;
    },
    getSmoke(smoke) {
      this.UserData.smoke = smoke;
    },
    closeSmoke() {
      this.dialog_smoke = false;
      this.dialog_education = true;
    },
    getEducation(education) {
      this.UserData.education = education;
    },
    closeEducation() {
      this.dialog_education = false;
      this.dialog_body = true;
    },
    getBody(body) {
      this.UserData.body = body;
    },
    closeBody() {
      this.dialog_body = false;
      this.dialog_job = true;
    },
    getJob(job) {
      this.UserData.job = job;
    },
    closeJob() {
      this.dialog_job = false;
      this.dialog_intro = true;
    },
    getIntro(intro) {
      this.UserData.intro = intro;
    },
    closeIntro() {
      this.dialog_intro = false;
    },
  },
  watch: {},
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
