<template>
  <v-container> </v-container>
</template>

<script>
export default {
  mounted() {
    console.log(this.$token);
    this.$http.get("/groups");
  },
};
</script>

<style scoped></style>
