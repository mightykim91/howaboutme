<template>
    <div class="container-btns">
        <div class="wrapper-btn wrapper-left">
            <button class="btn btn-education btn-left" @click="selectOption" value="고등학교 졸업">고등학교 졸업</button>
        </div>
        <div class="wrapper-btn">
            <button class="btn btn-education" @click="selectOption" value="대학교 졸업">대학교 졸업</button>
        </div>
        <div class="wrapper-btn wrapper-right">
            <button class="btn btn-education btn-right" @click="selectOption" value="대학원 이상">대학원 이상</button>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
    name: "Education",
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
            setEducation: "control/setEducation",
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
            this.setEducation(this.selected)
            if(this.selected === "상관 없음") {
                this.selected = []
            }
        }
    },
    mounted() {
      var educations = this.controlInfo.education
      var btns = document.querySelectorAll(".btn-education");
      for (var education of educations) {
        for (var btn of btns) {
          if (education === btn["value"]) {
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
      padding: 5px 13px !important;
    }
</style>