<template>
  <div class="heart-animation hide">
    <div class="heart-l"></div>
    <div class="heart-r"></div>
  </div>
</template>

<script>
export default {

}
</script>

<style>
.hide {
  display: none;
}
.heart-animation {
  z-index: 100;
  background-color: #EF5350;
  height: 70px;
  width: 70px;
  position: fixed;
  top: 43%;
  left: 45%;
  transform: rotate(45deg);
  animation: beat 2s;
}
@keyframes beat {
  50% {
    transform: rotate(45deg) scale(1.8);
  }
  from {
    opacity: 1;

  }
  to {
    opacity: 0;
  }
}
.heart-l {
  background-color: #EF5350;
  height: 40px;
  width: 70px;
  position: relative;
  border-radius: 70px 70px 0 0;
  bottom: 38px;
}
.heart-r {
  background-color: #EF5350;
  height: 40px;
  width: 70px;
  position: relative;
  border-radius: 70px 70px 0 0;
  bottom: 25px;
  right: 52px;
  transform: rotate(-90deg);
} 
</style>