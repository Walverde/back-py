<template>
  <v-app>


    <v-toolbar app dark="" width="50 px" height="50 px">

        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title color="white" >Enertrack</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon>
          <v-icon >add_shopping_cart</v-icon>
        </v-btn>


    </v-toolbar>

    <v-navigation-drawer app v-model="drawer" temporary="" dark>
      
      <v-list class="pa-1">
        <v-list-tile avatar>
            
          <v-list-tile-avatar>
            <img src="https://media-exp1.licdn.com/dms/image/C4D0BAQF3gFk8COpiGg/company-logo_200_200/0?e=2159024400&v=beta&t=k6bmHym8a3ctnr1MmkvdPbucEvXjKd1hFCyJzVI_PTA">
          </v-list-tile-avatar>

          <v-list-tile-content>
            <v-list-tile-title>Control Engenharia</v-list-tile-title>
          </v-list-tile-content>

        </v-list-tile>
      </v-list>

   
     <v-spacer></v-spacer>

      <v-app-bar @click="$router.push({ name: 'Home' })">
        Home
      </v-app-bar>

      <v-app-bar @click="$router.push({ name: 'monitorar' })">
        Monitorar
      </v-app-bar>

      <v-app-bar @click="$router.push({ name: 'exportar' })">
        Exportar
      </v-app-bar>

      <v-app-bar @click="$router.push({ name: 'smenu' })">
        Contate-nos
      </v-app-bar>

  

    </v-navigation-drawer>

    <v-card>
        <div id="app">
          <div id="nav">
            <v-container  >
              <img alt="Vue logo" src="../public/control.png" align= "justify" width="70 px">
            </v-container>
          
          </div>
      
          <v-main >
            <router-view />
          </v-main>
          
        </div>
        
    </v-card>

    <v-card align= "justify" > 

        <v-card-title primary-title align= "justify" >
          <div align= "justify">
            <h3 align= "justify" >Enertrack</h3>
            <div align= "justify" >By Control Egenharia</div>
          </div>
        </v-card-title>


    </v-card>

  </v-app>
</template>





<script>
export default {
  name: "app",
  data(){
    return{
      drawer: true
    };
  }
};
</script>





<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
