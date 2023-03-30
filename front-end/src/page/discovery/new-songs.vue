<template>
  <div
    class="new-songs"
    v-if="list.length"
  >
    <Title>The Newest Music</Title>
    <div class="list-wrap">
      <div
        :key="listIndex"
        class="list"
        v-for="(list, listIndex) in chunkedList"
      >
        <SongCard
          :key="item.id"
          :order="getSongOrder(listIndex, index)"
          @click.native="onClickSong(listIndex, index)"
          class="song-card"
          v-bind="newNormalizeSong(item)"
          v-for="(item,index) in list"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapMutations } from "@/store/helper/music"
import { getNewSongs } from "@/api"
import SongCard from "@/components/song-card"
import {createSong, newCreateSong, newRequest} from "@/utils"

const songsLimit = 10
export default {
  async created() {
    // const { result } = await getNewSongs()
    // this.list = result
    await this.getNewSongs()
  },
  data() {
    return {
      chunkLimit: Math.ceil(songsLimit / 2),
      list: []
    }
  },
  methods: {
    getSongOrder(listIndex, index) {
      return listIndex * this.chunkLimit + index + 1
    },
    getNewSongs() {
      newRequest.post('/api/music/getMusicResource',
          {
            num: 10
          }
      ).then((res) =>{
        const allSongs = Object.values(res.data)
        console.log(allSongs)
        this.list = allSongs
      })
    },
    normalizeSong(song) {
      const {
        id,
        name,
        song: {
          mvid,
          artists,
          album: { blurPicUrl },
          duration
        }
      } = song
      return createSong({
        id,
        name,
        img: blurPicUrl,
        artists,
        duration,
        mvId: mvid
      })
    },
    newNormalizeSong(song) {
      const {
        id,
        name,
        mvId,
        artists,
        img,
        duration,
        durationSecond,
        url
      } = song
      return newCreateSong({
        id,
        name,
        img,
        artists,
        artistsText: artists,
        duration,
        durationSecond,
        mvId,
        url
      })
    },
    onClickSong(listIndex, index) {
      // 这里因为getSongOrder是从1开始显示, 所以当做数组下标需要减一
      const nomalizedSongIndex = this.getSongOrder(listIndex, index) - 1
      const nomalizedSong = this.normalizedSongs[nomalizedSongIndex]
      this.startSong(nomalizedSong)
      this.setPlaylist(this.normalizedSongs)
    },
    ...mapMutations(["setPlaylist"]),
    ...mapActions(["startSong"])
  },
  computed: {
    chunkedList() {
      return [
        this.list.slice(0, this.chunkLimit),
        this.list.slice(this.chunkLimit, this.list.length)
      ]
    },
    normalizedSongs() {
      return this.list.map(song => this.newNormalizeSong(song))
    }
  },
  components: { SongCard }
}
</script>

<style lang="scss" scoped>
.new-songs {
  margin-bottom: 36px;
  .list-wrap {
    display: flex;

    .list {
      flex: 1;
      overflow: hidden;
    }
  }
}
</style>