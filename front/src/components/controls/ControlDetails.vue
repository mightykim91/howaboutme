<template>
  <div class="container-controldetails">
    <div class="control-item">
        <p class="control-title">학력</p>
        <Education />
    </div>
    <div class="control-item">
        <p class="control-title">직업</p>
        <Job />
    </div>
    <div class="control-item">
        <p class="control-title">종교</p>
        <Religion />
    </div>
    <div class="drink-smoke">
      <div class="control-item item-drink">
          <p class="control-title">음주 여부</p>
          <Drink />
      </div>
      <div class="control-item item-smoke">
          <p class="control-title">흡연 여부</p>
          <Smoke />
      </div>
    </div>
  </div>
</template>

<script>
import Education from "@/components/controls/Education.vue"
import Job from "@/components/controls/Job.vue"
import Religion from "@/components/controls/Religion.vue"
import Drink from "@/components/controls/Drink.vue"
import Smoke from "@/components/controls/Smoke.vue"

export default {
    name: "ControlDetail",
    components: {
      Education,
      Job,
      Religion,
      Drink,
      Smoke,
    },
    data() {
        return {

        }
    },
    methods: {

    }
}
</script>

<style lang="scss" scoped>
  @import "@/assets/scss/controls/controlDetails.scss", "@/assets/scss/controls/controlModal.scss";
</style>