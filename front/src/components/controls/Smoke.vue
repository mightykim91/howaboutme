<template>
<div class="smoke">
    <select class="select" v-model="selected">
        <option selected>상관 없음</option>
        <option>비흡연</option>
        <option>술 마실 때만</option>
        <option>가끔</option>
        <option>자주</option>
        <option>매일</option>
        <option>전자담배</option>
    </select>
</div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
    name: "Smoke",
    data() {
        return {
            selected: "상관 없음",
        }
    },
    computed: {
        ...mapGetters({
            controlInfo: "control/getControlInfo",
        })
    },
    methods: {
        ...mapMutations({
            setSmoke: "control/setSmoke",
        })
    },
    mounted() {
        this.selected = this.controlInfo.smoke;
    },
    watch: {
        selected() {
            this.setSmoke(this.selected);
        } 
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/controls/selectBox.scss";
    .select {
        background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnIHRyYW5zZm9ybT0ibWF0cml4KDEsLTIuNDQ5MjkzNTk4Mjk0NzA2NGUtMTYsMi40NDkyOTM1OTgyOTQ3MDY0ZS0xNiwxLC0xLjQyMTA4NTQ3MTUyMDIwMDRlLTEzLDIuODQyMTcwOTQzMDQwNDAxZS0xNCkiPjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0ibTQyMiAyODZjMCA4LjI4NCA2LjcxNiAxNSAxNSAxNXMxNS02LjcxNiAxNS0xNWMwLTY3LjUtMzUuMDY0LTkzLjc5OC02Ni0xMTctMjguOTc2LTIxLjczMi01NC00MC41LTU0LTkzIDAtOC4yODQtNi43MTYtMTUtMTUtMTVzLTE1IDYuNzE2LTE1IDE1YzAgNjcuNSAzNS4wNjQgOTMuNzk4IDY2IDExNyAyOC45NzYgMjEuNzMyIDU0IDQwLjUgNTQgOTN6IiBmaWxsPSIjOTk5OTk5IiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+PHBhdGggZD0ibTQ1MiA3NmMwLTguMjg0LTYuNzE2LTE1LTE1LTE1cy0xNSA2LjcxNi0xNSAxNWMwIDY0LjU0MiAxNy4yNzYgOTAuNDU3IDMyLjUxOSAxMTMuMzIgMTQuMTMyIDIxLjE5OSAyNy40ODEgNDEuMjIyIDI3LjQ4MSA5Ni42OCAwIDguMjg0IDYuNzE2IDE1IDE1IDE1czE1LTYuNzE2IDE1LTE1YzAtNjQuNTQyLTE3LjI3Ni05MC40NTctMzIuNTE5LTExMy4zMi0xNC4xMzItMjEuMTk5LTI3LjQ4MS00MS4yMjItMjcuNDgxLTk2LjY4eiIgZmlsbD0iIzk5OTk5OSIgZGF0YS1vcmlnaW5hbD0iIzAwMDAwMCIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPjxwYXRoIGQ9Im00OTcgMzMxaC00ODJjLTguMjg0IDAtMTUgNi43MTYtMTUgMTV2OTBjMCA4LjI4NCA2LjcxNiAxNSAxNSAxNWg0ODJjOC4yODQgMCAxNS02LjcxNiAxNS0xNXYtOTBjMC04LjI4NC02LjcxNi0xNS0xNS0xNXptLTc1IDMwdjYwaC0yMTF2LTYwem0tMzkyIDBoMTUxdjYwaC0xNTF6bTQ1MiA2MGgtMzB2LTYwaDMweiIgZmlsbD0iIzk5OTk5OSIgZGF0YS1vcmlnaW5hbD0iIzAwMDAwMCIgc3R5bGU9IiIgY2xhc3M9IiI+PC9wYXRoPjwvZz48L2c+PC9zdmc+")
            no-repeat 5% 0%;
        background-size: 22px;
    }
</style>