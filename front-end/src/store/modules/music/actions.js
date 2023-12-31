import storage from 'good-storage'
import {PLAY_HISTORY_KEY, getSongImg, newRequest} from '@/utils'

export default {
  // 整合歌曲信息 并且开始播放
  async startSong({ commit, state }, rawSong) {
    // 浅拷贝一份 改变引用
    // 1.不污染元数据
    // 2.单曲循环为了触发watch
    const song = Object.assign({}, rawSong)
    console.log(song)
    if (!song.img) {
      if (song.albumId) {
        song.img = await getSongImg(song.id, song.albumId)
      }
    }
    commit('setCurrentSong', song)
    commit('setPlayingState', true)
    // 历史记录
    const { playHistory } = state
    const playHistoryCopy = playHistory.slice()
    const foundIndex = playHistoryCopy.findIndex(({ id }) => song.id === id)
    if (foundIndex !== -1) {
      // 删除旧那一项, 插入到最前面
      playHistoryCopy.splice(foundIndex, 1)
    }
    playHistoryCopy.unshift(song)
    commit('setPlayHistory', playHistoryCopy)
    storage.set(PLAY_HISTORY_KEY, playHistoryCopy)

    //update view counts
    // newRequest.get('/music/updateViewCounts')
    //     .then((res) =>{
    //       console.log("update view counts")
    //     })
  },
  clearCurrentSong({ commit }) {
    commit('setCurrentSong', {})
    commit('setPlayingState', false)
    commit('setCurrentTime', 0)
  },
  clearPlaylist({ commit, dispatch }) {
    commit('setPlaylist', [])
    dispatch('clearCurrentSong')
  },
  clearHistory({ commit }) {
    const history = []
    commit('setPlayHistory', history)
    storage.set(PLAY_HISTORY_KEY, history)
  },
  addToPlaylist({ commit, state }, song) {
    const { playlist } = state
    const copy = playlist.slice()
    if (!copy.find(({ id }) => id === song.id)) {
      copy.unshift(song)
      commit('setPlaylist', copy)
    }
  },
  changeUserFavorites({ commit }, dict) {
    commit('setFavorites', dict.newFavoritesState)
    commit('setUserFavoritesList', dict.newUserFavoritesList)
  }
}