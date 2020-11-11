<template>
  <v-card>
    <v-card-title class="headline"> 당신의 생일은? </v-card-title>
    <v-card-actions class="d-block">
      <div>
        <v-menu
          ref="menu"
          v-model="menu"
          :close-on-content-click="false"
          transition="scale-transition"
          offset-y
          min-width="275px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-model="date"
              label="Birthday date"
              prepend-icon="mdi-calendar"
              readonly
              v-bind="attrs"
              v-on="on"
            ></v-text-field>
          </template>
          <v-date-picker
            ref="picker"
            v-model="date"
            :max="new Date().toISOString().substr(0, 10)"
            min="1950-01-01"
            @change="save"
          ></v-date-picker>
        </v-menu>
        <v-btn
          class="info-btn mx-auto my-3"
          color="red lighten-3"
          dark
          @click="emitBirth"
        >
          입력완료
        </v-btn>
      </div>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "Birth",
  data() {
    return {
      dialog_birth: true,
      date: null,
      menu: false,
    };
  },
  watch: {
    menu(val) {
      val && setTimeout(() => (this.$refs.picker.activePicker = "YEAR"));
    },
  },
  methods: {
    save(date) {
      this.$refs.menu.save(date);
    },
    emitBirth() {
      // this.dialog_birth = true;
      this.$emit("getBirth", this.date);
      this.$emit("closeBirth", this.dialog_birth);
    },
  },
};
</script>

<style scoped src="../../assets/scss/userinfo.scss" lang="scss">
