<template>
  <div class="file hide">
    <div class='file-background'>
      <v-file-input
          prepend-icon="mdi-camera"
          v-model='imgData'
          @change='onChangeImages'
          ></v-file-input>
    </div>
    <div class='file-background'>
      <v-img :src="imgUrl" alt=""></v-img>
    </div>
    <i class="fas fa-times file-exit" @click="exitFile"></i>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        imgData: null,
        imgUrl: null,
      }
    },
    props: {
    },
    methods: {
      test() {

      },
      exitFile() {
        document.querySelector('.file').classList.add('hide')
      },
      addFile(file) {
        this.$emit('addFile', file)
      },
      onChangeImages() {
          const file = this.imgData; // Get first index in files
          this.imgUrl = URL.createObjectURL(file); // Create File URL
          console.log(this.imgUrl)
      },
    },
    mounted() {
      var input = document.querySelector(".chat-input")
      var inputY = input.getBoundingClientRect().top
      var file = document.querySelector('.file')
      file.style.top = `${inputY-130}px`
    }
  }
</script>

<style>
.file {
  position: fixed;
  top: 0px;
  width: 100%;
  height: 130px;
  padding: 10px;
  background-color: rgba( 180, 180, 180, 0.8 );
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.file-background {
  width: 45%;
  height: 95%;
  background-color: white;
}
.file-exit {
  display: flex;
}
.hide {
  display: none;
}
</style>