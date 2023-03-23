import Vue from 'vue'
import Router from 'vue-router'

const Discovery = () => import(/* webpackChunkName: "Discovery" */ '@/page/discovery')
const PlaylistDetail = () => import(/* webpackChunkName: "PlaylistDetail" */ '@/page/playlist-detail')
const Playlists = () => import(/* webpackChunkName: "Playlists" */ '@/page/playlists')
const Songs = () => import(/* webpackChunkName: "Songs" */ '@/page/songs')

const User = () => import(/* webpackChunkName: "User" */ '@/page/user')
const Blogs = () => import(/* webpackChunkName: "Blogs" */ '@/page/blogs')
const Search = () => import(/* webpackChunkName: "Search" */ '@/page/search')
const SearchSongs = () => import(/* webpackChunkName: "SearchSongs" */ '@/page/search/songs')
const SearchPlaylists = () => import(/* webpackChunkName: "SearchPlaylists" */ '@/page/search/playlists')
const SearchMvs = () => import(/* webpackChunkName: "SearchMvs" */ '@/page/search/mvs')
const Staff = () => import('@/page/staff/staff')
const Mvs = () => import(/* webpackChunkName: "Mvs" */ '@/page/mvs')
const Mv = () => import(/* webpackChunkName: "Mv" */ '@/page/mv')

// 内容需要居中的页面
export const layoutCenterNames = ['discovery', 'playlists', 'songs', 'mvs']

// 需要显示在侧边栏菜单的页面
export const menuRoutes = [
  {
    path: '/discovery',
    name: 'discovery',
    component: Discovery,
    meta: {
      title: 'Find music',
      icon: 'music',
    },
  },
  // {
  //   path: '/playlists',
  //   name: 'playlists',
  //   component: Playlists,
  //   meta: {
  //     title: 'Recommended music lists',
  //     icon: 'playlist-menu',
  //   },
  // },
  {
    path: '/songs',
    name: 'songs',
    component: Songs,
    meta: {
      title: 'The newest music',
      icon: 'yinyue',
    },
  },
  // {
  //   path: '/mvs',
  //   name: 'mvs',
  //   component: Mvs,
  //   meta: {
  //     title: 'The newest MV',
  //     icon: 'mv',
  //   },
  // },
  {
    path: '/community',
    name: 'community',
    component: Blogs,
    meta: {
      title: 'Community',
      // element icon
      icon: 'new el-icon-s-grid'
    }
  }
]

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/discovery',
    },
    {
      path: '/playlist/:id',
      name: 'playlist',
      component: PlaylistDetail,
    },
    {
      path: '/search/:keywords',
      name: 'search',
      component: Search,
      props: true,
      children: [
        {
          path: '/',
          redirect: 'songs',
        },
        {
          path: 'songs',
          name: 'searchSongs',
          component: SearchSongs,
        },
        {
          path: 'playlists',
          name: 'searchPlaylists',
          component: SearchPlaylists,
        },
        {
          path: 'mvs',
          name: 'searchMvs',
          component: SearchMvs,
        },
      ],
    },
    {
      path: '/mv/:id',
      name: 'mv',
      component: Mv,
      props: (route) =>  ({id: +route.params.id}),
    },
    ...menuRoutes,
    {
      path: '/staff',
      name: 'staff',
      component: Staff
    },
    {
      path: '/user',
      name: 'user',
      component: User
    }
  ],
})
