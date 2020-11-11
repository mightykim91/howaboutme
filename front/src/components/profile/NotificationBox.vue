<template>
  <div class="container-notificationBox">
      <Notification />
      <Notification />
      <Notification />
      <Notification />
      <Notification />
      <Notification />
      <Notification />
  </div>
</template>

<script>
import Notification from "./Notification"

export default {
    name: "NotificationBox",
    components: {
        Notification,
    },
    data() {
        return {

        }
    },
    methods: {

    },
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/profile/notification.scss"
</style>