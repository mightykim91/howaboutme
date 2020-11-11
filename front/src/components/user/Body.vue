<template>
  <v-card class="mx-auto">
    <v-card-title class="headline"> 당신의 체형은? </v-card-title>
    <v-card-actions>
      <div class="submit-btn">
        <button class="btn" value="마른" text @click="emitBody">마른</button>
        <button class="btn" value="슬림 근육" text @click="emitBody;">
          슬림 근육
        </button>
        <button class="btn" value="보통" text @click="emitBody">보통</button>
        <button class="btn" value="근육질" text @click="emitBody;">
          근육질
        </button>
        <button class="btn" value="통통" text @click="emitBody;">통통</button>
        <button class="btn" value="우람" text @click="emitBody;">우람</button>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Body",

  data() {
    return {
      body: "",
      dialog_body: true,
    };
  },
  methods: {
    emitBody(event) {
      this.body = event.target.value;
      //   this.dialog_body = true;
      this.$emit("getBody", this.body);
      this.$emit("closeBody", this.dialog_body);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
