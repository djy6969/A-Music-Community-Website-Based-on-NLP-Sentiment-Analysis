(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["Mvs"],{"072d":function(t,a,e){"use strict";e("d44c")},"41fa":function(t,a,e){"use strict";e("dc5b")},"5a35":function(t,a,e){"use strict";e("66eb")},"66eb":function(t,a,e){},"6ad1":function(t,a,e){"use strict";e("7f7f");var s=function(){var t=this,a=t._self._c;return a("div",{staticClass:"mv-card",on:{click:t.goMv}},[a("div",{staticClass:"img-wrap"},[a("img",{directives:[{name:"lazy",rawName:"v-lazy",value:t.$utils.genImgUrl(t.img,500,260),expression:"$utils.genImgUrl(img, 500, 260)"}]}),t.playCount?a("div",{staticClass:"play-count-wrap"},[a("Icon",{attrs:{type:"play"}}),t._v("\n      "+t._s(t.$utils.formatNumber(t.playCount))+"\n    ")],1):t._e(),a("div",{staticClass:"play-icon-wrap"},[a("PlayIcon",{staticClass:"play-icon",attrs:{size:48}})],1),t.duration?a("div",{staticClass:"duration-wrap"},[t._v("\n      "+t._s(t.$utils.formatTime(t.duration/1e3))+"\n    ")]):t._e()]),t.name?a("p",{staticClass:"name"},[t._v(t._s(t.name))]):t._e(),t.author?a("p",{staticClass:"author"},[t._v(t._s(t.author))]):t._e()])},n=[],i=e("ed08"),r={props:["id","img","duration","playCount","name","author"],methods:{goMv:function(){Object(i["isDef"])(this.id)&&this.$router.push("/mv/".concat(this.id))}}},c=r,o=(e("5a35"),e("0c7c")),u=Object(o["a"])(c,s,n,!1,null,"d51534d2",null);a["a"]=u.exports},7651:function(t,a,e){"use strict";e.r(a);e("7f7f");var s=function(){var t=this,a=t._self._c;return a("div",{ref:"page",staticClass:"mvs"},[a("div",{staticClass:"tabs-wrap"},[a("span",{staticClass:"tabs-type"},[t._v("Region:")]),a("Tabs",{staticClass:"tabs",attrs:{tabs:t.areaTabsCN,type:"split"},model:{value:t.activeAreaTabIndex,callback:function(a){t.activeAreaTabIndex=a},expression:"activeAreaTabIndex"}})],1),a("div",{staticClass:"tabs-wrap"},[a("span",{staticClass:"tabs-type"},[t._v("Type:")]),a("Tabs",{staticClass:"tabs",attrs:{tabs:t.typeTabsCN,type:"split"},model:{value:t.activeTypeTabIndex,callback:function(a){t.activeTypeTabIndex=a},expression:"activeTypeTabIndex"}})],1),a("div",{staticClass:"tabs-wrap"},[a("span",{staticClass:"tabs-type"},[t._v("Ranking:")]),a("Tabs",{staticClass:"tabs",attrs:{tabs:t.sortTabsCN,type:"split"},model:{value:t.activeSortTabIndex,callback:function(a){t.activeSortTabIndex=a},expression:"activeSortTabIndex"}})],1),a("WithPagination",{attrs:{getData:t.getAllMvs,getDataParams:t.getDataParams,limit:40,scrollTarget:this.$refs&&this.$refs.page,total:t.mvCount},on:{getDataSuccess:t.onGetMvs}},[a("ul",{staticClass:"list-wrap"},t._l(t.mvs,(function(t){return a("li",{key:t.id,staticClass:"list-item"},[a("MvCard",{attrs:{author:t.artistName,duration:t.duration,id:t.id,img:t.cover,name:t.name,playCount:t.playCount}})],1)})),0)])],1)},n=[],i=e("365c"),r=e("6ad1"),c=e("b2b7"),o=["全部","内地","港台","欧美","日本","韩国"],u=["全部","官方版","原声","现场版","网易出品"],l=["上升最快","最热","最新"],p=["All","China Mainland","China HongKong and Taiwan","Europe and North America","Japan","South Korea"],d=["All","Official","Original Sound","Live","Netease"],b=["The Fastest Rising","The Hottest","The Newest"],g={created:function(){this.areaTabs=o,this.typeTabs=u,this.sortTabs=l,this.areaTabsCN=p,this.typeTabsCN=d,this.sortTabsCN=b,this.getAllMvs=i["b"]},data:function(){return{mvs:[],mvCount:0,activeAreaTabIndex:0,activeTypeTabIndex:0,activeSortTabIndex:0}},methods:{onGetMvs:function(t){var a=t.data,e=t.count;this.mvs=a,e&&(this.mvCount=e)}},computed:{getDataParams:function(){return{area:o[this.activeAreaTabIndex],order:l[this.activeSortTabIndex],type:u[this.activeTypeTabIndex]}}},components:{WithPagination:c["a"],MvCard:r["a"]}},v=g,f=(e("41fa"),e("0c7c")),h=Object(f["a"])(v,s,n,!1,null,"1027e50c",null);a["default"]=h.exports},b2b7:function(t,a,e){"use strict";var s=function(){var t=this,a=t._self._c;return a("div",{staticClass:"with-pagination"},[t._t("default"),a("div",{staticClass:"pagination-wrap"},[a("Pagination",{staticClass:"pagination",attrs:{"current-page":t.currentPage,"page-size":t.limit,total:t.total},on:{"update:currentPage":function(a){t.currentPage=a},"update:current-page":function(a){t.currentPage=a},"current-change":t.onPageChange}})],1)],2)},n=[],i=(e("8e6e"),e("456d"),e("ac6a"),e("8615"),e("ade3")),r=(e("96cf"),e("1da1")),c=(e("c5f6"),e("ed08"));function o(t,a){var e=Object.keys(t);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(t);a&&(s=s.filter((function(a){return Object.getOwnPropertyDescriptor(t,a).enumerable}))),e.push.apply(e,s)}return e}function u(t){for(var a=1;a<arguments.length;a++){var e=null!=arguments[a]?arguments[a]:{};a%2?o(Object(e),!0).forEach((function(a){Object(i["a"])(t,a,e[a])})):Object.getOwnPropertyDescriptors?Object.defineProperties(t,Object.getOwnPropertyDescriptors(e)):o(Object(e)).forEach((function(a){Object.defineProperty(t,a,Object.getOwnPropertyDescriptor(e,a))}))}return t}var l={props:{getData:{type:Function},getDataParams:{type:Object,default:function(){return{}}},limit:{type:Number,default:10},scrollTarget:{type:HTMLElement},total:{type:Number,default:0},keywords:{type:String}},created:function(){this.onPageChange()},data:function(){return{currentPage:1}},methods:{onPageChange:function(){var t=Object(r["a"])(regeneratorRuntime.mark((function t(){var a,e=this;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:if(t.prev=0,"undefined"!==typeof this.keywords){t.next=9;break}return t.next=4,this.getData(u({limit:this.limit,offset:Object(c["getPageOffset"])(this.currentPage,this.limit)},this.getDataParams));case 4:a=t.sent,this.$emit("getDataSuccess",a),this.scrollTarget&&Object(c["scrollInto"])(this.scrollTarget),t.next=10;break;case 9:c["newRequest"].post("/search/searchMusic",{searchContent:this.keywords}).then((function(t){e.$emit("getDataSuccess",Object.values(t.data)),e.scrollTarget&&Object(c["scrollInto"])(e.scrollTarget)}));case 10:t.next=15;break;case 12:t.prev=12,t.t0=t["catch"](0),this.$emit("getDataError",t.t0);case 15:case"end":return t.stop()}}),t,this,[[0,12]])})));function a(){return t.apply(this,arguments)}return a}()},watch:{getDataParams:{deep:!0,handler:function(){this.currentPage=1,this.onPageChange()}}}},p=l,d=(e("072d"),e("0c7c")),b=Object(d["a"])(p,s,n,!1,null,"5c19c762",null);a["a"]=b.exports},d44c:function(t,a,e){},dc5b:function(t,a,e){}}]);