<template>
  <div class="header">
    <div class="container-header">
    <div class="header-item">
    </div>
    <div class="header-item">
        <h2 class="header-logo-name">나는 어때?</h2>
    </div>
    <div class="header-item">
        <button class="header-btn" @click="openControlModal">
            <img class="header-btn-img" src="@/assets/images/header/typing.png" alt="">
        </button>
    </div>
    </div>
    <div class="modal-component">
        <ControlModal />
    </div>
  </div>
</template>

<script>
import ControlModal from "@/components/controls/ControlModal.vue"

export default {
    name: "Header",
    components: {
        ControlModal,
    },
    methods: {
        openControlModal() {
            document.querySelector(".container-controls").classList.remove("hide");
        }
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/main/header.scss";

</style>