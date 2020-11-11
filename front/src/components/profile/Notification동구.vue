<template>
  <div class='notification-each'>
    <div class='notification-profile-img'>
      <v-avatar style='background-color: white;' class='mx-auto' size='50'>
        <v-img
            src="https://www.popularitas.com/wp-content/uploads/2018/04/user-hero-blue.png"></v-img>
      </v-avatar>
      <v-btn
            class="mx-2 like-icon"
            fab
            dark
            small
            color="pink"
            @click="likeBtn"
        >
            <v-icon v-if="like" color="yellow">
            mdi-heart
            </v-icon>
            <v-icon v-else>
            mdi-heart
            </v-icon>
        </v-btn>
    </div>
    <div class='notification-content'>
      <div class='notification-content-username'>
        {{ partner }}
      </div>
      <div class='notification-content-body'>
        안녕 나는 김나연이야 서울 싸피에서 자율 프로젝트를 하고있지 우후훗
      </div>
    </div>
    <div class="notification-new">
      <div class="notification-new-time">
        2020-11-03
      </div>
      <div class="notification-new-number">
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

<style lang="scss" scoped>
.notification-each {
  height: 12vh;
  display: flex;
  border: white solid 1px;
  cursor: pointer;
  border-bottom: gray 0.2px solid;
}
.notification-profile-img {
  width: 25%;
  display: flex;
  align-items: center;
}
.notification-content {
  width: 50%;
}
.notification-content-username {
  height: 40%;
  display: flex;
  align-items: flex-end;
  font-size: 0.7rem;
  padding-left: 3px;
}
.notification-content-body {
  height: 60%;
  text-align: start;
  font-size: 0.65rem;
}
.notification-new {
  width: 25%;
}
.notification-new-time {
  height: 40%;
  color: gray;
  font-size: 0.7rem;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}
.notification-new-number {
  height: 60%;
  padding: 5px 20px 0 0;
  display: flex;
  justify-content: flex-end;
  font-size: 0.5rem;
  color: white;
}
</style>