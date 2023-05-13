<template>

  <div class="container">

    <div class="el-main">
      <el-button type="warning" @click="dialogFormVisible = true">Add New Music</el-button>

      <el-dialog title="Please Enter New Music Information" :visible.sync="dialogFormVisible">
        <el-form :inline="true" :model="form">

          <el-form-item>
            <el-upload
                class="upload"
                ref="upload"
                action="/music/add_new_music"
                :file-list="fileList"
                :auto-upload="false"
                :on-change="handleChange"
                :on-preview="handlePreview"
                :on-remove="handleRemove"
                :limit="1"
                multiple="multiple"
                accept=".mp3,">
              <el-button slot="trigger" size="small" type="primary" @click="ChooseMusicFile">Choose a Music (.mp3 file)</el-button>
            </el-upload>
          </el-form-item>

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

          <el-form-item>
            <el-upload
                action="/music/add_new_music"
                :auto-upload="false"
                list-type="picture-card"
                :limit="1"
                multiple="multiple"
                accept=".jpg,"
                :on-preview="handlePictureCardPreview"
                :on-remove="handleImageRemove"
                :on-change="handleImageChange">
              <i class="el-icon-plus"></i>
              <div slot="tip" class="el-upload__tip">Upload an Image as Music Cover (.jpg file)</div>
            </el-upload>

            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
          </el-form-item>

        </el-form>

        <div slot="footer" class="dialog-footer">
          <el-button @click="formClear">Cancel</el-button>
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
      formLabelWidth: '120px',
      imageList: [],
      fileList: [],
      dialogImageUrl: '',
      dialogVisible: false,
      multiple: false
    }
  },
  mounted() {
    this.init()
  },
  methods: {
    init() {

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
    handleImageChange(file, fileList) {
      this.imageList = fileList
      console.log(this.imageList)
    },
    handleImageRemove(file, fileList) {
      //移除图片
      console.log(file, fileList)
    },
    handlePictureCardPreview(file) {
      //图片预览
      this.dialogImageUrl = file.url
      this.dialogVisible = true
    },
    beforeMusicImageUpload(file){
      const _this = this
      return new Promise(function(resolve, reject) {
        const reader = new FileReader()
        // 这里是最关键的一步，转换成base64
        reader.readAsDataURL(file)
        reader.onload = function(event) {
          //定义参数获取图片路径
          _this.imageList.push(event.target.result)
        }
      })
    },
    ChooseMusicFile () {
      this.fileList = []
    },
    handleChange (file, fileList) {
      this.fileList = fileList
      console.log(this.fileList)
    },
    //自定义上传文件
    uploadMusic (file) {
      this.formData.append("file", file.file)
      console.log(file.file, "sb2")
    },
    //删除文件
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    // 点击文件
    handlePreview (file) {
      console.log(file)
    },
    formSubmit() {

      // prepare formData
      let formData = new FormData()
      // Get the file that contains the fileList and put it in formData
      formData.append("music", this.fileList[0].raw)
      formData.append("image", this.imageList[0].raw)
      formData.append("music_id", this.form.id)
      formData.append("title", this.form.name)
      formData.append("description", this.form.description)
      formData.append("artist", this.form.artist)
      formData.append("duration", this.form.duration)

      // axios
      newRequest.post('/music/add_new_music',
          formData,
          {
            "Content-Type": "multipart/form-data;charset=utf-8"
          }
      ).then((res) =>{
        console.log(res.data)
        this.formClear()
      })

    },
    formClear() {
      this.dialogFormVisible = false
      this.form = {
        name: '',
        id: '',
        description: '',
        artist: '',
        duration: '',
      }
      this.imageList = []
      this.fileList = []
    }
  },
}
</script>

<style lang="scss">

.container {
  padding: 12px;
}

</style>