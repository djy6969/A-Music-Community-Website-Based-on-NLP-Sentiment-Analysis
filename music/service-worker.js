if(!self.define){const e=e=>{"require"!==e&&(e+=".js");let s=Promise.resolve();return c[e]||(s=new Promise(async s=>{if("document"in self){const c=document.createElement("script");c.src=e,document.head.appendChild(c),c.onload=s}else importScripts(e),s()})),s.then(()=>{if(!c[e])throw new Error(`Module ${e} didn’t register its module`);return c[e]})},s=(s,c)=>{Promise.all(s.map(e)).then(e=>c(1===e.length?e[0]:e))},c={require:Promise.resolve(s)};self.define=(s,r,a)=>{c[s]||(c[s]=Promise.resolve().then(()=>{let c={};const i={uri:location.origin+s.slice(1)};return Promise.all(r.map(s=>{switch(s){case"exports":return c;case"module":return i;default:return e(s)}})).then(e=>{const s=a(...e);return c.default||(c.default=s),c})}))}}define("./service-worker.js",["./workbox-b4c2a21b"],(function(e){"use strict";e.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"/css/Blogs.0a7bac69.css",revision:"93ee07c270130c84933be15aae2c2a36"},{url:"/css/Discovery.7feafdd4.css",revision:"406946596287b09c0accbbaeae40825a"},{url:"/css/Mv.fad850d5.css",revision:"b40f9bea7b0d2808fb345dcd2d35d269"},{url:"/css/Mvs.184d582d.css",revision:"faab9c7f8fa966cbc7fcea920d82ae65"},{url:"/css/PlaylistDetail.e5c0ad93.css",revision:"47b1abf2280e379c7dee8dac03f84340"},{url:"/css/Playlists.d57dbcf4.css",revision:"acd4b1f5546a35bce2e7b580268f43c3"},{url:"/css/Search.d6bf9ba3.css",revision:"956cc5749cbe17f319ed88553018cb3e"},{url:"/css/SearchMvs.82dab3f8.css",revision:"678696692dd4d957a632a6fd4f8f2cbe"},{url:"/css/SearchPlaylists.224d88e7.css",revision:"09a654c0cc9629020ea213c781a52194"},{url:"/css/SearchSongs.e00a876c.css",revision:"61594cbafffcb667b228c6d7852e29ad"},{url:"/css/Songs.2897f5b7.css",revision:"d1ce4363d73f7e4c6883d953e1e031d5"},{url:"/css/User.d2e9f4a4.css",revision:"2ea09661cf2b098312c4e6a3232125fc"},{url:"/css/app.7b22a05b.css",revision:"f9a569e56afdb461ce5ee5ebe1de52ae"},{url:"/css/chunk-ba69ece0.767cc30c.css",revision:"d1ce4363d73f7e4c6883d953e1e031d5"},{url:"/css/chunk-vendors.2f0ee5a1.css",revision:"ab754fd8e4495b19ee1ca83874460f75"},{url:"/favicon.ico",revision:"fb0bfa066d55c810f2239addad12a06b"},{url:"/fonts/element-icons.535877f5.woff",revision:"535877f50039c0cb49a6196a5b7517cd"},{url:"/fonts/element-icons.732389de.ttf",revision:"732389ded34cb9c52dd88271f1345af9"},{url:"/img/play-bar.e5a7a142.png",revision:"e5a7a1420384639f27927dd0b5e64edb"},{url:"/index.html",revision:"607a8568de66453535ad0f02d2fc82ac"},{url:"/js/Blogs.cd334c0d.js",revision:"435e635b5223f6971f104c84ead182c7"},{url:"/js/Discovery.d43f161d.js",revision:"c136423b1c76ce18f25b3e6504ebc0e1"},{url:"/js/Mv.6a5e393a.js",revision:"a74bc4a9910eddf24bc9f9e0e8b7661a"},{url:"/js/Mvs.3c1e9200.js",revision:"336f708838c45e04ebb933246e17b0fd"},{url:"/js/PlaylistDetail.1c083f5b.js",revision:"0a1074a799ba4599dfc41935212f8935"},{url:"/js/Playlists.fe645d3b.js",revision:"b24b91a09e128d07c1cd068155ef2e7c"},{url:"/js/Search.8aa3cca1.js",revision:"38417461761abe3f3c44755328f2b3d6"},{url:"/js/SearchMvs.408b1531.js",revision:"7944a4260811ee50175c7bf6b69bfad1"},{url:"/js/SearchPlaylists.203783f8.js",revision:"ed89564807b5775ad300431fdc2a2cb8"},{url:"/js/SearchSongs.d7a33a76.js",revision:"13473aac4f8d7411d8c948ad45af12e1"},{url:"/js/Songs.7fdf1fbd.js",revision:"28341d3f770a4ef2e0a00a7150507678"},{url:"/js/User.9e5d1b9b.js",revision:"ee19ad97c39463bc824593efd74da17b"},{url:"/js/app.c7986e71.js",revision:"c909227a8b528c8dfd39109ad0738c7e"},{url:"/js/chunk-2d0c1006.5c1d33e4.js",revision:"8d0a4071486617011ed97fced3954bc5"},{url:"/js/chunk-ba69ece0.93ffec11.js",revision:"7a175675b020858c297a79420a928b6b"},{url:"/js/chunk-vendors.9c4f9a41.js",revision:"f324a37c1bfa22f547adf5201163b42a"}],{})}));
