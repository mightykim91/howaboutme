<template>
  <div class='title'>
    <img src="../../assets/images/title/flower.png" alt="">
    <h2 class='title-text'>{{ title }}</h2>
  </div>
</template>

<script>
export default {
  props: {
    title: String
  }
}
</script>

<style scoped>
@font-face {
    font-family: 'KOTRA_BOLD-Bold';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-10-21@1.1/KOTRA_BOLD-Bold.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
.title {
  height: 12vh;
  display: flex;
  background-color: rgb(241, 195, 195);
  border-radius: 0 0 25px 25px;
}
.title img {
  width: 50px;
  height: 50px;
  margin: 10px 0 0 20px;
}

.title-text {
  font-family: KOTRA_BOLD-Bold !important;
  color: white;
  position: absolute;
  top: 30px;
  left: 50px;
}

</style>