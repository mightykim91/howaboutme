<template>
  <v-card>
    <v-card-title class="headline"> 당신의 닉네임은? </v-card-title>
    <v-card-actions class="d-block">
      <div>
        <v-row>
          <v-col class="py-0 mx-auto col-10">
            <v-text-field
              v-model="nickname"
              filled
              placeholder="닉네임을 입력하세요 :)"
              solo
            ></v-text-field>
          </v-col>
        </v-row>
        <v-btn
          class="info-btn mx-auto my-3"
          color="red lighten-3"
          dark
          @click="emitNickname"
        >
          입력완료
        </v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Nickname",
  data() {
    return {
      dialog_nickname: true,
      nickname: "",
    };
  },
  methods: {
    emitNickname() {
      // this.dialog_nickname = true;
      this.$emit("getNickname", this.nickname);
      this.$emit("closeNickname", this.dialog_nickname);
    },
  },
};
</script>

<style scoped src="@/assets/scss/userinfo.scss" lang="scss">
