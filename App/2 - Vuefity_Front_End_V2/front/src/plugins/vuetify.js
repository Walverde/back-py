
import '@fortawesome/fontawesome-free/css/all.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import { colors } from 'vuetify/lib';
//import colors from 'vuetify/lib/util/colors';
import vueGoogleCharts from 'vue-google-charts';


Vue.use(vueGoogleCharts)
Vue.use(Vuetify);

export default new Vuetify({
    icons: {
        iconfont:'md' || 'fa'
    },
    theme: {
        themes: {
            light:{
                background: colors.blueGrey.accent2,
            },
            dark:{
                background: colors.blueGrey,
            }
        },
    }
});
