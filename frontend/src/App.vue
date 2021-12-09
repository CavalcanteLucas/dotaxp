<template>
  <div id="app">
    <div class="container">
      <div id="nav">
        <router-link to="/">
          Home
        </router-link> |
        <router-link to="/stats-progression">
          Stats Progression
        </router-link>
      </div>
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
    name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

html,
body {
  height: 100%;
  width: 100%;
  background-color: black;
}
body {
  display: table;
  margin: 0;
}
#top,
#bottom {
  width: 100%;
  background: yellow;
  display: table-row;
}
#top {
  height: 50px;
}
#bottom {
  background: lightgrey;
  height: 100%;
}

@import'~bootstrap/dist/css/bootstrap.css'
</style>
