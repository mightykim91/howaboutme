<template>
  <v-card class="mx-auto">
    <v-card-title class="headline"> 당신의 주량은? </v-card-title>
    <v-card-actions class="d-block">
      <div class="submit-btn">
        <button class="btn" value="안마심" text @click="emitDrink">
          안마심
        </button>
        <button class="btn" value="가끔" text @click="emitDrink;">가끔</button>
        <button class="btn" value="자주" text @click="emitDrink">자주</button>
        <button class="btn" value="매일" text @click="emitDrink;">매일</button>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Drink",

  data() {
    return {
      drink: "",
      dialog_drink: true,
    };
  },
  methods: {
    emitDrink(event) {
      this.drink = event.target.value;
      // this.dialog_drink = true;
      this.$emit("getDrink", this.drink);
      this.$emit("closeDrink", this.dialog_drink);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
