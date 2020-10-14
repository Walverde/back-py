<template>


  <nav>
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
                <v-list-item v-for="link in links" :key="link.text" router :to="link.router" active-class="border">
                    <v-list-item-action>
                        <v-icon>{{link.icon}}</v-icon>
                    </v-list-item-action>

                    <v-list-item-content>
                        <v-list-item-title>{{link.text}}</v-list-item-title> 
                    </v-list-item-content>
                </v-list-item>
            </v-list>

      <!-- Carrossel tava aqui -->

      </v-navigation-drawer>

  </nav>
</template>




<script>
export default {
    data: () => ({
        drawer: false,
        links:[
            {icon: 'home', text: 'Inicio', route: '/'},
            {icon: 'show_chart', text: 'Monitorar', route: '/'},
            {icon: 'save_alt', text: 'Exportar', route: '/'},
            {icon: 'headset_mic', text: 'Suporte', route: '/'},
        ],
        slides: [
            'Online check and payment of official debts',
            'Online check and payment of official debts',
            'Online check and payment of official debts',
            'Online check and payment of official debts',
            ]
    
    })
}
</script>


<style scoped>
.border{
    border-left: 4px solid #2c3e50;
};

</style>