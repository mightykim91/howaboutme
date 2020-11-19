<template>
  <v-card class="mx-auto">
    <v-card-title class="headline"> 당신의 성별은? </v-card-title>
    <v-card-actions class="d-block">
      <div class="submit-btn">
        <button class="btn" value="여자" text @click="emitGender">여자</button>
        <button class="btn-male" value="남자" text @click="emitGender">
          남자
        </button>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Gender",

  data() {
    return {
      gender: "",
      dialog_gender: true,
    };
  },
  methods: {
    emitGender(event) {
      this.gender = event.target.value;
      // this.dialog_gender = true;
      this.$emit("getGender", this.gender);
      this.$emit("closeGender", this.dialog_gender);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
