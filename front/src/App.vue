<template>
  <v-app id="app">
    <router-view />
    <!-- <router-view name="a" /> -->
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {
  },

  data: () => ({
    //
  }),
};
</script>
<style lang="scss">
@font-face { 
  font-family: 'NanumSquareRound'; 
  src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_two@1.0/NanumSquareRound.woff') format('woff'); 
  font-weight: 1000; 
  font-style: normal; }
@import url(https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@1.0/nanumsquare.css);

#app {
  font-family: NanumSquareRound, Avenir, Helvetica, Arial, sans-serif;
  font-weight: 700;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  // width: 375px;
  position: relative;
  margin: auto;
  background-color: white;
  p {
    margin: 0;
  }

}

</style>