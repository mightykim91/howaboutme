<template>
  <div>
    <Header />
    <Slider />
  </div>
</template>

<script>
import Slider from "../components/main/Slider"
import Header from "../components/common/Header.vue"
export default {
  components: {
    Slider,
    Header
  },
  mounted: function(){
    this.$socket.emit('initialize-socket', 'brian')
  }
}
</script>

<style>

</style>