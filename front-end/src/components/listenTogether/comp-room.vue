<!--
 * @Description: 房间显示
 * @Date: 2022-03-16 17:40:28
 * @LastEditTime: 2022-03-29 16:13:06
-->
<template>
    <div class="rtc-container">
        <!-- 进房操作区域 -->
        <div class="control-container">
            <div class="rtc-control-container">
                <el-button
                    class="button"
                    type="primary"
                    size="small" :disabled="isJoining || isJoined" @click="handleJoinRoom">Listen Together
                </el-button>
            </div>
            <div v-if="isHostMode" class="screen-share-control-container">
                 <div class="search">
                    <el-input
                        @click.native="onClickInput"
                        @keypress.native.enter="onEnterPress"
                        placeholder="Search"
                        prefix-icon="el-icon-search"
                        ref="input"
                        v-model.trim="searchKeyword"
                    />
                    <Toggle
                        :reserveDoms="[$refs.input && $refs.input.$el]"
                        :show.sync="searchPanelShow"
                    >
                        <!--  search recommendation and history   -->

                    </Toggle>
                </div>
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
</template>

<script>
import rtc from './mixins/rtc.js';
import shareRtc from './mixins/share-rtc.js';
import * as LibGenerateTestUserSigFn from '@/utils/lib-generate-test-usersig.min.js';

import {importHack} from './mixins/helper.js'
import Toggle from "@/base/toggle.vue";
import {newRequest} from "@/utils";


