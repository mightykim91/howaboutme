<template>
  <div class="container-controls hide">
      <div class="background-controls" @click="closeControls"></div>
      <div class="modal-controls">
        <!-- <div class="modal-deco-top"></div> -->
        <div class="modal-header">
            <h2 class="header-title">나의 이상형 찾기</h2>
            <button class="btn-confirm" @click="confirmChanges">
                <img src="@/assets/images/icon/check-mark.png">
            </button>
        </div>
        <div class="modal-body">
            <div class="control-item">
                <p class="control-title">지역</p>
                <div class="items-padding">
                    <Region />
                </div>
            </div>
            <div class="control-item">
                <p class="control-title">나이</p>
                <div class="items-padding">
                    <Age />
                </div>
            </div>
            <div class="control-item">
                <p class="control-title">키</p>
                <div class="items-padding">
                    <Height />
                </div>
            </div>
            <div class="control-item">
                <p class="control-title">체형</p>
                <BodyType />
            </div>
            <ControlDetails v-if="showDetails"/>
        </div>
        <div class="modal-footer">
            <div class="container-btns">
                <button class="btn-detail" v-if="!showDetails" @click="openDetails">세부 설정</button>
                <button class="btn-detail" v-if="showDetails" @click="closeDetails">접기</button>
            </div>
            <!-- <button class="btn-toTop" @click="toTop">⬆</button> -->
            <button class="btn-close" @click="closeControls">닫기</button>
        </div>
      </div>
  </div>
</template>

<script>
import Region from "@/components/controls/Region.vue"
import Age from "@/components/controls/Age.vue"
import Height from "@/components/controls/Height.vue"
import BodyType from "@/components/controls/BodyType.vue"
import ControlDetails from "@/components/controls/ControlDetails.vue"

import { mapActions } from "vuex";

export default {
    components: {
        Region,
        Age,
        Height,
        BodyType,
        ControlDetails,
    },
    data() {
        return {
            sliderBottom: 20, 
            sliderTop: 50,
            showDetails: false
        }
    },
    methods: {
        ...mapActions({
            updateControls: "control/updateControls",
        }),
        closeControls() {
            document.querySelector(".container-controls").classList.add("hide");
            this.closeDetails();
        },
        confirmChanges() {
            let result = this.updateControls()
            if (result) {
                this.$router.go();
            }
            else {
                alert("모든 조건을 설정해주세요.")
            }
            
        },
        openDetails() {
            this.showDetails = true;
            // var modal = document.querySelector(".modal-controls");
            var background = document.querySelector(".background-controls");
            // modal.style.height = "auto";
            background.style.height = "140vh";
        },
        closeDetails() {
            this.showDetails = false;
            // var modal = document.querySelector(".modal-controls");
            var background = document.querySelector(".background-controls");
            // modal.style.height = "80%";
            background.style.height = "100vh";
        },
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/controls/controlModal.scss", "@/assets/scss/controls/selectBox.scss"
</style>