export default {
  setUser(state, user) {
    state.user = user
  },
  setUserPlaylist(state, playlist) {
    state.userPlaylist = playlist
  },
  setUserRole(state, newRole) {
    console.log(newRole)
    state.userRole = newRole
  }
}
