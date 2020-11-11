<template>
  <v-card>
    <v-card-title class="card headline"> 당신의 취미는? </v-card-title>
    <v-card-actions class="d-block">
      <v-divider></v-divider>
      <div class="container-btns">
        <v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="영화보기"
              >
                영화보기
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="카페가기"
              >
                카페가기
              </button>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="코인노래방"
              >
                코인노래방
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="수다떨기"
              >
                수다떨기
              </button>
            </div>
          </v-col> </v-row
        ><v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="여행가기"
              >
                여행가기
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="카페가기"
              >
                카페가기
              </button>
            </div>
          </v-col> </v-row
        ><v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="영화보기"
              >
                영화보기
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="춤추기"
              >
                춤추기
              </button>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="맛집 탐방"
              >
                맛집 탐방
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="쇼핑하기"
              >
                쇼핑하기
              </button>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="볼링 치기"
              >
                볼링 치기
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="컴퓨터게임"
              >
                컴퓨터게임
              </button>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="요리하기"
              >
                요리하기
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="운동"
              >
                운동
              </button>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-left btn-body"
                @click="selectOption"
                value="독서하기"
              >
                독서하기
              </button>
            </div>
          </v-col>
          <v-col class="col-6" style="padding: 0px">
            <div class="wrapper-btn">
              <button
                class="btn-right btn-body"
                @click="selectOption"
                value="멍때리기"
              >
                멍때리기
              </button>
            </div>
          </v-col>
        </v-row>
      </div>
      <v-divider></v-divider>
    </v-card-actions>
    <v-btn
      class="info-btn mx-auto my-3"
      color="red lighten-3"
      dark
      @click="emitHobby"
    >
      입력완료
    </v-btn>
  </v-card>
</template>

<script>
export default {
  name: "Hobby",
  data() {
    return {
      selected: [],
    };
  },
  methods: {
    selectOption(event) {
      if (this.selected.includes(event.target.value)) {
        var index = this.selected.indexOf(event.target.value);
        this.selected.splice(index, 1);
        event.target.style.background = "white";
        event.target.style.borderTop = "1px solid rgb(211, 211, 211)";
        event.target.style.borderBottom = "1px solid rgb(211, 211, 211)";
        event.target.style.borderRight = "1px solid rgb(211, 211, 211)";
        event.target.style.color = "#2c3e50";
      } else {
        if (this.selected.length < 2) {
          this.selected.push(event.target.value);
          event.target.style.background = "rgb(252, 166, 157)";
          event.target.style.borderTop = "1px solid rgb(252, 166, 157)";
          event.target.style.borderBottom = "1px solid rgb(252, 166, 157)";
          event.target.style.borderRight = "1px solid rgb(252, 166, 157)";
          event.target.style.color = "white";
        } else {
          //   console.log("2개까지만!");
          alert("취미는 2개까지만 선택가능합니다");
        }
      }
    },
    emitHobby() {
      //   if (this.selected.length < 2) {
      this.dialog_hobby = false;
      this.$emit("getHobby", this.selected);
      this.$emit("closeHobby", this.dialog_hobby);
      //   } else {
      //     alert("취미는 2개까지만 선택가능합니다");
      //   }
    },
  },
};
</script>

<style lang="scss" scoped>
@import "@/assets/scss/controls/hobbyOption.scss", "@/assets/scss/userinfo.scss";
// .btn {
//   padding: 5px 11px !important;
// }
</style>