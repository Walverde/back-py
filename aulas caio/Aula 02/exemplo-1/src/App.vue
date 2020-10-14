<template>
  <div id="app">
    <text-input color = "green"/>
  </div>
</template>
<script>
import  TextInput from './components/TextInput'

export default {
  components: {TextInput}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
