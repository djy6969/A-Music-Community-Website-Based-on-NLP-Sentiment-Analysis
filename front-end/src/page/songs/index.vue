// The newest music page
<template>
  <div class="songs">
    <div class="tabs">
      <Tabs
        :tabs="tabs"
        @tabChange="getSongs"
        align="right"
        type="small"
        v-model="activeTabIndex"
      />
    </div>
    <SongTable
      :songs="songs"
      header-row-class-name="header-row"
    />
  </div>
</template>

<script type="text/ecmascript-6">
import { getTopSongs } from "@/api"
import { createSong } from "@/utils"
import SongTable from "@/components/song-table"
import { newRequest } from "@/utils";

export default {
  async created() {
    this.tabs = [
      { title: "All", type: 0 },
      { title: "China", type: 7 },
      { title: "Europe and America", type: 96 },
      { title: "Japan", type: 8 },
      { title: "South Korea", type: 16 }
    ]
    this.getSongs()
    this.getTest()
  },
  data() {
    return {
      activeTabIndex: 0,
      songs: []
    }
  },
  methods: {
    async getSongs() {
      const { data } = await getTopSongs(this.tabs[this.activeTabIndex].type)
      this.songs = data.map(song => {
        const {
          id,
          name,
          artists,
          duration,
          mvid,
          album: { picUrl, name: albumName }
        } = song
        return createSong({
          id,
          name,
          artists,
          duration,
          albumName,
          img: picUrl,
          mvId: mvid
        })
      })
      // eslint-disable-next-line no-console
      console.log(this.songs)
    },
    async getTest() {
      const res = await newRequest.get('/music/getAllMusicResources')
      // eslint-disable-next-line no-console
      console.log(res.data)
    }
  },
  components: {
    SongTable
  }
}
</script>

<style lang="scss">
.songs {
  padding: 12px;

  .header-row {
    display: none;
  }
}
</style>
