<template>
    <div class="container-btns">
        <div class="wrapper-btn wrapper-left">
            <button class="btn btn-religion btn-left" @click="selectOption" value="기독교">기독교</button>
        </div>
        <div class="wrapper-btn">
            <button class="btn btn-religion" @click="selectOption" value="천주교">천주교</button>
        </div>
        <div class="wrapper-btn">
            <button class="btn btn-religion" @click="selectOption" value="불교">불교</button>
        </div>
        <!-- <div class="wrapper-btn">
            <button class="btn btn-religion" @click="selectOption" value="기타">기타</button>
        </div> -->
        <div class="wrapper-btn">
            <button class="btn btn-religion" @click="selectOption" value="무교">무교</button>
        </div>
        <div class="wrapper-btn wrapper-right">
            <button class="btn btn-religion btn-right" @click="selectOption" value="상관 없음">상관 없음</button>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
    name: "Religion",
    data() {
        return {
            selected: []
        }
    },
    computed: {
        ...mapGetters({
            controlInfo: "control/getControlInfo"
        })
    },
    methods: {
        ...mapMutations({
            setReligion: "control/setReligion",
        }),
        selectOption(event) {
            if (this.selected.includes(event.target.value)) {
                var index = this.selected.indexOf(event.target.value)
                this.selected.splice(index, 1)
                event.target.style.background = "white"
                event.target.style.borderTop = "1px solid rgb(211, 211, 211)"
                event.target.style.borderBottom = "1px solid rgb(211, 211, 211)"
                event.target.style.borderRight = "1px solid rgb(211, 211, 211)"
                event.target.style.color = "#2c3e50"


            }
            else {
                this.selected.push(event.target.value)
                event.target.style.background = "rgb(252, 166, 157)"
                event.target.style.borderTop = "1px solid rgb(252, 166, 157)"
                event.target.style.borderBottom = "1px solid rgb(252, 166, 157)"
                event.target.style.borderRight = "1px solid rgb(252, 166, 157)"
                event.target.style.color = "white"
            }
            this.setReligion(this.selected)
        }
    },
    mounted() {
      var religions = this.controlInfo.religion
      var btns = document.querySelectorAll(".btn-religion");
      for (var religion of religions) {
        for (var btn of btns) {
          if (religion === btn["value"]) {
            btn.click();
          }
        }
      }
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/controls/optionButtons.scss";
    .btn {
      padding: 5px 11px !important;
    }
</style>