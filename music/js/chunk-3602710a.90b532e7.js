(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-3602710a"],{"4d2d":function(t,e,a){},"504c":function(t,e,a){var i=a("9e1e"),n=a("0d58"),l=a("6821"),o=a("52a7").f;t.exports=function(t){return function(e){var a,s=l(e),r=n(s),u=r.length,c=0,m=[];while(u>c)a=r[c++],i&&!o.call(s,a)||m.push(t?[a,s[a]]:s[a]);return m}}},"70b3":function(t,e,a){"use strict";a.r(e);a("7f7f");var i=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container"},[e("div",{staticClass:"el-main"},[e("el-button",{attrs:{type:"warning"},on:{click:function(e){t.dialogFormVisible=!0}}},[t._v("Add New Music")]),e("el-dialog",{attrs:{title:"Please enter new music information",visible:t.dialogFormVisible},on:{"update:visible":function(e){t.dialogFormVisible=e}}},[e("el-form",{attrs:{model:t.form}},[e("el-form-item",{attrs:{label:"活动名称","label-width":t.formLabelWidth}},[e("el-input",{attrs:{autocomplete:"off"},model:{value:t.form.name,callback:function(e){t.$set(t.form,"name",e)},expression:"form.name"}})],1),e("el-form-item",{attrs:{label:"活动区域","label-width":t.formLabelWidth}},[e("el-select",{attrs:{placeholder:"请选择活动区域"},model:{value:t.form.region,callback:function(e){t.$set(t.form,"region",e)},expression:"form.region"}},[e("el-option",{attrs:{label:"区域一",value:"shanghai"}}),e("el-option",{attrs:{label:"区域二",value:"beijing"}})],1)],1)],1),e("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[e("el-button",{on:{click:function(e){t.dialogFormVisible=!1}}},[t._v("取 消")]),e("el-button",{attrs:{type:"primary"},on:{click:function(e){t.dialogFormVisible=!1}}},[t._v("确 定")])],1)],1)],1),e("div",{staticClass:"el-main"},[e("el-table",{attrs:{data:t.tableData,stripe:"",border:"",height:"550"}},[e("el-table-column",{attrs:{prop:"name",label:"Music Name",width:"140"}}),e("el-table-column",{attrs:{prop:"duration",label:"Music Duration",width:"120"}}),e("el-table-column",{attrs:{prop:"artistsText",label:"Artists Name"}}),e("el-table-column",{attrs:{label:"Operation"},scopedSlots:t._u([{key:"default",fn:function(a){return[e("el-button",{attrs:{type:"primary"},on:{click:function(e){return t.changeMusicState(a.row)}}},[t._v(t._s(t.ifAvailable(a.row.usable)))])]}}])})],1)],1)])},n=[],l=(a("ac6a"),a("8615"),a("ed08")),o={name:"staff-management",data:function(){return{tableData:[],dialogFormVisible:!1,form:{name:"",region:"",date1:"",date2:"",delivery:!1,type:[],resource:"",desc:""},formLabelWidth:"120px"}},mounted:function(){this.init()},methods:{init:function(){this.staffGetAllMusic()},open:function(){var t=this;this.$prompt("请输入邮箱","提示",{confirmButtonText:"Submit",cancelButtonText:"Cancel",inputPattern:/[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,inputErrorMessage:"邮箱格式不正确"}).then((function(e){var a=e.value;t.$message({type:"success",message:"你的邮箱是: "+a})})).catch((function(){t.$message({type:"info",message:"取消输入"})}))},staffGetAllMusic:function(){var t=this;l["newRequest"].get("/music/managerGetAllMusicResource").then((function(e){var a=Object.values(e.data);t.tableData=a.map((function(t){var e=t.seq,a=t.id,i=t.name,n=t.artists,o=t.duration,s=t.durationSecond,r=t.mvId,u=t.img,c=t.albumName,m=t.url,d=t.usable;return Object(l["newCreateSong"])({id:e,oldId:a,name:i,artists:n,artistsText:n,duration:o,durationSecond:s,albumName:c,img:u,mvId:r,url:m,usable:d})})),console.log(t.tableData)}))},changeMusicState:function(t){console.log(t);var e=1-t.usable;l["newRequest"].post("/music/manage_music_usability",{music_id:t.oldId,usability:e}).then((function(a){console.log(a.data),t.usable=e}))},ifAvailable:function(t){return 1===t?"Deactivate":"Activate"}}},s=o,r=(a("d5d2"),a("0c7c")),u=Object(r["a"])(s,i,n,!1,null,null,null);e["default"]=u.exports},8615:function(t,e,a){var i=a("5ca1"),n=a("504c")(!1);i(i.S,"Object",{values:function(t){return n(t)}})},d5d2:function(t,e,a){"use strict";a("4d2d")}}]);