<template>
  <v-app>

     <v-app-bar app="" color="black" dark>
        <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Enertrack</v-toolbar-title>
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" dark="" app temporary="" >
                <v-layout column align-center>
                    <v-flex class="mt-10 mb-8">
                        <v-avatar>
                            <v-icon large>show_chart</v-icon>
                        </v-avatar>
                    </v-flex>
                </v-layout>

        <v-divider></v-divider>

                <v-list>
                    <v-list-item v-for="link in links" :key="link.text" router :to="link.route" active-class="border">

                        <v-list-item-action>
                            <v-icon class="white-text">{{link.icon}}</v-icon>
                        </v-list-item-action>

                        <v-list-item-content>
                            <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title> 
                        </v-list-item-content> 
                    </v-list-item>


                      <v-divider></v-divider>


                    <v-list-item  v-for="link in links2" :key="link.text" router=false :to="link.route" active-class="border">
                        <v-list-item-action>
                            <v-icon class="white-text">{{link.icon}}</v-icon>
                        </v-list-item-action>

                        <v-list-item-content>
                            <v-list-item-title class="white--text">{{ link.text }}</v-list-item-title> 
                        </v-list-item-content>
                    </v-list-item>


                     <v-divider></v-divider>  



                  </v-list>
                
          <!-- Carrossel tava aqui -->

    </v-navigation-drawer>



    <!-- Sizes your content based upon application components -->
    <v-main>


      <!-- Provides the application the proper gutter -->
      <v-container fluid>

        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
          
  </v-app>
</template>





<script>



export default {
  
  name: 'App',

  components: {

  },
  

  data: () => ({
    drawer: false,
    links:[
            {icon: 'home', text: 'Inicio', route: '/'},
            {icon: 'show_chart', text: 'Monitorar', route: '../monitorar'},
            {icon: 'save_alt', text: 'Exportar', route: '/exportar'},
            {icon: 'supervisor_account', text: 'Cadastrar', route: '/cadastrar'},
        ],
    links2:[
            {icon: 'headset_mic', text: 'Suporte', route: '/contate'},
            {icon: 'power_settings_new', text: 'Sair'},
        ],   
        slides: [
            'Online check and payment of official debts',
            'Online check and payment of official debts',
            'Online check and payment of official debts',
            'Online check and payment of official debts',
            ],
    //
  }),
};
</script>

<style scoped>
.border{
    border-left: 4px solid #008000 ;
};

</style>
