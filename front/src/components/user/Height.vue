<template>
  <v-card>
    <v-card-title class="headline"> 당신의 키는? </v-card-title>
    <v-card-actions class="d-block">
      <v-container>
        <div>
          <select size="5" class="select" v-model="height">
            <option @click="emitHeight" :key="n" v-for="n in 61" selected>
              {{ n + 139 }}
            </option>
          </select>
        </div>
      </v-container>
    </v-card-actions>
  </v-card>
</template>         

<script>
export default {
  name: "Height",
  data() {
    return {
      dialog_height: true,
      height: "",
      min_height: 140,
      heights: [],
    };
  },
  methods: {
    emitHeight() {
      // this.dialog_height = true;
      this.$emit("getHeight", this.height);
      this.$emit("closeHeight", this.dialog_height);
    },
  },
};
</script>

<style lang="scss" scoped>
@import "../../assets/scss/userinfo.scss",
  "@/assets/scss/controls/heightSelect.scss";
</style>