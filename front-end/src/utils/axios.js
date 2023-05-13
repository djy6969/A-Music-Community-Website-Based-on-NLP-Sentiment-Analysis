import axios from 'axios'
import { Loading } from 'element-ui'
import { confirm } from '@/base/confirm'
import store from '@/store'

// const BASE_URL = 'https://mu-api.yuk0.com/'
const BASE_URL = 'https://netease-cloud-music-api-lake-eta.vercel.app/'

// Request instance without global loading
export const requestWithoutLoading = createBaseInstance()
// Request instance with global loading
// We need to handle loading before processing the handleResponse result of the request
// We also need to insert the loading interceptor inside
export const request = createBaseInstance()
mixinLoading(request.interceptors)

// A generic axios instance: for netease api
function createBaseInstance() {
  const instance = axios.create({
    baseURL: BASE_URL,
  })

  instance.interceptors.response.use(handleResponse, handleError)
  return instance
}

// Encapsulation for baseURL
export const newRequest = createNewInstance()
mixinLoading(newRequest.interceptors)

// a new generic axios instance: for our back-end
function createNewInstance() {
  const instance = axios.create({
    // baseURL: 'http://127.0.0.1:5000/api/',
    baseURL: 'https://ipa-012.ucd.ie/api/',
  })

  instance.interceptors.response.use(handleResponse, handleError)
  return instance
}

function handleError(e) {
  confirm(e.message, 'Something went wrong')
  throw e
}

function handleResponse(response) {
  return response.data
}

let loading
let loadingCount = 0
const SET_AXIOS_LOADING = 'global/setAxiosLoading'
function mixinLoading(interceptors) {
  interceptors.request.use(loadingRequestInterceptor)
  interceptors.response.use(
    loadingResponseInterceptor,
    loadingResponseErrorInterceptor
  )

  function loadingRequestInterceptor(config) {
    if (!loading) {
      loading = Loading.service({
        target: 'body',
        background: 'transparent',
        text: 'Loading',
      })
      store.commit(SET_AXIOS_LOADING, true)
    }
    loadingCount++

    return config
  }

  function handleResponseLoading() {
    loadingCount--
    if (loadingCount === 0) {
      loading.close()
      loading = null
      store.commit(SET_AXIOS_LOADING, false)
    }
  }

  function loadingResponseInterceptor(response) {
    handleResponseLoading()
    return response
  }

  function loadingResponseErrorInterceptor(e) {
    handleResponseLoading()
    throw e
  }
}
