<template>
    <div class="container-btns">
        <div class="wrapper-btn" style="marginBottom:6px;">
            <button class="btn btn-job" @click="selectOption" value="학생">학생</button>
            <button class="btn btn-job" @click="selectOption" value="전문직">전문직</button>
            <button class="btn btn-job" @click="selectOption" value="교육직">교육직</button>
            <button class="btn btn-job" @click="selectOption" value="공무원">공무원</button>
            <button class="btn btn-job" @click="selectOption" value="사업가">사업가</button>
        </div>
        <div class="wrapper-btn">
            <button class="btn btn-job" @click="selectOption" value="연구,기술직">연구,기술직</button>
            <button class="btn btn-job" @click="selectOption" value="군인">군인</button>
            <button class="btn btn-job" @click="selectOption" value="무직">무직</button>
            <button class="btn btn-job" @click="selectOption" value="기타">기타</button>
        </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
    name: "Job",
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
            setJob: "control/setJob",
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
            this.setJob(this.selected)
            if(this.selected === "상관 없음") {
                this.selected = []
            }
        }
    },
    mounted() {
      var jobs = this.controlInfo.job
      var btns = document.querySelectorAll(".btn-job");
      for (var job of jobs) {
        for (var btn of btns) {
          if (job === btn["value"]) {
            btn.click();
          }
        }
      }
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/controls/pillButtons.scss";
</style>