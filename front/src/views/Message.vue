<template>
  <div>
    <Title :title="title" />
    <div class="message-body">
      <MessageEach />
      <MessageEach />
      <MessageEach />
      <MessageEach />
      <MessageEach />
      <MessageEach />
      <MessageEach />
      <MessageEach />
      <MessageEach />
      <MessageEach />
    </div>
  </div>
</template>

<script>
import MessageEach from '../components/message/MessageEach.vue'
import Title from '../components/common/Title'

export default {
  data() {
    return {
      title: 'Message',
    }
  },
  components: {
    MessageEach,
    Title
  },
  methods: {
    test() {
      console.log('check')
    }
  },
  mounted() {
    this.test()
  }

}
</script>

<style>
.message-body {
  height: 78vh;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
}
</style>