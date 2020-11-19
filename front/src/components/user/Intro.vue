<template>
  <v-card>
    <v-card-title class="headline">간단하게 당신을 소개해주세요. </v-card-title>
    <v-card-actions class="d-block">
      <div>
        <v-row>
          <v-col class="py-0 px-0 mx-auto col-10">
            <v-textarea
              solo
              name="input-7-4"
              height="150"
              v-model="intro"
              :rules="[rules.length(100)]"
              label="자신을 소개해주세요.(100자)"
            ></v-textarea>
          </v-col>
        </v-row>
        <v-btn
          class="info-btn mx-auto my-3"
          color="red lighten-3"
          dark
          @click="emitIntro"
          v-if="isValid"
        >
          입력완료
        </v-btn>
        <v-btn
          class="info-btn mx-auto my-3 btn-disabled"
          color="#cacaca"
          dark
          v-else
        >
          입력완료
        </v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "intro",
  data() {
    return {
      dialog_intro: true,
      intro: "",
      form: false,
      rules: {
        length: (len) => (v) =>
          (v || "").length < len || `${len}자 이내로 작성해주세요.`,
      },
    };
  },
  computed: {
    isValid() {
      return this.intro.length > 0 && this.intro.length < 101;
    },
  },
  methods: {
    emitIntro() {
      // this.dialog_intro = true;
      this.$emit("getIntro", this.intro);
      this.$emit("closeIntro", this.dialog_intro);
    },
  },
};
</script>

<style scoped src="@/assets/scss/userinfo.scss" lang="scss">
