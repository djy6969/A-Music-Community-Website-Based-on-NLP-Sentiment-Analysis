// The newest music page
<template>
  <div class="songs">
<!--  the tags  -->
    <div class="tabs">
      <Tabs
        :tabs="tabs"
        @tabChange="getSongs"
        align="right"
        type="small"
        v-model="activeTabIndex"
      />
    </div>
<!--  displayed songs  -->
    <Song></Song>
    <SongTable
      :songs="songs"
      header-row-class-name="header-row"
    />
<!--    <audio controls>-->
<!--      <source src="../../../../back-end/static/music/04cHqPMD4So.mp3"/>-->
<!--    </audio>-->
  </div>
</template>

<script type="text/ecmascript-6">
import {getTopSongs} from "@/api"
import {createSong, newRequest} from "@/utils"
import SongTable from "@/components/song-table"
import Song from "@/components/song"
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
      // const res = await newRequest.get('/music/getAllMusicResources')
      // this.allSongs = res.data
      // for(let i = 0;i < this.allSongs.length;i++){
      //   const re = await this.getMusic(this.allSongs[i][0])
      //   this.allSongs[i] = re.data
      //   // this.songs[i].albumId = re.data.albumId
      //   // this.songs[i].albumName = re.data.albumName
      //   // this.songs[i].artists = re.data.artists
      //   // this.songs[i].artistsText = re.data.artistsText
      //   // this.songs[i].duration = re.data.duration
      //   // this.songs[i].durationSecond = re.data.durationSecond
      //   // this.songs[i].id = re.data.id
      //   // this.songs[i].img = re.data.img
      //   // this.songs[i].mvId = re.data.mvId
      //   // this.songs[i].name = re.data.name
      //   // this.songs[i].url = re.data.url
      // }
      // console.log(this.songs)
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
    SongTable,
    Song
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