// let audioSourceA = AudioMixerPlugin.createAudioSource({url: 'https://ipa-012.ucd.ie/music/-wNSFmqhQsU.mp3'});
export default {
    name: 'compRoom',
    components: {Toggle},
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
            searchPanelShow: false,
            logList: [],
            inviteLink: '',
            showCopiedTip: false,
            audioSourceA: '',
            searchContent: ''
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
    watch: {
        cameraId(val) {
            this.switchDevice('video', val);
        },
        microphoneId(val) {
            this.switchDevice('audio', val);
        },
    },
    methods: {
        onEnterPress(){
            newRequest.post(
                '/search/searchMusic',
                {
                    searchContent: this.searchContent
                }
            ).then(res=>{
                console.log(res)
            })
        },
        pauseMusic() {
            // audioSourceA.pause()
            this.$socket.emit(
                'pause_music',
                {
                    room: this.$cookies.get('chatRoom').room,
                    musicState: 'pause'
                }
            )
        },
        resumeMusic() {
            // audioSourceA.resume()
            this.$socket.emit(
                'resume_music',
                {
                    room: this.$cookies.get('chatRoom').room,
                    musicState: 'resume'
                }
            )
        },
        playMusic() {
            // audioSourceA.play()
            this.$socket.emit(
                'play_music',
                {
                    room: this.$cookies.get('chatRoom').room,
                    musicState: 'play'
                }
            )
        },
        generateInviteLink() {
            if (!this.isHostMode) {
                return;
            }
            // eslint-disable-next-line no-unused-vars
            const {sdkAppId, secretKey, roomId} = this;
            const inviteUserId = `user_${parseInt(Math.random() * 100000000, 10)}`;
            const userSigGenerator = new (importHack(LibGenerateTestUserSigFn, 'LibGenerateTestUserSig'))(this.sdkAppId, this.secretKey, 604800);
            const inviteUserSig = userSigGenerator.genTestUserSig(inviteUserId);
            this.$socket.emit(
                'invite',
                {
                    secretKey: secretKey,
                    sdkAppId: sdkAppId,
                    inviteUserId: inviteUserId,
                    userSig: inviteUserSig,
                    userId: inviteUserId,
                    roomId: roomId,
                    room: this.$cookies.get('chatRoom').room,
                }
            )
        },

        // 点击【Join Room】按钮
        async handleJoinRoom() {
            if (this.isHostMode) {
                if (!this.sdkAppId || !this.secretKey) {
                    alert('Please enter sdkAppId and secretKey');
                    return;
                }
                if (!this.userId || !this.roomId) {
                    alert('Please enter userId and roomId');
                    return;
                }
                const userSigGenerator = new (importHack(LibGenerateTestUserSigFn, 'LibGenerateTestUserSig'))(this.sdkAppId, this.secretKey, 604800);
                this.userSig = userSigGenerator.genTestUserSig(this.userId);
            } else {
                if (!this.sdkAppId || !this.inviteUserSig || !this.userId || !this.roomId) {
                    alert('Please reacquire the invitation link');
                    return;
                }
                this.userSig = this.inviteUserSig;
            }
            await this.initClient();
            await this.join();
            await this.initLocalStream();

            // let originAudioTrack = this.localStream.getAudioTrack();
            let mixedAudioTrack = AudioMixerPlugin.mix({sourceList: [audioSourceA]});
            await this.localStream.replaceTrack(mixedAudioTrack)
            this.addSuccessLog('mixed https://ipa-012.ucd.ie/music/-wNSFmqhQsU.mp3')
            await this.client.publish(this.localStream);
            this.isPublishing = false;
            this.isPublished = true;
            this.generateInviteLink();
        },

        // 点击【Publish】按钮
        async handlePublish() {
            await this.publish();
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

        // 显示成功的 Log
        addSuccessLog(log) {
            if (!this.isHostMode) {
                return;
            }
            // this.logList.push({
            //     type: 'success',
            //     log,
            // });
            // const {scrollHeight} = this.$refs.logContainer;
            // this.$refs.logContainer.scrollTop = scrollHeight;
        },

        // 显示失败的 Log
        addFailedLog(log) {
            if (!this.isHostMode) {
                return;
            }
            this.logList.push({
                type: 'failed',
                log,
            });
        },

        reportFailedEvent(name, error, type = 'rtc') {
            console.log('111')
        },
    },
};
</script>

<style lang="scss" scoped>
.rtc-container {
  .label {
    margin: 14px 0 6px;
    text-align: left;
    font-weight: bold;
  }

  .control-container {
    text-align: left;
    margin-bottom: 10px;

    div:not(:nth-last-child(1)) {
      margin-bottom: 10px;
    }

    .button:not(:first-child) {
      margin-left: 2px;
    }
  }

  .invite-link-container {
    width: 100%;
    color: #084298;
    background-color: #cfe2ff;
    position: relative;
    padding: 10px 16px;
    margin-bottom: 16px;
    border: 1px solid #b6d4fe;
    border-radius: 0.25rem;

    .invite-input {
      margin-top: 10px;
    }

    .invite-btn {
      display: flex;
      cursor: pointer;
    }
  }

  .info-container {
    width: 100%;
    display: flex;
    justify-content: space-between;

    .log-container {
      flex-grow: 1;
      border: 1px solid #dddddd;
      height: 360px;
      padding: 10px;
      margin-right: 16px;
      overflow-y: scroll;

      .log-label {
        margin: 0 0 6px;
        font-weight: bold;
      }

      .log-state {
        display: inline-block;
        margin-right: 6px;
      }

      > div {
        font-size: 12px;
      }
    }

    .local-stream-container {
      width: 480px;
      height: 360px;
      position: relative;
      flex-shrink: 0;

      .local-stream-content {
        width: 100%;
        height: 100%;
      }

      .local-stream-control {
        width: 100%;
        height: 30px;
        position: absolute;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.3);
        display: flex;
        justify-content: flex-end;
        align-items: center;
        padding: 0 10px;

        .control {
          margin-left: 10px;
        }

        .icon-class {
          color: #fff;
          cursor: pointer;
          width: 20px;
          height: 20px;
        }
      }
    }
  }

  .info-container-mobile {
    display: block;

    .log-container {
      margin-right: 0;
    }

    .local-stream-container {
      width: 320px;
      height: 240px;
      margin-top: 10px;
    }
  }

  .remote-container {
    width: 100%;
    margin-top: 10px;
    display: flex;
    flex-wrap: wrap;

    .remote-stream-container {
      width: 320px;
      height: 240px;
      margin: 0 10px 10px 0;
    }
  }
}
</style>

<i18n>
{
  "en": {
    "Operation": "Operation",
    "Join Room": "Join Room",
    "Publish": "Publish",
    "Unpublish": "Unpublish",
    "Leave Room": "Leave Room",
    "Start Screen Share": "Start Screen Share",
    "Stop Screen Share": "Stop Screen Share",
    "Please enter sdkAppId and secretKey": "Please enter sdkAppId and secretKey",
    "Please enter userId and roomId": "Please enter userId and roomId",
    "Please reacquire the invitation link": "Please reacquire the invitation link!"
  },
  "zh": {
    "Operation": "操作",
    "Join Room": "进入房间",
    "Publish": "发布流",
    "Unpublish": "取消发布流",
    "Leave Room": "离开房间",
    "Start Screen Share": "开始共享屏幕",
    "Stop Screen Share": "停止共享屏幕",
    "Please enter sdkAppId and secretKey": "请输入 sdkAppId 和 secretKey",
    "Please enter userId and roomId": "请输入 userId 和 roomId",
    "Please reacquire the invitation link": "请重新获取邀请链接！"
  }
}
</i18n>
