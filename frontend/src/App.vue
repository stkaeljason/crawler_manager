
<template>
  <!-- <link rel="shortcut icon" href="./assets/logo0.ico"> -->
  <header>
    <div id="app">
      <link rel="shortcut icon" href="./assets/logo0.ico">
      <img class="logo" src="./assets/flowler.jpg" style="height:100px" alt="Nav logo">
      <router-view/>
    </div>
  </header>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

logo {
  text-align: left;
}
</style>
