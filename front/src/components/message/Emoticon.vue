<template>
  <div class="emoticon hide">
    <div class='emotion-background'></div>
    <div>
      <i class='emoticon-i' v-for="emoticon in emoticonLists" :key="emoticon" :class=emoticon @click="addEmoticon(emoticon)"></i>
    </div>
    <i class="fas fa-times emoticon-exit" @click="exitEmoticon"></i>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        emoticonLists: [
          "far fa-laugh-beam",
          "far fa-laugh",
          "far fa-surprise",
          "far fa-smile-wink",
          "far fa-sad-tear",
          "far fa-sad-cry",
          "far fa-meh-rolling-eyes",
          "far fa-meh-blank",
          "far fa-grin-wink",
          "far fa-grin-stars",
          "far fa-grin-squint",
          "far fa-grin-hearts",
          "far fa-grin-beam",
          "far fa-grin",
          "far fa-smile",
          "far fa-laugh-wink",
          "far fa-laugh-squint",
          "far fa-kiss-wink-heart",
          
        ],
      }
    },
    props: {
    },
    methods: {
      exitEmoticon() {
        document.querySelector('.emoticon').classList.add('hide')
      },
      addEmoticon(emoticon) {
        this.$emit('addEmoticon', "!emoticon " + emoticon)
        this.exitEmoticon()
      }
    },
    mounted() {
      var input = document.querySelector(".chat-input")
      var inputY = input.getBoundingClientRect().top
      var emoticon = document.querySelector('.emoticon')
      emoticon.style.top = `${inputY-130}px`
    }
  }
</script>

<style>
.emoticon {
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
.emoticon-i {
  font-size: 1.6rem;
  width: 16%;
  padding: 5px;
}
.emoticon-exit {
  display: flex;
}
.hide {
  display: none;
}
</style>