import Vue from 'vue'
import Router from 'vue-router'
import storage from 'good-storage'

const Discovery = () => import(/* webpackChunkName: "Discovery" */ '@/page/discovery')
const PlaylistDetail = () => import(/* webpackChunkName: "PlaylistDetail" */ '@/page/playlist-detail')
const UserFavorites = () => import(/* webpackChunkName: "UserFavorites" */ '@/page/favorites')
const Chatroom = () => import(/* webpackChunkName: "Chatroom" */ '@/page/chat')
const Playlists = () => import(/* webpackChunkName: "Playlists" */ '@/page/playlists')
const Songs = () => import(/* webpackChunkName: "Songs" */ '@/page/songs')
const MusicRecommendation = () => import(/* webpackChunkName: "Songs" */ '@/page/songs/recommendation')
const User = () => import(/* webpackChunkName: "User" */ '@/page/user')
const Blogs = () => import(/* webpackChunkName: "Blogs" */ '@/page/blogs')
const Search = () => import(/* webpackChunkName: "Search" */ '@/page/search')
const SearchSongs = () => import(/* webpackChunkName: "SearchSongs" */ '@/page/search/songs')
const SearchPlaylists = () => import(/* webpackChunkName: "SearchPlaylists" */ '@/page/search/playlists')
const SearchMvs = () => import(/* webpackChunkName: "SearchMvs" */ '@/page/search/mvs')
const Staff = () => import(/* webpackChunkName: "Staff" */ '@/page/staff/staff')
const StaffAnalysis = () => import(/* webpackChunkName: "StaffAnalysis" */ '@/page/staff/analysis')
const StaffManagement = () => import(/* webpackChunkName: "StaffManagement" */ '@/page/staff/management')
const Mvs = () => import(/* webpackChunkName: "Mvs" */ '@/page/mvs')
const Mv = () => import(/* webpackChunkName: "Mv" */ '@/page/mv')

function getCookie(key) {
    const cookieArr = document.cookie.split(';')
    //[a=100, b=200, c=300]
    let value = ''
    cookieArr.forEach(item => {
        if (item.split('=')[0].trim() === key) {
            value = item.split('=')[1]
        }
    })
    return value
}

// 内容需要居中的页面
export const layoutCenterNames = ['discovery', 'playlists', 'songs', 'mvs']

// 需要显示在侧边栏菜单的页面
export const menuRoutes = [
  {
    path: '/discovery',
    name: 'discovery',
    component: Discovery,
    meta: {
      title: 'Find Music',
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
      title: 'The Newest Music',
      icon: 'yinyue',
    },
  },
  {
    path: '/recommendation',
    name: 'recommendation',
    component: MusicRecommendation,
    meta: {
      title: 'Music Recommendation',
      icon: 'yinyue',
    },
  },
  {
    path: '/mvs',
    name: 'mvs',
    component: Mvs,
    meta: {
      title: 'The Newest MV',
      icon: 'mv',
    },
  },
  {
    path: '/community',
    name: 'community',
    component: Blogs,
    meta: {
      title: 'Community',
      // element icon
      icon: 'new el-icon-s-grid'
    }
  },

]

if (getCookie('auth') !== '') {
  // logged in
  menuRoutes.push(
      {
        path: '/favorites',
        name: 'userFavorites',
        component: UserFavorites,
        meta: {
          title: 'User Favorites',
          icon: 'playlist-menu',
        }
      }
  )
  if (storage.get("userRole", 0) === 2) {
    menuRoutes.push(
        {
          path: '/staff-analysis',
          name: 'staffAnalysis',
          component: StaffAnalysis,
          meta: {
            title: 'Staff Analysis',
            icon: 'fontawesome fa-solid fa-chart-bar',
            // icon: 'fontawesome fa-solid fa-magnifying-glass-chart',
          }
        }
    )
    menuRoutes.push(
        {
          path: '/staff-management',
          name: 'staffManagement',
          component: StaffManagement,
          meta: {
            title: 'Staff Management Music',
            icon: 'new el-icon-s-tools',
          }
        }
    )
  }

}

Vue.use(Router)

export default new Router({
  mode: 'hash',
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
    },
    {
      path: '*', // 重定向页面地址
      redirect: '/'
    },
    {
      path: '/chat',
      name: 'Chat',
      component: Chatroom
    }
  ],
})


