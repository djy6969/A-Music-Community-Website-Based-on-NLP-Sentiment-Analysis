if(!self.define){const s=s=>{"require"!==s&&(s+=".js");let e=Promise.resolve();return c[s]||(e=new Promise(async e=>{if("document"in self){const c=document.createElement("script");c.src=s,document.head.appendChild(c),c.onload=e}else importScripts(s),e()})),e.then(()=>{if(!c[s])throw new Error(`Module ${s} didn’t register its module`);return c[s]})},e=(e,c)=>{Promise.all(e.map(s)).then(s=>c(1===s.length?s[0]:s))},c={require:Promise.resolve(e)};self.define=(e,a,i)=>{c[e]||(c[e]=Promise.resolve().then(()=>{let c={};const f={uri:location.origin+e.slice(1)};return Promise.all(a.map(e=>{switch(e){case"exports":return c;case"module":return f;default:return s(e)}})).then(s=>{const e=i(...s);return c.default||(c.default=e),c})}))}}define("./service-worker.js",["./workbox-b4c2a21b"],(function(s){"use strict";s.skipWaiting(),s.clientsClaim(),s.precacheAndRoute([{url:"/css/Blogs.0a7bac69.css",revision:"93ee07c270130c84933be15aae2c2a36"},{url:"/css/Discovery.083fd268.css",revision:"f840a2c944ce57e313135b6b6bded190"},{url:"/css/Mv.fad850d5.css",revision:"b40f9bea7b0d2808fb345dcd2d35d269"},{url:"/css/Mvs.81e6ad1d.css",revision:"cb12fc61c646be373ac6a37ee99de845"},{url:"/css/PlaylistDetail.e5c0ad93.css",revision:"47b1abf2280e379c7dee8dac03f84340"},{url:"/css/Playlists.d57dbcf4.css",revision:"acd4b1f5546a35bce2e7b580268f43c3"},{url:"/css/Search.d6bf9ba3.css",revision:"956cc5749cbe17f319ed88553018cb3e"},{url:"/css/SearchMvs.020994f3.css",revision:"b9d4a3460968961fbc5b64fc0097b125"},{url:"/css/SearchPlaylists.ba3a3dc3.css",revision:"f0cf433d183be2385666f3dcba20aa2f"},{url:"/css/SearchSongs.05416f87.css",revision:"04df95610c8204c698ba58ba5a8c296e"},{url:"/css/Songs.2897f5b7.css",revision:"d1ce4363d73f7e4c6883d953e1e031d5"},{url:"/css/User.d2e9f4a4.css",revision:"2ea09661cf2b098312c4e6a3232125fc"},{url:"/css/app.27177559.css",revision:"674ce9c177477115beb323ce5a65e224"},{url:"/css/chunk-34f09bbf.bd99c0ee.css",revision:"7c7c7bb20b3a4556ebc1a594f5021124"},{url:"/css/chunk-3c831644.0c93a684.css",revision:"fce78707d8c9202ea57307b1e5ff5360"},{url:"/css/chunk-4b477df4.767cc30c.css",revision:"d1ce4363d73f7e4c6883d953e1e031d5"},{url:"/css/chunk-8e06649a.bd7b7bef.css",revision:"ed2b633eb8a8336c235fcf95728e41f2"},{url:"/css/chunk-vendors.1d75dee6.css",revision:"8e66815dad00112a0955b3d87880242a"},{url:"/favicon.ico",revision:"fb0bfa066d55c810f2239addad12a06b"},{url:"/fonts/element-icons.535877f5.woff",revision:"535877f50039c0cb49a6196a5b7517cd"},{url:"/fonts/element-icons.732389de.ttf",revision:"732389ded34cb9c52dd88271f1345af9"},{url:"/img/play-bar.e5a7a142.png",revision:"e5a7a1420384639f27927dd0b5e64edb"},{url:"/index.html",revision:"3e506fa562d81d39871ab94be94f18ca"},{url:"/js/Blogs.5002b892.js",revision:"435e635b5223f6971f104c84ead182c7"},{url:"/js/Discovery.2578bf00.js",revision:"c743bc92a283c5e7a012398448c8c36d"},{url:"/js/Mv.c47f745b.js",revision:"df6b0089ef38ed7221af3e73321a2429"},{url:"/js/Mvs.c64890bb.js",revision:"1c77a00aad333cb500e02a4e03ee05f7"},{url:"/js/PlaylistDetail.cab2ef61.js",revision:"13423ff0b0e9d4c4b5018361ae8d880a"},{url:"/js/Playlists.fbd4ca55.js",revision:"7dc5e6220c79083a8d899f42aa82e86f"},{url:"/js/Search.9a751f2d.js",revision:"38417461761abe3f3c44755328f2b3d6"},{url:"/js/SearchMvs.cbdc2e9b.js",revision:"ce52a9aa998f507ee949019625fc8d08"},{url:"/js/SearchPlaylists.732a5496.js",revision:"77a8f2890955f7e0a1ae333ade36c9b7"},{url:"/js/SearchSongs.a44ac5f5.js",revision:"bc43fc9ce366277cfc4646776c9058e1"},{url:"/js/Songs.17882258.js",revision:"8469d1c48e8a4252ca08dae5bfc6145e"},{url:"/js/User.479509e8.js",revision:"ee19ad97c39463bc824593efd74da17b"},{url:"/js/app.eeff1b2d.js",revision:"71197aa49b27d4716e29565aaa0caadb"},{url:"/js/chunk-2d0c1006.91aca5ed.js",revision:"8d0a4071486617011ed97fced3954bc5"},{url:"/js/chunk-34f09bbf.82a93c39.js",revision:"fdee95ee4df51aece08d203815e49f60"},{url:"/js/chunk-3c831644.a4fbf492.js",revision:"38bc92259f6cf47eb97fbfbf82bc1210"},{url:"/js/chunk-4b477df4.5b5957d7.js",revision:"3748eef89fc1c0d840701d4d4f82af1d"},{url:"/js/chunk-8e06649a.6f00c23f.js",revision:"332c178ee768b96115a448f71d227133"},{url:"/static/fontawesome/css/all.css",revision:"55a54f958c00ab3123d151720e46c3d8"},{url:"/static/fontawesome/css/all.min.css",revision:"ded1c367363e8b20bdc6a19b8350a737"},{url:"/static/fontawesome/css/brands.css",revision:"4233f057e8cf9765cfda5a0ec73ff94d"},{url:"/static/fontawesome/css/brands.min.css",revision:"db8644805501909c3a9eabc5ea9cd601"},{url:"/static/fontawesome/css/fontawesome.css",revision:"ab0a19a5435ddb85b67f08153aa27ee8"},{url:"/static/fontawesome/css/fontawesome.min.css",revision:"e2313ac29f4514d18516bb15c1d79aae"},{url:"/static/fontawesome/css/regular.css",revision:"b2bf71aad69fbd4aab3242f80544f968"},{url:"/static/fontawesome/css/regular.min.css",revision:"40535b5c9c6681123dfe445736d402a4"},{url:"/static/fontawesome/css/solid.css",revision:"6b1e826a3e0545f777c7770ce41f87b2"},{url:"/static/fontawesome/css/solid.min.css",revision:"ace20fde18fdfe21c87be34ba8c325bb"},{url:"/static/fontawesome/css/svg-with-js.css",revision:"75a5621a71c1f3b511e7cd33d4e0a19c"},{url:"/static/fontawesome/css/svg-with-js.min.css",revision:"541c1fbef048fabc6fe1ec58c3472104"},{url:"/static/fontawesome/css/v4-font-face.css",revision:"c93227fd02873b40267f972bf717ef63"},{url:"/static/fontawesome/css/v4-font-face.min.css",revision:"799f759492c014579d063cc24dca8079"},{url:"/static/fontawesome/css/v4-shims.css",revision:"39476e99835ec79d718080ba95b8afc3"},{url:"/static/fontawesome/css/v4-shims.min.css",revision:"0e111e42b92aa32f0847263dfaadbc6a"},{url:"/static/fontawesome/css/v5-font-face.css",revision:"0e86830243abcc53f4c1a69e886fe25e"},{url:"/static/fontawesome/css/v5-font-face.min.css",revision:"8061d392d2bbc32fa5ab95a1fbf9df22"},{url:"/static/fontawesome/webfonts/fa-brands-400.ttf",revision:"0ab3921d9b80975c5597432ab59f5d0a"},{url:"/static/fontawesome/webfonts/fa-brands-400.woff2",revision:"8b0ddedbb27cbc9971c8667caa8a0cc1"},{url:"/static/fontawesome/webfonts/fa-regular-400.ttf",revision:"20206738b2bffb741b00200d5d3d6d20"},{url:"/static/fontawesome/webfonts/fa-regular-400.woff2",revision:"61f30b79daf5b31f0d254a31fba66158"},{url:"/static/fontawesome/webfonts/fa-solid-900.ttf",revision:"e2ceb83946c9e5fc7eab24453a03bffb"},{url:"/static/fontawesome/webfonts/fa-solid-900.woff2",revision:"c64278386c2bbb5e293e11b94ca2f6d1"},{url:"/static/fontawesome/webfonts/fa-v4compatibility.ttf",revision:"d20cedd7e254d4b58b721b6995ca52b4"},{url:"/static/fontawesome/webfonts/fa-v4compatibility.woff2",revision:"4bc58bc16bb05a05d3a47a4f7e143b75"},{url:"/static/js/socket.io.js",revision:"34d04bc6ee3c5759374a2d1b5403950f"}],{})}));
