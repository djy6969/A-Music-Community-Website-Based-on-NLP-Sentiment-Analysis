(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-8e06649a"],{"50ea":function(t,e,a){},b2d2:function(t,e,a){"use strict";a.r(e);var i=function(){var t=this,e=t._self._c;return e("div",{staticClass:"container"},[e("el-tag",{attrs:{type:"success",effect:"dark"}},[t._v("For All Musics:")]),e("dv-border-box-12",{staticClass:"border-box",attrs:{id:"capsule-chart"}},[e("dv-capsule-chart",{staticClass:"charts",staticStyle:{height:"400px"},attrs:{config:t.top10Config}})],1),e("dv-border-box-12",{staticClass:"border-box",attrs:{id:"capsule-chart"}},[e("dv-capsule-chart",{staticClass:"charts",staticStyle:{height:"400px"},attrs:{config:t.bottom10Config}})],1),e("dv-border-box-12",{staticClass:"border-box"},[e("dv-charts",{staticStyle:{height:"800px"},attrs:{option:t.positiveAllConfig}})],1),e("dv-border-box-12",{staticClass:"border-box"},[e("dv-charts",{staticStyle:{height:"800px"},attrs:{option:t.negativeAllConfig}})],1),e("el-tag",{attrs:{type:"",effect:"dark"}},[t._v("For a Single Music:")]),e("div",{attrs:{id:"select-area"}},[e("el-select",{attrs:{filterable:"",placeholder:"Please select a music"},on:{change:t.selectMusicItem},model:{value:t.selectMusicValue,callback:function(e){t.selectMusicValue=e},expression:"selectMusicValue"}},t._l(t.selectMusicOptions,(function(t){return e("el-option",{key:t.value,attrs:{label:t.label,value:t.value}})})),1)],1),e("dv-border-box-12",{staticClass:"border-box"},[e("dv-charts",{staticClass:"charts",staticStyle:{height:"600px"},attrs:{option:t.singleCommentConfig}})],1),e("dv-border-box-12",{staticClass:"border-box"},[e("dv-charts",{staticClass:"charts",staticStyle:{height:"600px"},attrs:{option:t.singleHotConfig}})],1),e("dv-border-box-12",{staticClass:"border-box"},[e("dv-charts",{staticClass:"charts",staticStyle:{height:"500px"},attrs:{option:t.singleProportionConfig}})],1)],1)},s=[],o=(a("7f7f"),a("7514"),a("ed08")),n={name:"analysis",data:function(){return{top10Config:{},bottom10Config:{},positiveAllConfig:{},negativeAllConfig:{},selectMusicOptions:[],selectMusicValue:"",musicItem:{},singleCommentConfig:{},singleHotConfig:{},singleProportionConfig:{}}},mounted:function(){this.init()},methods:{init:function(){this.staffGetAllMusicName(),this.staffGetAllHistograms(),this.staffGetAllPies()},staffGetAllMusicName:function(){var t=this;o["newRequest"].get("/visualization/get_music_info").then((function(e){console.log(e.data),t.selectMusicOptions=e.data}))},staffGetAllHistograms:function(){var t=this;o["newRequest"].get("/visualization/column_all_top").then((function(e){console.log(e.data),t.top10Config={data:e.data,showValue:!0}})),o["newRequest"].get("/visualization/column_all_bottom").then((function(e){console.log(e.data),t.bottom10Config={data:e.data,showValue:!0}}))},staffGetAllPies:function(){var t=this;o["newRequest"].get("/visualization/pie_all_positive").then((function(e){console.log(e.data),t.positiveAllConfig={color:["#fb7293"],title:{text:"Music Proportions in Positive Comments"},series:[{type:"pie",data:e.data,insideLabel:{show:!0}}]}})),o["newRequest"].get("/visualization/pie_all_negative").then((function(e){console.log(e.data),t.negativeAllConfig={color:["#fb7293"],title:{text:"Music Proportions in Negative Comments"},series:[{type:"pie",data:e.data,insideLabel:{show:!0}}]}}))},selectMusicItem:function(t){var e=this;this.musicItem=this.selectMusicOptions.find((function(e){return e.value===t})),o["newRequest"].post("/visualization/pie_single",{id:t}).then((function(t){console.log(t.data),e.singleProportionConfig={color:["#fb7293"],title:{text:"Proportion of Different Comments"},series:[{type:"pie",data:t.data,insideLabel:{show:!0}}]}})),o["newRequest"].post("/visualization/line_score",{id:t}).then((function(t){console.log(t.data);var a=t.data;e.singleHotConfig={title:{text:"Music Popularity"},xAxis:{name:"Date and Time",data:a[0].data},yAxis:{name:"Score",data:"value"},series:[{data:a[1].data,type:"line",lineArea:{show:!0},linePoint:{radius:4},label:{show:!0}}]}})),o["newRequest"].post("/visualization/line_sentiment",{id:t}).then((function(t){console.log(t.data);var a=t.data;e.singleCommentConfig={title:{text:"Different Types of Comments for Each Music"},legend:{data:[a[1].name,a[2].name,a[3].name]},xAxis:{name:"Date and Time",data:a[0].data},yAxis:{name:"Number",data:"value"},series:[{name:a[1].name,data:a[1].data,type:"line",linePoint:{radius:4},label:{show:!0},stack:"a",fill:{show:!0}},{name:a[2].name,data:a[2].data,type:"line",linePoint:{radius:4},label:{show:!0},stack:"b",smooth:!0},{name:a[3].name,data:a[3].data,type:"line",linePoint:{radius:4},label:{show:!0},stack:"c",lineStyle:{lineDash:[5,5]}}]}}))}}},l=n,c=(a("e5cd"),a("0c7c")),r=Object(c["a"])(l,i,s,!1,null,null,null);e["default"]=r.exports},e5cd:function(t,e,a){"use strict";a("50ea")}}]);