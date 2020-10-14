<template>
  <v-card class="mx-auto overflow-hidden" height="400" >

    <v-app-bar app="" color="black" dark>
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Enertrack</v-toolbar-title>
    </v-app-bar>

  </v-card>
</template>

<script>
  export default {
    data: () => ({
      drawer: false,
      
    }),
  }
</script>