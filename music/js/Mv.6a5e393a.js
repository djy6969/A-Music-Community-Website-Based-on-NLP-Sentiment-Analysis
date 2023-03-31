(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["Mv"],{2505:function(t,i,a){},5108:function(t,i,a){"use strict";a.r(i);a("7f7f");var e=function(){var t=this,i=t._self._c;return t.$utils.isDef(t.mvDetail.id)?i("div",{staticClass:"mv"},[i("div",{staticClass:"mv-content"},[i("div",{staticClass:"left"},[i("p",{staticClass:"title"},[t._v("mv详情")]),i("div",{staticClass:"player"},[i("VideoPlayer",{ref:"video",attrs:{url:t.mvPlayInfo.url,poster:t.mvDetail.cover}})],1),i("div",{staticClass:"author-wrap"},[i("div",{staticClass:"avatar"},[i("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.$utils.genImgUrl(t.artist.picUrl,120),expression:"$utils.genImgUrl(artist.picUrl, 120)"}]})]),i("p",{staticClass:"author"},[t._v(t._s(t.artist.name))])]),i("p",{staticClass:"name"},[t._v(t._s(t.mvDetail.name))]),i("div",{staticClass:"desc"},[i("span",{staticClass:"date"},[t._v("发布："+t._s(t.$utils.formatDate(t.mvDetail.publishTime,"yyyy-MM-dd")))]),i("span",{staticClass:"count"},[t._v("播放："+t._s(t.mvDetail.playCount)+"次")])]),i("div",{staticClass:"comments"},[i("Comments",{attrs:{id:t.id,type:"mv"}})],1)]),i("div",{staticClass:"right"},[i("p",{staticClass:"title"},[t._v("相关推荐")]),i("div",{staticClass:"simi-mvs"},t._l(t.simiMvs,(function(a){return i("Card",{key:a.id,staticClass:"simi-mv-card",attrs:{desc:"by ".concat(a.artistName),name:a.name},on:{click:function(i){return t.$utils.goMv(a.id)}},scopedSlots:t._u([{key:"img-wrap",fn:function(){return[i("MvCard",{attrs:{duration:a.duration,img:a.cover,playCount:a.playCount}})]},proxy:!0}],null,!0)})})),1)])])]):t._e()},s=[],n=(a("8e6e"),a("456d"),a("ac6a"),a("5df3"),a("3835")),r=(a("96cf"),a("1da1")),c=a("ade3"),o=(a("c5f6"),a("365c")),l=a("ed08"),u=a("e7e6"),v=a("961b"),m=a("6ad1");function d(t,i){var a=Object.keys(t);if(Object.getOwnPropertySymbols){var e=Object.getOwnPropertySymbols(t);i&&(e=e.filter((function(i){return Object.getOwnPropertyDescriptor(t,i).enumerable}))),a.push.apply(a,e)}return a}function p(t){for(var i=1;i<arguments.length;i++){var a=null!=arguments[i]?arguments[i]:{};i%2?d(Object(a),!0).forEach((function(i){Object(c["a"])(t,i,a[i])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(a)):d(Object(a)).forEach((function(i){Object.defineProperty(t,i,Object.getOwnPropertyDescriptor(a,i))}))}return t}var f={mixins:[l["hideMenuMixin"]],props:{id:{type:Number,required:!0}},metaInfo:function(){return{title:this.mvDetail.name}},created:function(){this.init()},data:function(){return{mvDetail:{},mvPlayInfo:{},artist:{},simiMvs:[]}},methods:p({init:function(){var t=Object(r["a"])(regeneratorRuntime.mark((function t(){var i,a,e,s,r,c,l,u=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Promise.all([Object(o["i"])(this.id),Object(o["j"])(this.id),Object(o["r"])(this.id)]);case 2:return i=t.sent,a=Object(n["a"])(i,3),e=a[0].data,s=a[1].data,r=a[2].mvs,t.next=9,Object(o["c"])(e.artistId);case 9:c=t.sent,l=c.artist,this.mvDetail=e,this.mvPlayInfo=s,this.artist=l,this.simiMvs=r,this.$nextTick((function(){var t=u.$refs.video.player;t.on("play",(function(){u.setPlayingState(!1)}))}));case 16:case"end":return t.stop()}}),t,this)})));function i(){return t.apply(this,arguments)}return i}(),goMv:function(t){this.$router.push("/mv/".concat(t))}},Object(u["c"])(["setPlayingState"])),watch:{id:"init"},components:{Comments:v["a"],MvCard:m["a"]}},y=f,h=(a("bec7"),a("0c7c")),b=Object(h["a"])(y,e,s,!1,null,"02228b90",null);i["default"]=b.exports},"5a35":function(t,i,a){"use strict";a("66eb")},"66eb":function(t,i,a){},"6ad1":function(t,i,a){"use strict";a("7f7f");var e=function(){var t=this,i=t._self._c;return i("div",{staticClass:"mv-card",on:{click:t.goMv}},[i("div",{staticClass:"img-wrap"},[i("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.$utils.genImgUrl(t.img,500,260),expression:"$utils.genImgUrl(img, 500, 260)"}]}),t.playCount?i("div",{staticClass:"play-count-wrap"},[i("Icon",{attrs:{type:"play"}}),t._v("\n      "+t._s(t.$utils.formatNumber(t.playCount))+"\n    ")],1):t._e(),i("div",{staticClass:"play-icon-wrap"},[i("PlayIcon",{staticClass:"play-icon",attrs:{size:48}})],1),t.duration?i("div",{staticClass:"duration-wrap"},[t._v("\n      "+t._s(t.$utils.formatTime(t.duration/1e3))+"\n    ")]):t._e()]),t.name?i("p",{staticClass:"name"},[t._v(t._s(t.name))]):t._e(),t.author?i("p",{staticClass:"author"},[t._v(t._s(t.author))]):t._e()])},s=[],n=a("ed08"),r={props:["id","img","duration","playCount","name","author"],methods:{goMv:function(){Object(n["isDef"])(this.id)&&this.$router.push("/mv/".concat(this.id))}}},c=r,o=(a("5a35"),a("0c7c")),l=Object(o["a"])(c,e,s,!1,null,"d51534d2",null);i["a"]=l.exports},bec7:function(t,i,a){"use strict";a("2505")}}]);