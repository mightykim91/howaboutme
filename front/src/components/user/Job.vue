<template>
  <v-card class="mx-auto">
    <v-card-title class="headline"> 당신의 직업은? </v-card-title>
    <v-card-actions class="d-block">
      <div class="submit-btn">
        <button class="btn" value="학생" text @click="emitJob">학생</button>
        <button class="btn" value="전문직" text @click="emitJob">전문직</button>
        <button class="btn" value="교육직" text @click="emitJob">교육직</button>
        <button class="btn" value="공무원" text @click="emitJob">공무원</button>
        <button class="btn" value="사업가" text @click="emitJob">사업가</button>
        <button class="btn" value="연구,기술직" text @click="emitJob">
          연구,기술직
        </button>
        <button class="btn" value="군인" text @click="emitJob">군인</button>
        <button class="btn" value="무직" text @click="emitJob">무직</button>
        <button class="btn" value="기타" text @click="emitJob">기타</button>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Job",

  data() {
    return {
      job: "",
      dialog_job: true,
    };
  },
  methods: {
    emitJob(event) {
      this.job = event.target.value;
      // this.dialog_Job = true;
      this.$emit("getJob", this.job);
      this.$emit("closeJob", this.dialog_job);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
