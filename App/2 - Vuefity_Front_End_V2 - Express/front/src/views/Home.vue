<template>


  <v-app :style="{backgound: $vuetify.theme.themes.light.background}">
    <v-container>
      <v-layout row class="ma-4">
        <v-app style="background-color: grey lighten-1;" class="rounded">
          <v-row>
            <v-col cols="12" md="8" class="ligne" > 
            <!-- <v-col cols="12" md="8" class="ligne" >  ORIGINAL COM A BARRA-->
              <v-container>
              <v-row>
                  <v-col cols="12" md="9" offset-md="1">
                   <v-text-field 
                   label="Pesquisar" 
                   prepend-inner-icon="search"
                   ></v-text-field>
                  </v-col>
                  <v-col cols="12" md="2" align="center" justify="center" >
                    <v-badge color="error" overlap class="mt-5">
                            <template slot="badge">2</template>
                            <v-icon color="tertiary">mdi-bell</v-icon>
                    </v-badge>
                  </v-col>
                <v-col cols="12" md="12">
                  <h1 class="headline md-2 grey--text">Tensão</h1>
                  <template>
                    <div id="app">
                      <GChart
                        type="ColumnChart"
                        :data="chartDatat"
                        :options= "chartOptions"
                        /> 
                    </div>
                  </template>
                </v-col>
                <v-col cols="12" md12><h1 class="headline mb-2 grey--text">Corrente</h1></v-col>
                <v-col cols="12" md="8">
                  <v-card>
                    <v-list>

                      <v-list-item>
                        <v-list-item-avatar color="blue">
                          <v-icon dark>fas fa-car</v-icon>
                        </v-list-item-avatar>
                        <v-list-item-content>
                          <v-list-item-title>Auto</v-list-item-title>
                          <v-list-item-subtitle>pewe</v-list-item-subtitle>
                        </v-list-item-content>
                        <v-list-item-content align="right">
                          <v-list-item-title class="indigo--text">500</v-list-item-title>
                          <v-list-item-subtitle>100</v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>

                      <v-divider insert></v-divider>

                      <v-list-item>
                        <v-list-item-avatar color="red">
                          <v-icon dark>fas fa-car</v-icon>
                        </v-list-item-avatar>
                        <v-list-item-content>
                          <v-list-item-title>Auto</v-list-item-title>
                          <v-list-item-subtitle>pewe</v-list-item-subtitle>
                        </v-list-item-content>
                        <v-list-item-content align="right">
                          <v-list-item-title class="indigo--text">500</v-list-item-title>
                          <v-list-item-subtitle>100</v-list-item-subtitle>
                        </v-list-item-content>
                      </v-list-item>


                      
                    </v-list>
                  </v-card>
                </v-col>
                <v-col cols="12" md="4">
                  <v-card class="max-auto" max-height="400">
                    <v-img class="white--text align-end" height="150px" src="card.jpg"></v-img>
                    <v-card-title class="pb-0">Titulo 03 qualquer </v-card-title>
                    <v-card-text class="text-primary">
                      <div>Pew de mais </div>
                      <div>Pew de menos </div>
                    </v-card-text>
                  </v-card>
                </v-col>  
              </v-row>

              </v-container>

              
               </v-col>

               <v-col cols="12" md="4">

              <!-- <v-container>
                
                <v-row>
                  <v-col cols="12" md12>

                  <v-list-item>
                    <v-list-item-avatar>
                      <v-img src="img1.png"></v-img>
                    </v-list-item-avatar>
                    <v-list-item-content>
                      <v-list-item-title>Titululo qualquer 03 </v-list-item-title>
                      <v-list-item-subtitle> sub qualquer</v-list-item-subtitle>
                    </v-list-item-content>
                    <v-list-item-action>
                      <v-icon>fas fa-sign-out-alt</v-icon>
                    </v-list-item-action>
                  </v-list-item>

                  <v-divider></v-divider>
                
                </v-col>
                <v-col cols="12" m12>

                  <v-list-item>
                    <v-list-item-avatar color="grey">
                      <v-icon color="green">fas fa-dollar-sign</v-icon>
                    </v-list-item-avatar>

                     <v-list-item-content>
                      <v-list-item-subtitle>Heisenberg</v-list-item-subtitle>
                      <v-list-item-title>qualquer 007</v-list-item-title>
                      <v-list-item-action>
                        <v-icon color="indigo" large>fab fa-cc-visa</v-icon>
                      </v-list-item-action>
                    </v-list-item-content>
                  </v-list-item>

                  <v-list-item>
                    <v-list-item-avatar color="grey">
                      <v-icon color="green">fas fa-dollar-sign</v-icon>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-subtitle>Heisenberg</v-list-item-subtitle>
                      <v-list-item-title>qualquer 007</v-list-item-title>
                      <v-list-item-action>
                        <v-icon color="indigo" large>fab fa-cc-visa</v-icon>
                      </v-list-item-action>
                    </v-list-item-content> 
                  </v-list-item>
                  

                  <v-list-item>
                    <v-list-item-avatar color="grey">
                      <v-icon color="green">fas fa-dollar-sign</v-icon>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-subtitle>Heisenberg</v-list-item-subtitle>
                      <v-list-item-title>qualquer 007</v-list-item-title>
                      <v-list-item-action>
                        <v-icon color="indigo" large>fab fa-cc-visa</v-icon>
                      </v-list-item-action>
                    </v-list-item-content>
                  </v-list-item>
                  
                  <v-divider></v-divider>

                </v-col>

                <v-list-item-action color="green accent-1">
                  <v-icon color="light-green">fas fa-plus</v-icon>
                  <v-list-item-content>ADD </v-list-item-content>
                </v-list-item-action>
                  
                </v-row>
              </v-container> -->
            </v-col>
          </v-row>
        </v-app>
      </v-layout>
    </v-container>
  </v-app>

</template>

<script>
// @ is an alias to /src


export default {
  data: () => ({
    chartDatat: [
      ["I_A","V_A","W_A","T"],
      ["1",128,235,1],
      ["1",129,225,2],
      ["1",127,127,3],
      ["1",130,129,4],
    ],
    chartOptions: {
      chart: {
        title: "company Performance",
        subtitle: "I_A, V_A, and T: 1-1"
      }
    }
  }),

  computed: {
    theme() {
      return (this.$vuetify.theme.dark) ? 'dark' : 'light' 
    }
  }
}
</script>

<style scoped>
.rounded{
  border-radius: 30px;
}
.ligne{
  border-right: solid 1px #95a5a6;
}
</style>
