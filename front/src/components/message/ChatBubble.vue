<template>
  <div>
    <div v-if="chatlog.sender === 'Kim'" class='chat-bubble-partner'>
      <div class='chat-bubble-left chat-bubble--left'>
        {{ chatlog.text }}
      </div>
    </div>

    <!-- 날릴 부분 -->
    <!-- <div v-if="user === 'emoticon'" class='chat-bubble-partner'>
      <div class='chat-bubble-left chat-bubble--left'>
        <i class="far fa-laugh-beam" style="font-size: 40px;"></i>
      </div>
    </div> -->
    <!--  -->
    <div v-else class='chat-bubble-user'>
      <div class='chat-bubble-right chat-bubble--right'>
        {{ chatlog.text }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: String,
    chatlog: Object,
  },
}
</script>

<style>
.chat-bubble-user {
  display: flex;
  justify-content: flex-end;
}
.chat-bubble-partner {
  display: flex;
  justify-content: flex-start;
}
.chat-bubble-left {
  padding: 10px 14px;
  background-color: #eee;
  margin: 10px 30px;
  border-radius: 9px;
  position: relative;
  /* animation: 1s ease-in; */
}
.chat-bubble-left::after {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  top: 50%;
  border-bottom: 0;
  margin-top: -10px;
}
.chat-bubble-right {
  padding: 10px 14px;
  background-color: rgb(241, 195, 195);
  margin: 10px 30px;
  border-radius: 9px;
  position: relative;
  /* animation: 1s ease-in; */
}
.chat-bubble-right::after {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  border: 20px solid transparent;
  top: 50%;
  border-bottom: 0;
  margin-top: -10px;
}
.chat-bubble--left::after{
  left: 0;
  border-right-color: #eee;
  border-left: 0;
  margin-left: -15px;
}
.chat-bubble--right::after {
  right: 0;
  border-left-color: rgb(241, 195, 195);
  border-right: 0;
  margin-right: -15px;
}

</style>