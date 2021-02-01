import Vue from "vue";
import Vuetify from "vuetify/lib";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    options: { customProperties: true },
    themes: {
      light: {
        primary: "#233237",
        secondary: "#EAC67A",
        accent: "#592B26",
      },
    },
  },
});
