<template>
    <div class="invite-container">
        <div class="content">
            <div class="invite-tips">
                You've been invited to a video call
                sdkAppId: {{this.sdkAppId}}
            </div>
            <!-- rtc 房间 -->
            <div class="rtc-container">
        <!-- 进房操作区域 -->
        <div class="control-container">
            <div class="rtc-control-container">
                <el-button
                        class="button"
                        type="primary"
                        size="small" :disabled="isJoining || isJoined" @click="handleJoinRoom">Join Room
                </el-button>

                <el-button
                        class="button"
                        type="primary" size="small" @click="handleLeave">Leave Room
                </el-button>
                <el-button @click="playMusic">Play</el-button>
            </div>
        </div>

        <div class="info-container">

            <!-- 本地流区域 -->
            <div v-if="localStream" class="local-stream-container">
                <!-- 本地流播放区域 -->
                <div id="localStream" class="local-stream-content"></div>
                <!-- 本地流操作栏 -->
                <div v-if="isPlayingLocalStream" class="local-stream-control">
                    <div class="video-control control">
            <span v-if="!isMutedVideo" @click="muteVideo">
              <svg-icon icon-name="video" class="icon-class"></svg-icon>
            </span>
                        <span v-if="isMutedVideo" @click="unmuteVideo">
              <svg-icon icon-name="video-muted" class="icon-class"></svg-icon>
            </span>
                    </div>
                    <div class="audio-control control">
            <span v-if="!isMutedAudio" @click="muteAudio">
              <svg-icon icon-name="audio" class="icon-class"></svg-icon>
            </span>
                        <span v-if="isMutedAudio" @click="unmuteAudio">
              <svg-icon icon-name="audio-muted" class="icon-class"></svg-icon>
            </span>
                    </div>
                </div>
            </div>
        </div>

        <!-- 远端流区域 -->
        <div class="remote-container">
            <div
                    v-for="(item) in remoteStreamList"
                    :key="item.getUserId()"
                    :id="item.getUserId()"
                    class="remote-stream-container">
            </div>
        </div>
    </div>
        </div>
    </div>
</template>

<script>
import rtc from "@/components/listenTogether/mixins/rtc";
import shareRtc from "@/components/listenTogether/mixins/share-rtc";
import AudioMixerPlugin from "rtc-audio-mixer";
let audioSourceA = AudioMixerPlugin.createAudioSource({url: 'https://ipa-012.ucd.ie/music/-wNSFmqhQsU.mp3'});
export default {
    name: 'Invite',
    mixins: [rtc, shareRtc],
    props: {
        type: String,
        sdkAppId: Number,
        secretKey: String,
        userId: String,
        roomId: Number,
        cameraId: String,
        microphoneId: String,
        inviteUserSig: String,
    },
    data() {
        return {
            userSig: '309cda7170d7b1b37b2cc7ae78798511a1f786ec8cc8ea349e4eb50bdfaa23d5',
        };
    },
    computed: {
        isHostMode() {
            return this.type !== 'invite';
        },
        showInviteLink() {
            return this.isHostMode && (this.isJoined || this.isShareJoined) && this.inviteLink;
        },
    },
    components: {
    },
    sockets:{
        play_music(){
            audioSourceA.play()
        },
        pause_music(){
          audioSourceA.pause()
        },
        resume_music(){
            audioSourceA.resume()
        }
    },
    watch: {
        cameraId(val) {
            this.switchDevice('video', val);
        },
        microphoneId(val) {
            this.switchDevice('audio', val);
        },
    },
    methods: {
        pauseMusic(){
            audioSourceA.pause()
        },
        resumeMusic(){
            audioSourceA.resume()
        },
        playMusic(){
            audioSourceA.play()
        },

        // 点击【Join Room】按钮
        async handleJoinRoom() {
            if (!this.sdkAppId || !this.inviteUserSig || !this.userId || !this.roomId) {
                alert('Please reacquire the invitation link');
                return;
            }
            this.userSig = this.inviteUserSig;

            await this.initClient();
            await this.join();
            await this.initLocalStream();
            console.log('initLocalStream')
            // let originAudioTrack = this.localStream.getAudioTrack();
            let mixedAudioTrack = AudioMixerPlugin.mix({sourceList: [audioSourceA]});
            await this.localStream.replaceTrack(mixedAudioTrack)
            audioSourceA.play()
            console.log('audioSourceA.play')
            this.addSuccessLog('mixed https://ipa-012.ucd.ie/music/-wNSFmqhQsU.mp3')
            await this.client.publish(this.localStream);
            this.isPublishing = false;
            this.isPublished = true;
        },

        // 点击【Publish】按钮
        async handlePublish() {
            await this.publish();
        },
        addSuccessLog(log) {
            if (!this.isHostMode) {
                return;
            }
        },

        // 点击【Unpublish】按钮
        async handleUnpublish() {
            await this.unPublish();
        },

        // 点击【Leave Room】按钮
        async handleLeave() {
            await this.leave();
        },

        // 点击【开始屏幕分享】按钮
        async handleStartScreenShare() {
            if (!this.sdkAppId || !this.secretKey) {
                alert('Please enter sdkAppId and secretKey');
                return;
            }
            await this.initShareClient();
            await this.initShareLocalStream();
            await this.handleShareJoin();
            await this.handleSharePublish();
            this.generateInviteLink();
        },

        // 点击【停止屏幕分享按钮】
        async handleStopScreenShare() {
            await this.handleShareUnpublish();
            await this.handleShareLeave();
        },
    },
    mounted() {
        console.log()
    }
};
</script>

<style lang="scss" scoped>
.content {
  width: 80%;
  margin: 0 auto;
  max-width: 1320px;
  padding-top: 30px;

  &.content-mobile {
    width: 100%;
    padding: 30px 16px 20px;
  }

  .invite-tips {
    width: 100%;
    height: 60px;
    color: #084298;
    background-color: #cfe2ff;
    position: relative;
    padding: 1rem 1rem;
    margin-bottom: 1rem;
    border: 1px solid #b6d4fe;
    border-radius: 0.25rem;
  }
}
</style>

