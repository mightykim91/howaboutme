<template>
  <v-card class="mx-auto">
    <v-card-title class="headline"> 당신의 종교는? </v-card-title>
    <v-card-actions class="d-block">
      <div class="submit-btn">
        <button class="btn" value="무교" text @click="emitReligion">
          무교
        </button>
        <button class="btn" value="기독교" text @click="emitReligion">
          기독교
        </button>
        <button class="btn" value="불교" text @click="emitReligion">
          불교
        </button>
        <button class="btn" value="천주교" text @click="emitReligion">
          천주교
        </button>
        <button class="btn" value="기타" text @click="emitReligion">
          기타
        </button>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Religion",

  data() {
    return {
      religion: "",
      dialog_religion: true,
    };
  },
  methods: {
    emitReligion(event) {
      this.religion = event.target.value;
      // this.dialog_religion = true;
      this.$emit("getReligion", this.religion);
      this.$emit("closeReligion", this.dialog_religion);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
