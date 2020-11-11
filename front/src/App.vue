<template>
  <v-app id="app">
    <Navbar />
    <router-view />
    <router-view name="a" />
  </v-app>
</template>

<script>
import Navbar from "@/components/common/Navbar.vue";

export default {
  name: "App",

  components: {
    Navbar,
  },

  data: () => ({
    //
  }),
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
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