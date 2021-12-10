<template>
  <div class="home">
    <img
      alt="Vue logo"
      src="../assets/logo.png"
      width="450"
      height="240"
    >
    <HelloWorld msg="Dota2 Beta's Tracker" />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
    name: 'Home',
    components: {
        HelloWorld
    }
}
</script>
