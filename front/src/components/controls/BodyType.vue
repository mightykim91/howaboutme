<template>
  <div>
      <div class="container-btns">
          <div class="wrapper-btn wrapper-left">
            <button class="btn btn-body btn-left" @click="selectOption" value="마른">마른</button>
          </div>
          <div class="wrapper-btn">
            <button class="btn btn-body" @click="selectOption" value="슬림 근육">슬림 근육</button>
          </div>
          <div class="wrapper-btn">

            <button class="btn btn-body" @click="selectOption" value="보통">보통</button>
          </div>
          <div class="wrapper-btn">

            <button class="btn btn-body" @click="selectOption" value="근육질">근육질</button>
          </div>
          <div class="wrapper-btn">
            <button class="btn btn-body" @click="selectOption" value="통통">통통</button>
          </div>
          <div class="wrapper-btn wrapper-right">
            <button class="btn btn-body btn-right" @click="selectOption" value="우람">우람</button>
          </div>
      </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
export default {
    name: "BodyType",
    data() {
        return {
            selected: []
        }
    },
    computed: {
      ...mapGetters({
        controlInfo: "control/getControlInfo",
      })
    },
    methods: {
      ...mapMutations({
        setBody: "control/setBody",
      }),
      selectOption(event) {
          if (this.selected.includes(event.target.value)) {
              var index = this.selected.indexOf(event.target.value)
              this.selected.splice(index, 1)
              event.target.style.background = "white"
              event.target.style.color = "rgb(119, 116, 139)"


          }
          else {
              this.selected.push(event.target.value)
              event.target.style.background = "rgb(252, 166, 157)"
              event.target.style.color = "white"
          }
          if(this.selected.length === 0) {
            this.selected = "상관 없음"
          }
          this.setBody(this.selected);
          if(this.selected === "상관 없음") {
            this.selected = []
          }
      }
    },
    mounted() {
      var bodyTypes = this.controlInfo.body;
      var btns = document.querySelectorAll(".btn-body");
      for (var bodyType of bodyTypes) {
        for (var btn of btns) {
          if (bodyType === btn["value"]) {
            btn.click();
          }
        }
      }
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/controls/optionButtons.scss"
</style>