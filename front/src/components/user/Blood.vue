<template>
  <v-card class="mx-auto">
    <v-card-title class="headline"> 당신의 혈액형은? </v-card-title>
    <v-card-actions class="d-block">
      <div class="submit-btn">
        <button class="btn" value="A" text @click="emitBlood">A</button>
        <button class="btn" value="B" text @click="emitBlood">B</button>
        <button class="btn" value="AB" text @click="emitBlood">AB</button>
        <button class="btn" value="O" text @click="emitBlood">O</button>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Blood",

  data() {
    return {
      blood: "",
      dialog_blood: true,
    };
  },
  methods: {
    emitBlood(event) {
      this.blood = event.target.value;
      //   this.dialog_blood = true;
      this.$emit("getBlood", this.blood);
      this.$emit("closeBlood", this.dialog_blood);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
