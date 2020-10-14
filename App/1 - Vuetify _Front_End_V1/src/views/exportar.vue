<template>
    <v-container>
        <v-card>

            <v-card-title>Exportar Dados</v-card-title>
        </v-card>
            
  <v-row align= "center">
    <v-col cols= "12">
      <v-select
        :items= "pews"
                readonly
        label="Selecione o periodo"
      ></v-select>
    </v-col>
  </v-row>

  <v-row align= "center">
    <v-col cols= "12">
      <v-select
      v-model="selectedFruits"
      :items="pews"
      label="Periodo"
      multiple
      ></v-select>
    </v-col>
  </v-row>

      <v-select
      v-model="selectedFruits"
      :items="fruits"
      label="Select"
      multiple
    >
      <template v-slot:prepend-item>
        <v-list-item
          ripple
          @click="toggle"
        >
          <v-list-item-action>
            <v-icon :color="selectedFruits.length > 0 ? 'indigo darken-4' : ''">{{ icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Select All</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider class="mt-2"></v-divider>
      </template>
      <template v-slot:append-item>
        <v-divider class="mb-2"></v-divider>
        <v-list-item disabled>
          <v-list-item-avatar color="grey lighten-3">
            <v-icon>mdi-food-apple</v-icon>
          </v-list-item-avatar>

          <v-list-item-content v-if="likesAllFruit">
            <v-list-item-title>Holy smokes, someone call the fruit police!</v-list-item-title>
          </v-list-item-content>

          <v-list-item-content v-else-if="likesSomeFruit">
            <v-list-item-title>Fruit Count</v-list-item-title>
            <v-list-item-subtitle>{{ selectedFruits.length }}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-content v-else>
            <v-list-item-title>
              How could you not like fruit?
            </v-list-item-title>
            <v-list-item-subtitle>
              Go ahead, make a selection above!
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-select>
            

    </v-container>
</template>
<script>
  export default {

    data: () => ({
        ano: ['2012',
        '2020',
        '2021',
        '2022',
        '2023',
        '2024',
        '2025',
        '2026',
        '2027',
        '2028',
        '2029',
        '2030',
        '2031',
        '2032',
        ],
        mes: [
            'Janeiro',
            'Fevereiro',
            'Março',
            'Abril',
            'Maio',
            'Junho',
            'Julho',
            'Agosto',
            'Setembro',
            'Outrubro',
            'Novenbro',
            'Dezembro',
        ],
        dia: [],
        pews: [
          'Foo', 
          'Bar', 
          'Fizz', 
          'Buzz'],
      fruits: [
        'Apples',
        'Apricots',
        'Avocado',
        'Bananas',
        'Blueberries',
        'Blackberries',
        'Boysenberries',
        'Bread fruit',
        'Cantaloupes (cantalope)',
        'Cherries',
        'Cranberries',
        'Cucumbers',
        'Currants',
        'Dates',
        'Eggplant',
        'Figs',
        'Grapes',
        'Grapefruit',
        'Guava',
        'Honeydew melons',
        'Huckleberries',
        'Kiwis',
        'Kumquat',
        'Lemons',
        'Limes',
        'Mangos',
        'Mulberries',
        'Muskmelon',
        'Nectarines',
        'Olives',
        'Oranges',
        'Papaya',
        'Peaches',
        'Pears',
        'Persimmon',
        'Pineapple',
        'Plums',
        'Pomegranate',
        'Raspberries',
        'Rose Apple',
        'Starfruit',
        'Strawberries',
        'Tangerines',
        'Tomatoes',
        'Watermelons',
        'Zucchini',
      ],
      selectedFruits: [],
    }),
    computed: {
      likesAllFruit () {
        return this.selectedFruits.length === this.fruits.length
      },
      likesSomeFruit () {
        return this.selectedFruits.length > 0 && !this.likesAllFruit
      },
      icon () {
        if (this.likesAllFruit) return 'mdi-close-box'
        if (this.likesSomeFruit) return 'mdi-minus-box'
        return 'mdi-checkbox-blank-outline'
      },
    },
    methods: {
      toggle () {
        this.$nextTick(() => {
          if (this.likesAllFruit) {
            this.selectedFruits = []
          } else {
            this.selectedFruits = this.fruits.slice()
          }
        })
      },
    },

  }
</script>