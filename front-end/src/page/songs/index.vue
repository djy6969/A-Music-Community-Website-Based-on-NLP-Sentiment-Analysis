// The newest music page
<template>
  <div class="songs">
<!--  the tags  -->
<!--    <div class="tabs">-->
<!--      <Tabs-->
<!--        :tabs="tabs"-->
<!--        @tabChange="getSongs"-->
<!--        align="right"-->
<!--        type="small"-->
<!--        v-model="activeTabIndex"-->
<!--      />-->
<!--    </div>-->
<!--  displayed songs  -->
    <SongTable
      :songs="songs"
      header-row-class-name="header-row"
    />
  </div>
</template>

<script type="text/ecmascript-6">
import {getTopSongs} from "@/api"
import {createSong, newCreateSong, newRequest} from "@/utils"
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
      console.log(data)
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
      //await this.getSongs()
      await this.getAllMusic()
    },
    async getAllMusic() {
      newRequest.post('/api/music/getMusicResource',
          {
            num: 50
          }
      ).then((res) =>{
        const allSongs = Object.values(res.data)
        console.log(allSongs)
        this.songs = allSongs.map(song =>{
          const {
            id,
            name,
            artists,
            duration,
            durationSecond,
            mvId,
            img,
            albumName,
            url
          } = song
          return newCreateSong({
            id,
            name,
            artists,
            artistsText: artists,
            duration,
            durationSecond,
            albumName,
            img,
            mvId,
            url
          })
        })
      })
    },
  },
  components: {
    SongTable,
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
