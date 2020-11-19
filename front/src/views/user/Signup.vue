<template>
  <div id="login">
    <v-form class="login-form" v-model="valid">
      <v-container>
        <v-row>
          <h2 class="login-text">계정에<br />로그인하세요.</h2>
        </v-row>
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              color="white"
              :rules="nameRules"
              label="이름"
              clearable
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              color="white"
              label="비밀번호"
              clearable
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              color="white"
              label="비밀번호 확인"
              clearable
            ></v-text-field>
          </v-col>
        </v-row>
        <div class="text-center">
          <v-btn class="submit-btn" rounded color="black" dark> Login </v-btn>
          <v-btn class="submit-btn" rounded color="white">
            Login with Google
          </v-btn>
        </div>
      </v-container>
    </v-form>
  </div>
</template>
<script>
export default {
  name: "Login",
  data() {
    return {};
  },
};
</script>
<style scoped src="../../assets/scss/login.scss" lang="scss">
