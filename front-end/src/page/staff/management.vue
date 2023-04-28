<template>

  <div class="container">

    <div class="el-main">
      <el-button type="warning" @click="dialogFormVisible = true">Add New Music</el-button>

      <el-dialog title="Please enter new music information" :visible.sync="dialogFormVisible">
        <el-form :inline="true" :model="form">
          <el-form-item label="Music Name" :label-width="formLabelWidth">
            <el-input v-model="form.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Music Id" :label-width="formLabelWidth">
            <el-input v-model="form.id" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Description" :label-width="formLabelWidth">
            <el-input v-model="form.description" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Artist" :label-width="formLabelWidth">
            <el-input v-model="form.artist" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="Duration" :label-width="formLabelWidth">
            <el-input v-model="form.duration" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="formCancel">Cancel</el-button>
          <el-button type="primary" @click="formSubmit">Submit</el-button>
        </div>
      </el-dialog>

    </div>

    <div class="el-main">

      <el-table :data="tableData" stripe border height="550" >
        <el-table-column prop="name" label="Music Name" width="140">
        </el-table-column>
        <el-table-column prop="duration" label="Music Duration" width="120">
        </el-table-column>
        <el-table-column prop="artistsText" label="Artists Name">
        </el-table-column>

        <el-table-column label="Operation">
          <template v-slot="scope">
            <el-button type="primary" @click="changeMusicState(scope.row)">{{ ifAvailable(scope.row.usable) }}</el-button>
          </template>
        </el-table-column>
      </el-table>

    </div>

  </div>

</template>

<script type="text/ecmascript-6">

import { newCreateSong, newRequest } from "@/utils"
export default {
  name: "staff-management",
  data() {
    return {
      tableData: [],
      // add new music
      dialogFormVisible: false,
      form: {
        name: '',
        id: '',
        description: '',
        artist: '',
        duration: '',
      },
      formLabelWidth: '120px'
    }
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {
      // upload new music

      // show all musics including those users can't play
      this.staffGetAllMusic()

    },
    staffGetAllMusic() {
      newRequest.get('/music/managerGetAllMusicResource'
      ).then((res) =>{
        const allSongs = Object.values(res.data)
        this.tableData = allSongs.map(song =>{
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
            url,
            usable
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
            url,
            usable
          })
        })
        console.log(this.tableData)
      })
    },
    changeMusicState(row) {
      console.log(row)
      const newState = 1 - row.usable
      newRequest.post('/music/manage_music_usability',
          {
            music_id: row.oldId,
            usability: newState
          }
      ).then((res) =>{
        console.log(res.data)
        row.usable = newState
      })
    },
    ifAvailable(state) {
      return state === 1
          ? "Deactivate"
          : "Activate"
    },
    formSubmit() {
      this.dialogFormVisible = false

      // axios

    },
    formCancel() {
      this.dialogFormVisible = false
      this.form = {
        name: '',
        id: '',
        description: '',
        artist: '',
        duration: '',
      }
    }
  },
}
</script>

<style lang="scss">

.container {
  padding: 12px;
}

</style>