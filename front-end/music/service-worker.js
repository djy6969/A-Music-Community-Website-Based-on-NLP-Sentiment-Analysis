if(!self.define){const e=e=>{"require"!==e&&(e+=".js");let s=Promise.resolve();return c[e]||(s=new Promise(async s=>{if("document"in self){const c=document.createElement("script");c.src=e,document.head.appendChild(c),c.onload=s}else importScripts(e),s()})),s.then(()=>{if(!c[e])throw new Error(`Module ${e} didn’t register its module`);return c[e]})},s=(s,c)=>{Promise.all(s.map(e)).then(e=>c(1===e.length?e[0]:e))},c={require:Promise.resolve(s)};self.define=(s,r,i)=>{c[s]||(c[s]=Promise.resolve().then(()=>{let c={};const a={uri:location.origin+s.slice(1)};return Promise.all(r.map(s=>{switch(s){case"exports":return c;case"module":return a;default:return e(s)}})).then(e=>{const s=i(...e);return c.default||(c.default=s),c})}))}}define("./service-worker.js",["./workbox-b4c2a21b"],(function(e){"use strict";e.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"/css/Discovery.28dfb622.css",revision:"d6ccdb3aa8d6c6a9ee638cd17d3a8c04"},{url:"/css/Mv.fad850d5.css",revision:"b40f9bea7b0d2808fb345dcd2d35d269"},{url:"/css/Mvs.81583490.css",revision:"e29a0f6cc6210bd5d7dc41d2e332d698"},{url:"/css/PlaylistDetail.e5c0ad93.css",revision:"47b1abf2280e379c7dee8dac03f84340"},{url:"/css/Playlists.d57dbcf4.css",revision:"acd4b1f5546a35bce2e7b580268f43c3"},{url:"/css/Search.1f275ae2.css",revision:"b065fd3b862f2fedea17b48b5c12b3b2"},{url:"/css/SearchMvs.d944f820.css",revision:"b477992fc51de6bfeca8207cc99dab5e"},{url:"/css/SearchPlaylists.ac7d41bb.css",revision:"4069ac7297280988ce9b775552901592"},{url:"/css/SearchSongs.b3177a33.css",revision:"c8e26c0abf989b8f2ddd6f0bb07e3dac"},{url:"/css/Songs.767cc30c.css",revision:"d1ce4363d73f7e4c6883d953e1e031d5"},{url:"/css/app.914ad87f.css",revision:"ff99ed559a324c93eac99ec9b824bf83"},{url:"/css/chunk-vendors.73beaac3.css",revision:"af0f0b1614c3e12bf17bc57f6b4cd16f"},{url:"/favicon.ico",revision:"fb0bfa066d55c810f2239addad12a06b"},{url:"/fonts/element-icons.535877f5.woff",revision:"535877f50039c0cb49a6196a5b7517cd"},{url:"/fonts/element-icons.732389de.ttf",revision:"732389ded34cb9c52dd88271f1345af9"},{url:"/img/play-bar.e5a7a142.png",revision:"e5a7a1420384639f27927dd0b5e64edb"},{url:"/index.html",revision:"125248cbe6c2e996ef74927e6531a666"},{url:"/js/Discovery.7133cb3d.js",revision:"f9e7f0c96b4cd425e6ffc823e7c44e05"},{url:"/js/Mv.44fe2329.js",revision:"55fbed73b32e8ff3becc137302346679"},{url:"/js/Mvs.7a3d1396.js",revision:"9b7e7df98c0146662173555deefcd9db"},{url:"/js/PlaylistDetail.78c01725.js",revision:"a984a4c97d998c4fac9e8cae7111eda8"},{url:"/js/Playlists.5b6f4f6b.js",revision:"96fe625117489c48e26df6ebd6b51abe"},{url:"/js/Search.a04d812d.js",revision:"83a8ad9e015c84e31722d13e333a692b"},{url:"/js/SearchMvs.fd45b359.js",revision:"a8891965e9f4227b57e8a33275adb47b"},{url:"/js/SearchPlaylists.bec70b71.js",revision:"251e76d5a6eb65e4aecf9fa87ae4093a"},{url:"/js/SearchSongs.f426dc91.js",revision:"4a0e1f2ceafda9dc1a6dac43b0b6f62b"},{url:"/js/Songs.df62af6b.js",revision:"98496097640b2ac3576e1507bf520df2"},{url:"/js/app.a7257ca0.js",revision:"e9240b8cd95356fac78b80ea7ef5d604"},{url:"/js/chunk-vendors.68d2ab0b.js",revision:"be697923cebe97248548edd86e20da03"}],{})}));
