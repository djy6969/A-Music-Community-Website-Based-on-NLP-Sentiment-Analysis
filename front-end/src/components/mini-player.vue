// bottom music player
<template>
  <div class="mini-player" id="mini-player">
    <!-- 歌曲内容 -->
    <div class="song">
      <template v-if="hasCurrentSong">
        <div @click="togglePlayerShow" class="img-wrap">
          <div class="mask"></div>
          <img v-lazy="$utils.genImgUrl(currentSong.img, 80)" class="blur" />
          <div class="player-control">
            <Icon :size="24" :type="playControlIcon" color="white" />
          </div>
        </div>
        <div class="content">
          <div class="top">
            <p class="name">{{ currentSong.name }}</p>
            <p class="split">-</p>
            <p class="artists">{{ currentSong.artistsText }}</p>
          </div>
          <div class="time">
            <span class="played-time">
              {{$utils.formatTime(currentTime) }}
            </span>
            <span class="split">/</span>
            <span class="total-time">
              {{ currentSong.duration }}
            </span>
          </div>
        </div>
      </template>
    </div>
    <!-- 控制台 -->
    <div class="control">
      <Icon :size="24" @click="prev" class="icon" type="prev" />
      <el-popover
        :value="isPlayErrorPromptShow"
        placement="top"
        trigger="manual"
        width="160"
      >
        <p>click to play</p>
        <div @click="togglePlaying" class="play-icon" slot="reference">
          <Icon :size="24" :type="playIcon" />
        </div>
      </el-popover>

      <Icon :size="24" @click="next" class="icon" type="next" />
    </div>

    <div class="mode">
<!--      <Share :shareUrl="shareUrl" class="mode-item" v-show="hasCurrentSong" />-->

      <!-- if user favorites this music -->
        <Icon
          :type="favoritesStyle"
          @click="changeFavoritesState"
          class="mode-item"
          slot="reference"
          v-if="ifShowFavoritesButton"
        />
      <!-- 模式 -->
      <el-popover placement="top" trigger="hover" width="160">
        <p>{{ playModeText }}</p>
        <Icon
          :size="20"
          :type="modeIcon"
          @click="onChangePlayMode"
          class="mode-item"
          slot="reference"
        />
      </el-popover>
      <!-- 播放列表 -->
      <el-popover
        :value="isPlaylistPromptShow"
        placement="top"
        trigger="manual"
        width="160"
      >
        <p>music list is updated</p>
        <Icon
          :size="20"
          @click="togglePlaylistShow"
          class="mode-item"
          slot="reference"
          type="playlist"
        />
      </el-popover>
      <!-- 音量 -->
      <div class="volume-item">
        <Volume :volume="volume" @volumeChange="onVolumeChange" />
      </div>
    </div>
    <div class="progress-bar-wrap">
      <ProgressBar
        :disabled="!hasCurrentSong"
        :percent="playedPercent"
        @percentChange="onProgressChange"
      />
    </div>
    <audio
      :src="currentSong.url"
      @canplay="ready"
      @ended="end"
      @timeupdate="updateTime"
      ref="audio"
    ></audio>
  </div>
</template>

<script type="text/ecmascript-6">
import {
  mapState,
  mapMutations,
  mapGetters,
  mapActions
} from "@/store/helper/music"
import Storage from "good-storage"
import Share from "@/components/share"
import {VOLUME_KEY, PLAY_MODE, playModeMap, isDef, newRequest} from "@/utils"
import ProgressBar from "@/base/progress-bar.vue";
import Volume from "@/base/volume.vue";
import Icon from "@/base/icon.vue";

