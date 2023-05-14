(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["StaffManagement"],{"70b3":function(t,e,i){"use strict";i.r(e);i("7f7f");var a=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container"},[e("div",{staticClass:"el-main"},[e("el-button",{attrs:{type:"warning"},on:{click:function(e){t.dialogFormVisible=!0}}},[t._v("Add New Music")]),e("el-dialog",{attrs:{title:"Please Enter New Music Information",visible:t.dialogFormVisible},on:{"update:visible":function(e){t.dialogFormVisible=e}}},[e("el-form",{attrs:{inline:!0,model:t.form}},[e("el-form-item",[e("el-upload",{ref:"upload",staticClass:"upload",attrs:{action:"/music/add_new_music","file-list":t.fileList,"auto-upload":!1,"on-change":t.handleChange,"on-preview":t.handlePreview,"on-remove":t.handleRemove,limit:1,multiple:"multiple",accept:".mp3,"}},[e("el-button",{attrs:{slot:"trigger",size:"small",type:"primary"},on:{click:t.ChooseMusicFile},slot:"trigger"},[t._v("Choose a Music (.mp3 file)")])],1)],1),e("el-form-item",{attrs:{label:"Music Name","label-width":t.formLabelWidth}},[e("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}})],1),e("el-form-item",{attrs:{label:"Music Id","label-width":t.formLabelWidth}},[e("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.id,callback:function(e){t.$set(t.form,"id",e)},expression:"form.id"}})],1),e("el-form-item",{attrs:{label:"Description","label-width":t.formLabelWidth}},[e("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.description,callback:function(e){t.$set(t.form,"description",e)},expression:"form.description"}})],1),e("el-form-item",{attrs:{label:"Artist","label-width":t.formLabelWidth}},[e("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.artist,callback:function(e){t.$set(t.form,"artist",e)},expression:"form.artist"}})],1),e("el-form-item",{attrs:{label:"Duration","label-width":t.formLabelWidth}},[e("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.duration,callback:function(e){t.$set(t.form,"duration",e)},expression:"form.duration"}}),e("p",[t._v("Duration Format: xx:xx")])],1),e("el-form-item",[e("el-upload",{attrs:{action:"/music/add_new_music","auto-upload":!1,"list-type":"picture-card",limit:1,multiple:"multiple",accept:".jpg,","on-preview":t.handlePictureCardPreview,"on-remove":t.handleImageRemove,"on-change":t.handleImageChange}},[e("i",{staticClass:"el-icon-plus"}),e("div",{staticClass:"el-upload__tip",attrs:{slot:"tip"},slot:"tip"},[t._v("Upload an Image as Music Cover (.jpg file)")])]),e("el-dialog",{attrs:{visible:t.dialogVisible},on:{"update:visible":function(e){t.dialogVisible=e}}},[e("img",{attrs:{width:"100%",src:t.dialogImageUrl,alt:""}})])],1)],1),e("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[e("el-button",{on:{click:t.formClear}},[t._v("Cancel")]),e("el-button",{attrs:{type:"primary"},on:{click:t.formSubmit}},[t._v("Submit")])],1)],1)],1),e("div",{staticClass:"el-main"},[e("el-table",{attrs:{data:t.tableData,stripe:"",border:"",height:"550"}},[e("el-table-column",{attrs:{prop:"name",label:"Music Name",width:"140"}}),e("el-table-column",{attrs:{prop:"duration",label:"Music Duration",width:"120"}}),e("el-table-column",{attrs:{prop:"artistsText",label:"Artists Name"}}),e("el-table-column",{attrs:{label:"Operation"},scopedSlots:t._u([{key:"default",fn:function(i){return[e("el-button",{attrs:{type:"primary"},on:{click:function(e){return t.changeMusicState(i.row)}}},[t._v(t._s(t.ifAvailable(i.row.usable)))])]}}])})],1)],1)])},l=[],o=(i("ac6a"),i("8615"),i("ed08")),n={name:"staff-management",data:function(){return{tableData:[],dialogFormVisible:!1,form:{name:"",id:"",description:"",artist:"",duration:""},formLabelWidth:"120px",imageList:[],fileList:[],dialogImageUrl:"",dialogVisible:!1,multiple:!1}},mounted:function(){this.init()},methods:{init:function(){this.staffGetAllMusic()},staffGetAllMusic:function(){var t=this;o["newRequest"].get("/music/managerGetAllMusicResource").then((function(e){var i=Object.values(e.data);t.tableData=i.map((function(t){var e=t.seq,i=t.id,a=t.name,l=t.artists,n=t.duration,s=t.durationSecond,r=t.mvId,u=t.img,c=t.albumName,m=t.url,d=t.usable;return Object(o["newCreateSong"])({id:e,oldId:i,name:a,artists:l,artistsText:l,duration:n,durationSecond:s,albumName:c,img:u,mvId:r,url:m,usable:d})})),console.log(t.tableData)}))},changeMusicState:function(t){console.log(t);var e=1-t.usable;o["newRequest"].post("/music/manage_music_usability",{music_id:t.oldId,usability:e}).then((function(i){console.log(i.data),t.usable=e}))},ifAvailable:function(t){return 1===t?"Deactivate":"Activate"},handleImageChange:function(t,e){this.imageList=e,console.log(this.imageList)},handleImageRemove:function(t,e){console.log(t,e)},handlePictureCardPreview:function(t){this.dialogImageUrl=t.url,this.dialogVisible=!0},beforeMusicImageUpload:function(t){var e=this;return new Promise((function(i,a){var l=new FileReader;l.readAsDataURL(t),l.onload=function(t){e.imageList.push(t.target.result)}}))},ChooseMusicFile:function(){this.fileList=[]},handleChange:function(t,e){this.fileList=e,console.log(this.fileList)},uploadMusic:function(t){this.formData.append("file",t.file),console.log(t.file,"sb2")},handleRemove:function(t,e){console.log(t,e)},handlePreview:function(t){console.log(t)},formSubmit:function(){var t=this,e=new FormData;e.append("music",this.fileList[0].raw),e.append("image",this.imageList[0].raw),e.append("music_id",this.form.id),e.append("title",this.form.name),e.append("description",this.form.description),e.append("artist",this.form.artist),e.append("duration",this.form.duration),o["newRequest"].post("/music/add_new_music",e,{"Content-Type":"multipart/form-data;charset=utf-8"}).then((function(e){console.log(e.data),t.formClear(),t.staffGetAllMusic()}))},formClear:function(){this.dialogFormVisible=!1,this.form={name:"",id:"",description:"",artist:"",duration:""},this.imageList=[],this.fileList=[]}}},s=n,r=(i("af27"),i("0c7c")),u=Object(r["a"])(s,a,l,!1,null,null,null);e["default"]=u.exports},af27:function(t,e,i){"use strict";i("cb31")},cb31:function(t,e,i){}}]);