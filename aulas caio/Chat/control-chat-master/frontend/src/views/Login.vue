<template>
  <v-container>
    <v-layout justify-center>
      <v-card class="col-5">
        <v-card-title>Login</v-card-title>
        <v-text-field v-model="form.email" label="Email" />
        <v-text-field
          v-model="form.password"
          label="Password"
          type="password"
        />
        <v-card-actions>
          <v-btn @click="send">Logar</v-btn>
        </v-card-actions>
      </v-card>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data() {
    return {
      form: {},
    };
  },
  methods: {
    send() {
      this.$http
        .post("/login", this.form)
        .then((result) => {
          console.log(result);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped></style>