const DEFAULT_VOLUME = 0.75
export default {
  data() {
    return {
      isPlayErrorPromptShow: false,
      songReady: false,
      volume: Storage.get(VOLUME_KEY, DEFAULT_VOLUME),
    }
  },
  async mounted() {
    await this.getUserFavorites()
    this.audio.volume = this.volume
  },
  methods: {
    getUserFavorites() {
      if (this.$cookies.get('auth') !== null) {
        newRequest.post('/collection/getFavoritesSongs',
            {
              userId: this.$cookies.get('auth').userid
            }
        ).then((res) =>{
          // vuex mutations
          this.setUserFavoritesList(res.data)
        })
      }
    },
    togglePlaying() {
      if (!this.currentSong.id) {
        return
      }
      this.setPlayingState(!this.playing)
    },
    ready() {
      this.songReady = true
    },
    async play() {
      if (this.songReady) {
        try {
          await this.audio.play()
          if (this.isPlayErrorPromptShow) {
            this.isPlayErrorPromptShow = false
          }
        } catch (error) {
          // 提示用户手动播放
          this.isPlayErrorPromptShow = true
          this.setPlayingState(false)
        }
      }
    },
    pause() {
      this.audio.pause()
      // clear interval
      clearInterval(this.ifRestart)
      this.setIfRestart(0)
    },
    updateTime(e) {
      const time = e.target.currentTime
      this.setCurrentTime(time)
    },
    prev() {
      if (this.songReady) {
        this.startSong(this.prevSong)
        // vuex
        this.setFavorites(this.userFavoritesList.includes(this.currentSong.oldId))
        clearInterval(this.ifRestart)
        this.setIfRestart(0)

        // if not start playing, repeat
        this.setIfRestart(setInterval(() => {
          if (this.currentTime === 0 ) {
            this.startSong(this.currentSong)
          } else {
            clearInterval(this.ifRestart)
            this.setIfRestart(0)
          }
        }, 3500))
      }
    },
    next() {
      if (this.songReady) {
        this.startSong(this.nextSongButton)
        // vuex
        this.setFavorites(this.userFavoritesList.includes(this.currentSong.oldId))
        clearInterval(this.ifRestart)
        this.setIfRestart(0)

        // if not start playing, repeat
        this.setIfRestart(setInterval(() => {
          if (this.currentTime === 0 ) {
            this.startSong(this.currentSong)
          } else {
            clearInterval(this.ifRestart)
            this.setIfRestart(0)
          }
        }, 3500))
      }
    },
    end() {
      if (this.songReady) {
        this.startSong(this.nextSong)
      }
    },
    onProgressChange(percent) {
      this.audio.currentTime = this.currentSong.durationSecond * percent
      this.setPlayingState(false)
    },
    onVolumeChange(percent) {
      this.audio.volume = percent
      Storage.set(VOLUME_KEY, percent)
    },
    onChangePlayMode() {
      const modeKeys = Object.keys(playModeMap)
      const currentModeIndex = modeKeys.findIndex(
        key => playModeMap[key].code === this.playMode
      )
      const nextIndex = (currentModeIndex + 1) % modeKeys.length
      const nextModeKey = modeKeys[nextIndex]
      const nextMode = playModeMap[nextModeKey]
      this.setPlayMode(nextMode.code)
      Storage.set(PLAY_MODE, nextMode.code)
    },
    togglePlaylistShow() {
      this.setPlaylistShow(!this.isPlaylistShow)
    },
    togglePlayerShow() {
      this.setPlayerShow(!this.isPlayerShow)
    },
    changeFavoritesState() {
      // axios
      console.log("change favorites state")
      if (this.ifAddedToFavorites) {
        // exist in favorites
        newRequest.post('/collection/deleteMusicFromCollection',
            {
              userId: this.$cookies.get('auth').userid,
              musicId: this.currentSong.oldId
            }
        ).then((res) =>{
          // Vuex actions
          const left = this.userFavoritesList
          left.splice(this.userFavoritesList.indexOf(this.currentSong.oldId), 1)
          this.changeUserFavorites({"newFavoritesState": !this.ifAddedToFavorites, "newUserFavoritesList": left})
        })
      } else {
        // doesn't exist
        newRequest.post('/collection/addMusicToCollection',
            {
              userId: this.$cookies.get('auth').userid,
              musicId: this.currentSong.oldId
            }
        ).then((res) =>{
          // Vuex actions
          const tem = this.userFavoritesList
          tem.push(this.currentSong.oldId)
          this.changeUserFavorites({"newFavoritesState": !this.ifAddedToFavorites, "newUserFavoritesList": tem})
        })
      }
    },
    ...mapMutations([
      "setCurrentTime",
      "setPlayingState",
      "setPlayMode",
      "setPlaylistShow",
      "setPlayerShow",
      "setFavorites",
      "setUserFavoritesList",
      "setIfRestart"
    ]),
    ...mapActions(["startSong", "changeUserFavorites"])
  },
  watch: {
    currentSong(newSong, oldSong) {
      // 清空了歌曲
      if (!newSong.id) {
        this.audio.pause()
        this.audio.currentTime = 0
        return
      }
      // 单曲循环
      if (oldSong && newSong.id === oldSong.id) {
        this.setCurrentTime(0)
        this.audio.currentTime = 0
        this.play()
        return
      }
      this.songReady = false
      if (this.timer) {
        clearTimeout(this.timer)
      }
      this.timer = setTimeout(() => {
        this.play()
      }, 1000)
    },
    playing(newPlaying) {
      this.$nextTick(() => {
        newPlaying ? this.play() : this.pause()
      })
    }
  },
  computed: {
    hasCurrentSong() {
      return isDef(this.currentSong.id)
    },
    checkLogin(){
      return this.$cookies.get('auth') !== null
          ? this.$cookies.get('auth').userid
          : ''
    },
    playIcon() {
      return this.playing ? "pause" : "play"
    },
    currentMode() {
      return playModeMap[this.playMode]
    },
    modeIcon() {
      return this.currentMode.icon
    },
    favoritesState() {
      // judge state based on Vuex
      return this.ifAddedToFavorites
    },
    favoritesStyle() {
      // judge state based on Vuex
      if (this.favoritesState) {
        // added
        return "fontawesome fa-solid fa-heart"
      } else {
        // not added
        return "fontawesome fa-regular fa-heart"
      }
    },
    ifShowFavoritesButton() {
      return !!(this.hasCurrentSong && this.checkLogin !== '')
    },
    playModeText() {
      return this.currentMode.name
    },
    audio() {
      return this.$refs.audio
    },
    // 播放的进度百分比
    playedPercent() {
      const { durationSecond } = this.currentSong
      return Math.min(this.currentTime / durationSecond, 1) || 0
    },
    playControlIcon() {
      return this.isPlayerShow ? "shrink" : "open"
    },
    shareUrl() {
      return `${window.location.origin}?shareMusicId=${this.currentSong.id}`
    },
    ...mapState([
      "currentSong",
      "currentTime",
      "playing",
      "playMode",
      "isPlaylistShow",
      "isPlaylistPromptShow",
      "isPlayerShow",
      "ifAddedToFavorites",
      "userFavoritesList",
      "ifRestart"
    ]),
    ...mapGetters(["prevSong", "nextSong", "nextSongButton"])
  },
  components: {Icon, Volume, ProgressBar, Share }
}
</script>

