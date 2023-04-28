<template>

  <div class="container">

    <div class="el-main">
      <el-button type="warning" @click="dialogFormVisible = true">Add New Music</el-button>

      <el-dialog title="Please enter new music information" :visible.sync="dialogFormVisible">
        <el-form :model="form">
          <el-form-item label="活动名称" :label-width="formLabelWidth">
            <el-input v-model="form.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="活动区域" :label-width="formLabelWidth">
            <el-select v-model="form.region" placeholder="请选择活动区域">
              <el-option label="区域一" value="shanghai"></el-option>
              <el-option label="区域二" value="beijing"></el-option>
            </el-select>
          </el-form-item>
        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFormVisible = false">取 消</el-button>
          <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
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
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
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
    open() {
      this.$prompt('请输入邮箱', '提示', {
        confirmButtonText: 'Submit',
        cancelButtonText: 'Cancel',
        inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
        inputErrorMessage: '邮箱格式不正确'
      }).then(({ value }) => {
        this.$message({
          type: 'success',
          message: '你的邮箱是: ' + value
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '取消输入'
        });
      });
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
    }
  },
}
</script>

<style lang="scss">

.container {
  padding: 12px;
}

</style>