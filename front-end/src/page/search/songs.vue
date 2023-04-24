// search details
<template>
  <div class="search-songs">
    <WithPagination
      :getDataParams="searchParams"
      :limit="30"
      :scrollTarget="searchRoot.$refs && searchRoot.$refs.header"
      :total="songCount"
      @getDataSuccess="newOnGetSearch"
      :keywords="this.keywords">
      <div class="table">
        <SongTable
          :highlightText="keywords"
          :renderNameDesc="renderNameDesc"
          :songs="songs"
          :stripe="true"
        />
      </div>
    </WithPagination>
  </div>
</template>

<script type="text/ecmascript-6">
import { getSearch } from "@/api"
import SongTable from "@/components/song-table"
import WithPagination from "@/components/with-pagination"
import {createSong, newCreateSong, newRequest} from "@/utils"

export default {
  async created() {

  },
  inject: ["searchRoot"],
  data() {
    return {
      songs: [],
      songCount: 0,
      currentPage: 1
    }
  },
  methods: {
    getSearch,
    onGetSearch(result) {
      const {
        result: { songs, songCount }
      } = result
      this.songs = songs.map(song => {
        const { id, mvid, name, alias, artists, duration, album } = song
        return createSong({
          id,
          name,
          alias,
          artists,
          duration,
          mvId: mvid,
          albumName: album.name,
          albumId: album.id
        })
      })

      // update the number of search results
      this.songCount = songCount
      this.searchRoot.onUpdateCount(songCount)
    },
    newOnGetSearch(songs) {
      this.songs = songs.map(song => {
        const { seq, id, name, img, mvId, artists, url, duration, durationSecond, albumName, albumId } = song
        return newCreateSong({
          id: seq,
          oldId: id,
          name,
          artists,
          artistsText: artists,
          url,
          duration,
          durationSecond,
          mvId,
          albumName,
          albumId,
          img
        })
      })
      // update the number of search results
      this.songCount = this.songs.length
      this.searchRoot.onUpdateCount(this.songs.length)
    },
    renderNameDesc(scope) {

      // new
      // const single = Object.values(scope.row)
      // return single.map(desc => (
      //   <HighlightText
      //     class="name-desc"
      //     text={desc}
      //     highlightText={this.keywords}
      //   />
      // ))

      // const { alias } = scope.row
      // return alias.map(desc => (
      //   <HighlightText
      //     class="name-desc"
      //     text={desc}
      //     highlightText={this.keywords}
      //   />
      // ))
    }
  },
  computed: {
    keywords() {
      return this.searchRoot.keywords
    },
    searchParams() {
      return { keywords: this.keywords }
    }
  },
  components: {
    SongTable,
    WithPagination
  }
}
</script>

<style lang="scss" scoped>
.search-songs {
  .table {
    .name-desc {
      display: block;
      margin-top: 8px;
      color: var(--font-color-grey-shallow);
      @include text-ellipsis;
    }
  }

  .pagination {
    margin-top: 16px;
    text-align: right;
  }
}
</style>