<style lang="scss" scoped>
.mini-player {
  position: relative;
  position: fixed;
  z-index: $mini-player-z-index;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  height: $mini-player-height;
  padding: 8px 16px;
  padding-right: 24px;
  background: var(--body-bgcolor);

  .song {
    display: flex;
    flex: 4;
    overflow: hidden;

    .img-wrap {
      position: relative;
      margin-right: 8px;
      border-radius: 6px;
      overflow: hidden;
      cursor: pointer;
      @include img-wrap(40px);

      img {
        &.blur {
          filter: blur(2px);
        }
      }

      .player-control {
        @include abs-center;
      }

      .mask {
        @include abs-stretch;
        background: rgba(0, 0, 0, 0.2);
      }
    }

    .content {
      flex: 1;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-around;

      .top {
        display: flex;
        align-items: flex-end;
        white-space: nowrap;

        .name {
          color: var(--font-color-white);
          @include text-ellipsis;
        }

        .split {
          font-size: $font-size-xs;
          margin: 0 4px;
        }

        .artists {
          font-size: $font-size-xs;
          @include text-ellipsis;
        }
      }

      .time {
        font-size: $font-size-xs;
        color: var(--font-color-grey);

        .split {
          margin: 0 4px;
        }
      }
    }
  }

  .control {
    position: absolute;
    height: 100%;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 200px;
    @include flex-center();

    .play-icon {
      @include flex-center();
      position: relative;
      width: 45px;
      height: 45px;
      margin: 0 16px;
      border-radius: 50%;
      background: $theme-color;
      cursor: pointer;

      i {
        color: #fff;
      }
      .icon-play {
        transform: translateX(1px);
      }
    }

    .icon {
      color: $theme-color;
    }
  }

  .mode {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex: 6;

    .mode-item {
      display: block;
      margin-right: 16px;
      width: 22px;
    }

    .volume-item {
      margin-right: 22px;
    }
  }

  .progress-bar-wrap {
    position: absolute;
    left: 0;
    right: 0;
    top: -14px;
  }
}

.icon {
  color: var(--font-color);
  cursor: pointer;
}
</style>
