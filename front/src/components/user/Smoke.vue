<template>
  <v-card class="mx-auto">
    <v-card-title class="headline"> 당신의 흡연량은? </v-card-title>
    <v-card-actions class="d-block">
      <div class="submit-btn">
        <button class="btn" value="비흡연" text @click="emitSmoke">
          비흡연
        </button>
        <button class="btn" value="술 마실 때만" text @click="emitSmoke;">
          술 마실 때만
        </button>

        <button class="btn" value="가끔" text @click="emitSmoke;">가끔</button>
        <button class="btn" value="자주" text @click="emitSmoke">자주</button>
        <button class="btn" value="매일" text @click="emitSmoke;">매일</button>
        <button class="btn" value="전자담배" text @click="emitSmoke;">
          전자담배
        </button>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Smoke",

  data() {
    return {
      smoke: "",
      dialog_smoke: true,
    };
  },
  methods: {
    emitSmoke(event) {
      this.smoke = event.target.value;
      // this.dialog_smoke = true;
      this.$emit("getSmoke", this.smoke);
      this.$emit("closeSmoke", this.dialog_smoke);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
