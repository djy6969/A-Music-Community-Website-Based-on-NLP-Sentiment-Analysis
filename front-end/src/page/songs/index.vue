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
import {getTopSongs} from "@/api"
import {createSong, newRequest} from "@/utils"
import SongTable from "@/components/song-table"

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
      songs: [],
      newSongs: []
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
    },
    async getTest() {
      const res = await newRequest.get('/music/getAllMusicResources')
      for(let i = 0;i < res.data.length;i++){
        this.getMusic(res.data[i][0])
      }
    },
    async getMusic(data) {
      console.log(data)
      return await newRequest.post('/music/getMusicResource', data)
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
