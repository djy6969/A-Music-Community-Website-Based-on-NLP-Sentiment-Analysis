<template>
  <div id="app">
    <Layout />
    <Player />
    <MiniPlayer />
    <Playlist />
    <ShareReader />
  </div>
</template>

<script>
import Layout from "@/layout"
import MiniPlayer from "@/components/mini-player"
import Playlist from "@/components/playlist"
import Player from "@/components/player"
import ShareReader from "@/components/share-reader"

export default {
  metaInfo() {
    return {
      title: "Daring Music Community"
    }
  },
  components: { Layout, MiniPlayer, Playlist, Player, ShareReader },
  computed: {
    ifCustomer() {
      if (this.$cookies.get('auth') !== null) {
        return this.$cookies.get('auth').role !== 2
      } else {
        return false
      }

    }
  }
}
</script>

<style lang="scss">
#app {
  height: 100%;
  background-color: var(--body-bgcolor);
  font-size: $font-size;
}
</style>
