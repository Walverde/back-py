<template>
    <input v-model="text" :style ="style"/>
</template>
<script>
export default {
    name:"TextInput",
    props:{
        color: {
            type: String,
            default: "red",
        },
        width:{
            type: Number,
            default: 1100,
        }
    },
    data(){
        return{
            text:'Insira o texto',
        }
    },
    computed:{
        style(){
            return{
                color: this.color,
                width: (this.text.length * 10 )+ 'px',
            };
        }
    }
    
}
</script>

<style scoped>

</style>