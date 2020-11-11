<template>
<div>
    <select class="select" v-model="selected">
        <option selected>모든 지역</option>
        <option>서울</option>
        <option>경기도</option>
        <option>부산</option>
        <option>인천</option>
        <option>대구</option>
        <option>대전</option>
        <option>광주</option>
        <option>울산</option>
        <option>세종시</option>
        <option>충청남도</option>
        <option>충청북도</option>
        <option>경상남도</option>
        <option>경상북도</option>
        <option>전라남도</option>
        <option>전라북도</option>
        <option>강원도</option>
        <option>제주도</option>
    </select>
</div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";

export default {
    name: "Region",
    data() {
        return {
            selected: "모든 지역",
        }
    },
    computed: {
        ...mapGetters({
            controlInfo: "control/getControlInfo",
        })
    },
    methods: {
        ...mapMutations({
            setRegion: "control/setRegion",
        })
    },
    mounted() {
        this.selected = this.controlInfo.region;
    },
    watch: {
        selected() {
            this.setRegion(this.selected);
        } 
    }
}
</script>

<style lang="scss" scoped>
    @import "@/assets/scss/controls/selectBox.scss";
    .select {
        background: url("data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHhtbG5zOnN2Z2pzPSJodHRwOi8vc3ZnanMuY29tL3N2Z2pzIiB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiIgeD0iMCIgeT0iMCIgdmlld0JveD0iMCAwIDUxMiA1MTIiIHN0eWxlPSJlbmFibGUtYmFja2dyb3VuZDpuZXcgMCAwIDUxMiA1MTIiIHhtbDpzcGFjZT0icHJlc2VydmUiIGNsYXNzPSIiPjxnIHRyYW5zZm9ybT0ibWF0cml4KDAuNzk5OTk5OTk5OTk5OTk5OSwwLDAsMC43OTk5OTk5OTk5OTk5OTk5LDUxLjE5OTk5NDY1OTQyMzkzNiw1MS4yMDAwMDAwMDAwMDAwMikiPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgoJPGc+CgkJPHBhdGggZD0iTTQyNS45NTEsODkuMDIxQzM4Ni44NjQsMzIuNDUxLDMyNC45MTcsMCwyNTYuMDA2LDBTMTI1LjE0OCwzMi40NTEsODYuMDYxLDg5LjAyMSAgICBjLTM4Ljg5NSw1Ni4yODQtNDcuODc2LDEyNy41NDEtMjQuMDcyLDE5MC40OTZjNi4zNjcsMTcuMTkyLDE2LjQ4OCwzMy44OTUsMzAuMDEsNDkuNTQ3bDE1MC4zNzgsMTc2LjYzNCAgICBjMy40MDEsMy45OTgsOC4zODQsNi4zMDIsMTMuNjI5LDYuMzAyYzUuMjQ1LDAsMTAuMjI4LTIuMzAzLDEzLjYyOS02LjMwMmwxNTAuMzM2LTE3Ni41ODYgICAgYzEzLjU4Mi0xNS43NDIsMjMuNjktMzIuNDI3LDMwLjAwNC00OS40ODFDNDczLjgyNywyMTYuNTYyLDQ2NC44NDYsMTQ1LjMwNSw0MjUuOTUxLDg5LjAyMXogTTQxNi40NTEsMjY3LjA5MyAgICBjLTQuODY5LDEzLjE1OC0xMi44MTgsMjYuMTY3LTIzLjYxMywzOC42OGMtMC4wMywwLjAzLTAuMDYsMC4wNi0wLjA4NCwwLjA5NkwyNTYuMDA2LDQ2Ni40ODdMMTE5LjE3NCwzMDUuNzY4ICAgIGMtMTAuNzg5LTEyLjUwMi0xOC43MzgtMjUuNTEtMjMuNjU1LTM4Ljc5NGMtMTkuNjg2LTUyLjA2NS0xMi4yMTUtMTEwLjk4MSwxOS45OTEtMTU3LjU5MiAgICBjMzIuMzA3LTQ2Ljc2LDgzLjUxOS03My41NzgsMTQwLjQ5Ni03My41NzhjNTYuOTc2LDAsMTA4LjE4MiwyNi44MTcsMTQwLjQ5LDczLjU3OCAgICBDNDI4LjcwOCwxNTUuOTkzLDQzNi4xODUsMjE0LjkwOSw0MTYuNDUxLDI2Ny4wOTN6IiBmaWxsPSIjOTk5OTk5IiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+Cgk8L2c+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnPgoJCTxwYXRoIGQ9Ik0yNTYuMDA2LDEwNi4yMTljLTU1LjI3NiwwLTEwMC4yNTIsNDQuOTctMTAwLjI1MiwxMDAuMjUyczQ0Ljk3LDEwMC4yNTIsMTAwLjI1MiwxMDAuMjUyczEwMC4yNTItNDQuOTcsMTAwLjI1Mi0xMDAuMjUyICAgIEMzNTYuMjU4LDE1MS4xOTUsMzExLjI4MiwxMDYuMjE5LDI1Ni4wMDYsMTA2LjIxOXogTTI1Ni4wMDYsMjcwLjkxOGMtMzUuNTM2LDAtNjQuNDQ4LTI4LjkxMi02NC40NDgtNjQuNDQ4ICAgIGMwLTM1LjUzNiwyOC45MTItNjQuNDQ4LDY0LjQ0OC02NC40NDhjMzUuNTM2LDAsNjQuNDQ4LDI4LjkxMiw2NC40NDgsNjQuNDQ4UzI5MS41NDIsMjcwLjkxOCwyNTYuMDA2LDI3MC45MTh6IiBmaWxsPSIjOTk5OTk5IiBkYXRhLW9yaWdpbmFsPSIjMDAwMDAwIiBzdHlsZT0iIiBjbGFzcz0iIj48L3BhdGg+Cgk8L2c+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPGcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPC9nPgo8ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8L2c+CjxnIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjwvZz4KPC9nPjwvc3ZnPg==")
            no-repeat 5% 50%; /* 위치 아이콘 추가 */
        background-size: 22px;
    }
</style>