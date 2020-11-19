<template>
  <div class='alreadylike'>
    <img class="like-modal-sorry" src="../../assets/images/icon/sorry.png" alt="">
    <div>이미 하트를 보낸 상대입니다</div> 
    <i @click="exitBtn" class="far fa-times-circle modal-close"></i>
  </div>
</template>

<script>
export default {
  methods: {
    exitBtn() {
      this.$emit('closeModal')
    }
  }
}
</script>

<style>
.alreadylike {
  position: relative;
  background-color: white;
  height: 20vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: gray;
  font-size: 0.8rem;
}
.alreadylike .modal-close {
  color: gray !important;
  background: white;
  font-size: 1.5rem;
  border-radius: 0.7rem 0.7rem;
  position: absolute;
  top: 1.5vh;
  right: 3vw;
  z-index: 10;
}
</style>