<template>
    <div>
        <div class="search">
            <el-input
                v-model="searchData.searchTarget"
                placeholder="Search"
                prefix-icon="el-icon-search"
                v-on:input="onSearchSongs"
                @keypress.native.enter="onSearchSongs"
            />
            <Toggle
                :reserveDoms="[$refs.input && $refs.input.$el]"
                :show.sync="searchPanelShow"
            >
                <!--  search recommendation and history   -->
                <el-card v-for="(item, index) in this.searchData.searchResult" :key="index" class="box-card">
                    <span>{{ item.name }}</span>
                    <el-button
                        icon="el-icon-video-play"
                        style="float: right"
                        type="primary"
                        @click="updateMusic(item.url)"
                    >Play
                    </el-button>
                </el-card>
            </Toggle>
        </div>
        <audio id="comp-player" ref="music" :src="audio.url" autoplay/>
        <div class="screen-share-control-container">
            <ul>
                <li>
                    <el-button icon="el-icon-video-play" @click="playMusic">Play Music</el-button>
                </li>
                <li>
                    <el-button icon="el-icon-video-pause" @click="pauseMusic">Pause Music</el-button>
                </li>
                <li>
                    <el-button icon="el-icon-refresh" @click="resumeMusic">Resume Music</el-button>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
import Toggle from "@/base/toggle.vue";
import {newRequest} from "@/utils";

export default {
    name: "compMusicPlayer",
    components: {Toggle},
    data() {
        return {
            audio: {
                url: 'https://ipa-012.ucd.ie/music/-wNSFmqhQsU.mp3'
            },
            searchData:{
                searchTarget: '',
                searchResult: ''
            },
            searchPanelShow: false,
        }
    },
    sockets: {
        play_music(data) {
            console.log('socket get play music, data:'+data)
            document.getElementById('comp-player').play()
        },
        pause_music(data) {
            console.log('socket get pause music, data:'+data)
            document.getElementById('comp-player').pause()
        },
        resume_music(data) {
            console.log('socket get resume music, data:'+data)
            document.getElementById('comp-player').currentTime = 0;
            document.getElementById('comp-player').play()
        },
        update_music(data) {
            console.log('socket get update music')
            console.log(data)
            this.audio.url = data.musicUrl
            console.log('this.audio.url:' + this.audio.url)
            document.getElementById('comp-player').src = data.musicUrl
            document.getElementById('comp-player').load()
            document.getElementById('comp-player').play()
        }
    },
    methods: {
        onSearchSongs(){
            newRequest.post(
                '/search/searchMusic',
                {
                    searchContent: this.searchData.searchTarget
                }
            ).then(res=>{
                console.log(res)
                this.searchData.searchResult = res.data
            })
        },
        updateMusic(url){
            this.$socket.emit(
                'update_music',
                {
                    room: this.$cookies.get('chatRoom').room,
                    musicUrl: url
                }
            )
            console.log('socket send update music, url:' + url)
        },
        playMusic() {
            this.$socket.emit(
                'play_music',
                {
                    room: this.$cookies.get('chatRoom').room,
                    musicState: 'play'
                }
            )
            console.log('socket send play music')
        },
        resumeMusic() {
            this.$socket.emit(
                'resume_music',
                {
                    room: this.$cookies.get('chatRoom').room,
                    musicState: 'resume'
                }
            )
            console.log('socket send resume music')
        },
        pauseMusic() {
            this.$socket.emit(
                'pause_music',
                {
                    room: this.$cookies.get('chatRoom').room,
                    musicState: 'pause'
                }
            )
            console.log('socket send pause music')
        },
    }

}
</script>

<style scoped>

</style>