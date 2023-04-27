// The newest music page
<template>
  <div class="songs">
    <SongTable
      :songs="songs"
      header-row-class-name="header-row"
    />
  </div>
</template>

<script type="text/ecmascript-6">
import { newCreateSong, newRequest } from "@/utils"
import SongTable from "@/components/song-table"

export default {
  async created() {
    await this.init()
  },
  data() {
    return {
      songs: [],
    }
  },
  methods: {
    async init() {
      await this.getAllMusic()
    },
    async getAllMusic() {
      newRequest.post('/music/getMusicRecommendation',
          {
            userId: this.checkLogin
          }
      ).then((res) =>{
        const allSongs = Object.values(res.data)
        console.log(allSongs)
        this.songs = allSongs.map(song =>{
          const {
            seq,
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
            id: seq,
            oldId: id,
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
  computed: {
    checkLogin(){
      return this.$cookies.get('auth') !== null
          ? this.$cookies.get('auth').userid
          : ''
    }
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
