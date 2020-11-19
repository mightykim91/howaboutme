<template>
  <div class="progress-circular text-center">
    <v-progress-circular
      :size="40"
      :width="3"
      color="rgb(240, 108, 108)"
      indeterminate
    ></v-progress-circular>
  </div>
</template>

<script>
export default {
    name: "Loading",
}
</script>

<style scoped>
.v-progress-circular {
  margin: 1rem;
}

.hide {
    display: none;
}
</style>