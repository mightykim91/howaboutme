<template>
  <div class='message-each' @click="$router.push('/chat/'+partner)">
    <div class='message-profile-img'>
      <v-avatar style='background-color: white;' class='mx-auto' size='50'>
        <v-img
            src="https://www.popularitas.com/wp-content/uploads/2018/04/user-hero-blue.png"></v-img>
      </v-avatar>
    </div>
    <div class='message-content'>
      <div class='message-content-username'>
        {{ partner }}
      </div>
      <div class='message-content-body'>
        안녕 나는 김나연이야 서울 싸피에서 자율 프로젝트를 하고있지 우후훗
      </div>
    </div>
    <div class="message-new">
      <div class="message-new-time">
        2020-11-03
      </div>
      <div class="message-new-number">
        <v-avatar color="#fca69d" size="20">
          1
        </v-avatar>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      partner: "kimnayu",
    }
  },

}
</script>

<style>
.message-each {
  height: 12vh;
  display: flex;
  border: white solid 1px;
  cursor: pointer;
  border-bottom: gray 0.2px solid;
}
.message-profile-img {
  width: 25%;
  display: flex;
  align-items: center;
}
.message-content {
  width: 50%;
}
.message-content-username {
  height: 40%;
  display: flex;
  align-items: flex-end;
  font-size: 0.7rem;
  padding-left: 3px;
}
.message-content-body {
  height: 60%;
  text-align: start;
  font-size: 0.65rem;
}
.message-new {
  width: 25%;
}
.message-new-time {
  height: 40%;
  color: gray;
  font-size: 0.7rem;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}
.message-new-number {
  height: 60%;
  padding: 5px 20px 0 0;
  display: flex;
  justify-content: flex-end;
  font-size: 0.5rem;
  color: white;
}
</style>