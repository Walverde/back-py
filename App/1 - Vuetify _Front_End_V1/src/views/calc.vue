<template>
    <v-container>
        <v-card>
            <v-card-title>Calculadora</v-card-title>
            <v-card-text >
                    <v-text-field
                    v-model="expression"
                    outlined 
                    label="Digite uma expressão" 
                    hint="Massa, de mais" 
                    color="primary"
                    />
                    <v-layout class="col-6 col-md-12 pa-0 pa-ma-15" wrap justify-center>
                        <v-btn
                        :class="button ?['col-3', 'ma-1'] : ['col-7','ml-15', 'mr-15']" 
                        v-for="(button,i) in buttons" 
                        :key="i" 
                        @click="buttonClick(button)"
                        >
                        {{button}}
                    </v-btn>
                    </v-layout>
                    <v-btn @click="calc">=</v-btn>
                    <v-label>{{result}}</v-label>
                    <v-alert v-if="error" color="error" >{{ error }}</v-alert>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script>
export default {
    name:"Calc",

    data(){
        return{
            expression: "",
            result: "",
            buttons:[1,2,3,4,5,6,7,8,9,0, '+','-','*','/'],
        };
    },
    methods:{
        buttonClick(value){
            this.expression +=value;
        },
        calc(){
            try{
                this.result = eval(this.expression);
            }catch(e){
                this.error = "Incorreto";
            }
            
        },
    },
    
};
</script>

<style scoped>

</style>