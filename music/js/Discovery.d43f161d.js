(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["Discovery"],{"0347":function(t,e,n){},"1c64":function(t,e,n){},"22f4":function(t,e,n){"use strict";n("0347")},"236e":function(t,e,n){"use strict";n("56b3")},"2fcc":function(t,e,n){"use strict";n("f64d")},"39ed":function(t,e,n){"use strict";n.r(e);var s=function(){var t=this,e=t._self._c;return e("div",{staticClass:"discovery"},[e("div",{staticClass:"discovery-content"},[e("Banner"),e("NewSongs"),e("NewMvs")],1)])},r=[],i=function(){var t=this,e=t._self._c;return e("el-carousel",{staticClass:"banner-carousel",attrs:{interval:4e3,type:"card"}},t._l(t.banners,(function(n){return e("el-carousel-item",{key:n.scm},[e("img",{staticClass:"banner-img",attrs:{src:t.$utils.genImgUrl(n.imageUrl,1e3,400)}})])})),1)},a=[],c=(n("96cf"),n("1da1")),o=n("365c"),u={created:function(){var t=Object(c["a"])(regeneratorRuntime.mark((function t(){var e,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["d"])();case 2:e=t.sent,n=e.banners,this.banners=n;case 5:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),data:function(){return{banners:[]}}},l=u,d=(n("737c"),n("0c7c")),f=Object(d["a"])(l,i,a,!1,null,"4019963e",null),m=f.exports,g=(n("7f7f"),function(){var t=this,e=t._self._c;return t.list.length?e("div",{staticClass:"recommend"},[e("Title",[t._v("Recommended Playlists")]),e("div",{staticClass:"list-wrap"},t._l(t.list,(function(t){return e("PlaylistCard",{key:t.id,attrs:{desc:t.copywriter,id:t.id,img:t.picUrl,name:t.name}})})),1)],1):t._e()}),p=[],v=n("4ead"),h={created:function(){var t=Object(c["a"])(regeneratorRuntime.mark((function t(){var e,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["k"])({limit:10});case 2:e=t.sent,n=e.result,this.list=n;case 5:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),data:function(){return{list:[]}},components:{PlaylistCard:v["a"]}},b=h,y=(n("94b6"),Object(d["a"])(b,g,p,!1,null,"80867dee",null)),w=y.exports,C=function(){var t=this,e=t._self._c;return t.list.length?e("div",{staticClass:"new-songs"},[e("Title",[t._v("The Newest Music")]),e("div",{staticClass:"list-wrap"},t._l(t.chunkedList,(function(n,s){return e("div",{key:s,staticClass:"list"},t._l(n,(function(n,r){return e("SongCard",t._b({key:n.id,staticClass:"song-card",attrs:{order:t.getSongOrder(s,r)},nativeOn:{click:function(e){return t.onClickSong(s,r)}}},"SongCard",t.newNormalizeSong(n),!1))})),1)})),0)],1):t._e()},_=[],O=(n("8e6e"),n("456d"),n("ac6a"),n("8615"),n("ade3")),j=n("e7e6"),S=function(){var t=this,e=t._self._c;return e("div",{staticClass:"song-card"},[e("div",{staticClass:"order-wrap"},[e("span",{staticClass:"order"},[t._v(t._s(t.$utils.pad(t.order)))])]),e("div",{staticClass:"img-wrap"},[e("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.$utils.genImgUrl(t.img,120),expression:"$utils.genImgUrl(img, 120)"}]}),e("PlayIcon",{staticClass:"play-icon"})],1),e("div",{staticClass:"song-content"},[e("p",{staticClass:"song-name"},[t._v(t._s(t.name))]),e("p",{staticClass:"singer"},[t._v(t._s(t.artistsText))])])])},k=[],x={props:["order","name","img","artistsText"]},P=x,I=(n("b796"),Object(d["a"])(P,S,k,!1,null,"6ece8fc2",null)),R=I.exports,N=n("ed08");function z(t,e){var n=Object.keys(t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(t);e&&(s=s.filter((function(e){return Object.getOwnPropertyDescriptor(t,e).enumerable}))),n.push.apply(n,s)}return n}function M(t){for(var e=1;e<arguments.length;e++){var n=null!=arguments[e]?arguments[e]:{};e%2?z(Object(n),!0).forEach((function(e){Object(O["a"])(t,e,n[e])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(n)):z(Object(n)).forEach((function(e){Object.defineProperty(t,e,Object.getOwnPropertyDescriptor(n,e))}))}return t}var T=10,$={created:function(){var t=Object(c["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,this.getNewestSongs();case 2:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}(),data:function(){return{chunkLimit:Math.ceil(T/2),list:[],ifRestart:0}},methods:M(M(M({getSongOrder:function(t,e){return t*this.chunkLimit+e+1},getNewestSongs:function(){var t=this;N["newRequest"].post("/music/getMusicResource",{num:10}).then((function(e){var n=Object.values(e.data);console.log(n),t.list=n}))},normalizeSong:function(t){var e=t.id,n=t.name,s=t.song,r=s.mvid,i=s.artists,a=s.album.blurPicUrl,c=s.duration;return Object(N["createSong"])({id:e,name:n,img:a,artists:i,duration:c,mvId:r})},newNormalizeSong:function(t){var e=t.seq,n=t.id,s=t.name,r=t.mvId,i=t.artists,a=t.img,c=t.duration,o=t.durationSecond,u=t.url;return Object(N["newCreateSong"])({id:e,oldId:n,name:s,img:a,artists:i,artistsText:i,duration:c,durationSecond:o,mvId:r,url:u})},onClickSong:function(t,e){var n=this;clearInterval(this.ifRestart),this.ifRestart=0;var s=this.getSongOrder(t,e)-1,r=this.normalizedSongs[s];this.startSong(r),this.setPlaylist(this.normalizedSongs),this.ifRestart=setInterval((function(){0===n.currentSongTime()?n.startSong(r):(clearInterval(n.ifRestart),n.ifRestart=0)}),3500)}},Object(j["c"])(["setPlaylist","setPlayingState"])),Object(j["d"])(["currentTime"])),Object(j["a"])(["startSong"])),computed:{chunkedList:function(){return[this.list.slice(0,this.chunkLimit),this.list.slice(this.chunkLimit,this.list.length)]},normalizedSongs:function(){var t=this;return this.list.map((function(e){return t.newNormalizeSong(e)}))},currentPlayingSong:function(){return this.currentSong},currentSongTime:function(){return this.currentTime},playingState:function(){return this.playing}},components:{SongCard:R}},U=$,D=(n("236e"),Object(d["a"])(U,C,_,!1,null,"f8256590",null)),L=D.exports,q=function(){var t=this,e=t._self._c;return t.mvs.length?e("div",{staticClass:"new-mvs"},[e("Title",[t._v("Recommended MV")]),e("ul",{staticClass:"list-wrap"},t._l(t.mvs,(function(t){return e("li",{key:t.id,staticClass:"list-item"},[e("MvCard",{attrs:{author:t.artistName,id:t.id,img:t.picUrl,name:t.name,playCount:t.playCount}})],1)})),0)],1):t._e()},B=[],E=n("6ad1"),J={created:function(){this.getMvs()},data:function(){return{mvs:[]}},methods:{getMvs:function(){var t=Object(c["a"])(regeneratorRuntime.mark((function t(){var e,n;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,Object(o["l"])();case 2:e=t.sent,n=e.result,this.mvs=n;case 5:case"end":return t.stop()}}),t,this)})));function e(){return t.apply(this,arguments)}return e}()},components:{MvCard:E["a"]}},V=J,A=(n("41c6"),Object(d["a"])(V,q,B,!1,null,"f9c08f4e",null)),F=A.exports,G={components:{Banner:m,NewPlaylists:w,NewSongs:L,NewMvs:F}},H=G,K=(n("2fcc"),Object(d["a"])(H,s,r,!1,null,"075fd2dc",null));e["default"]=K.exports},"41c6":function(t,e,n){"use strict";n("1c64")},"4ead":function(t,e,n){"use strict";n("7f7f");var s=function(){var t=this,e=t._self._c;return e("div",{staticClass:"playlist-card",on:{click:t.onClickCard}},[e("div",{staticClass:"img-wrap"},[e("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.$utils.genImgUrl(t.img,300),expression:"$utils.genImgUrl(img, 300)"}]}),t.desc?e("div",{staticClass:"desc-wrap"},[e("span",{staticClass:"desc"},[t._v(t._s(t.desc))])]):t._e(),e("PlayIcon",{staticClass:"play-icon",attrs:{size:36}})],1),e("p",{staticClass:"name"},[t._v(t._s(t.name))])])},r=[],i={props:["id","img","name","desc"],methods:{onClickCard:function(){this.$router.push("/playlist/".concat(this.id))}}},a=i,c=(n("22f4"),n("0c7c")),o=Object(c["a"])(a,s,r,!1,null,"5ee4ad8a",null);e["a"]=o.exports},"504c":function(t,e,n){var s=n("9e1e"),r=n("0d58"),i=n("6821"),a=n("52a7").f;t.exports=function(t){return function(e){var n,c=i(e),o=r(c),u=o.length,l=0,d=[];while(u>l)n=o[l++],s&&!a.call(c,n)||d.push(t?[n,c[n]]:c[n]);return d}}},"56b3":function(t,e,n){},"5a35":function(t,e,n){"use strict";n("66eb")},"66eb":function(t,e,n){},"6ad1":function(t,e,n){"use strict";n("7f7f");var s=function(){var t=this,e=t._self._c;return e("div",{staticClass:"mv-card",on:{click:t.goMv}},[e("div",{staticClass:"img-wrap"},[e("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.$utils.genImgUrl(t.img,500,260),expression:"$utils.genImgUrl(img, 500, 260)"}]}),t.playCount?e("div",{staticClass:"play-count-wrap"},[e("Icon",{attrs:{type:"play"}}),t._v("\n      "+t._s(t.$utils.formatNumber(t.playCount))+"\n    ")],1):t._e(),e("div",{staticClass:"play-icon-wrap"},[e("PlayIcon",{staticClass:"play-icon",attrs:{size:48}})],1),t.duration?e("div",{staticClass:"duration-wrap"},[t._v("\n      "+t._s(t.$utils.formatTime(t.duration/1e3))+"\n    ")]):t._e()]),t.name?e("p",{staticClass:"name"},[t._v(t._s(t.name))]):t._e(),t.author?e("p",{staticClass:"author"},[t._v(t._s(t.author))]):t._e()])},r=[],i=n("ed08"),a={props:["id","img","duration","playCount","name","author"],methods:{goMv:function(){Object(i["isDef"])(this.id)&&this.$router.push("/mv/".concat(this.id))}}},c=a,o=(n("5a35"),n("0c7c")),u=Object(o["a"])(c,s,r,!1,null,"d51534d2",null);e["a"]=u.exports},"737c":function(t,e,n){"use strict";n("dc4e")},"7ee5":function(t,e,n){},8615:function(t,e,n){var s=n("5ca1"),r=n("504c")(!1);s(s.S,"Object",{values:function(t){return r(t)}})},"94b6":function(t,e,n){"use strict";n("7ee5")},b796:function(t,e,n){"use strict";n("d25b")},d25b:function(t,e,n){},dc4e:function(t,e,n){},f64d:function(t,e,n){}}]);