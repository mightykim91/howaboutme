<template>
  <v-card>
    <v-card-title class="headline"> 활동 지역은 어디인가요? </v-card-title>
    <v-card-actions class="d-block">
      <v-container>
        <div>
          <select class="mb-4 select" v-model="area">
            <option selected>모든 지역</option>
            <option>서울</option>
            <option>경기도</option>
            <option>부산</option>
            <option>인천</option>
            <option>대구</option>
            <option>대전</option>
            <option>광주</option>
            <option>울산</option>
            <option>세종시</option>
            <option>충청남도</option>
            <option>충청북도</option>
            <option>경상남도</option>
            <option>경상북도</option>
            <option>전라남도</option>
            <option>전라북도</option>
            <option>강원도</option>
            <option>제주도</option>
          </select>
          <v-btn
            class="info-btn mx-auto my-3"
            color="red lighten-3"
            dark
            @click="emitArea"
          >
            입력완료
          </v-btn>
        </div>
      </v-container>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Birth",
  data() {
    return {
      dialog_area: true,
      area: "",
    };
  },
  methods: {
    emitArea() {
      // this.dialog_area = true;
      this.$emit("getArea", this.area);
      this.$emit("closeArea", this.dialog_area);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../assets/scss/userinfo.scss",
  "@/assets/scss/controls/selectBox.scss";
</style>