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
import {ref} from "vue";

export default {
  async created() {
    this.tabs = [
      { title: "All", type: 0 },
      { title: "China", type: 7 },
      { title: "Europe and America", type: 96 },
      { title: "Japan", type: 8 },
      { title: "South Korea", type: 16 }
    ]
    this.init()
  },
  data() {
    return {
      activeTabIndex: 0,
      songs: ref([]),
      allSongs: []
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
    async init() {
      await this.getSongs()
      console.log(this.songs)
      this.getAllMusic()
    },
    async getAllMusic() {
      const res = await newRequest.get('/music/getAllMusicResources')
      this.allSongs = res.data
      for(let i = 0;i < this.allSongs.length;i++){
        const re = await this.getMusic(this.allSongs[i][0])
        this.allSongs[i] = re.data
        console.log(re.data.music_filepath)
        // this.songs[i].url = this.songs[99-i].url
        // this.songs[i].img = this.songs[99-i].img
        // this.songs[i].durationSecond = this.songs[99-i].durationSecond
        // this.songs[i].duration = this.songs[99-i].duration
      }
      console.log(this.songs)
    },
    async getMusic(data) {
      return await newRequest.post('/music/getMusicResource',
          {
            music_id: data
          }
      )
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
