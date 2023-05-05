<template>
    <div class="container">
        <div class="leftSide">
            <div class="search_chat">
                <div style="display: flex">
                    <input placeholder="Add New Friend" type="text" v-model="friendId">
                    <el-button @click="addFriend">Add</el-button>
                </div>
            </div>
            <!--ChatList-->

            <chat-list
                    v-for="(item, index) in this.friendList"
                    :key="index"
                    :id="item"
                    @click.native="startChatroom(item)"
            />
            <listen-together
                v-if="!ifInvited"
            />
            <invite
                v-if="ifInvited"
                :sdkAppId="Number(invitedData.sdkAppId)"
                :inviteUserSig="invitedData.userSig"
                :userId="invitedData.userId"
                :roomId="invitedData.roomId"
                :secretKey = invitedData.secretKey
            />
        </div>

        <div class="rightSide" style="width: 80%;">
            <div class="header">
                <div class="imgText">
                    <div class="userimg">
                        <el-avatar :src="friendData.avatarUrl"/>
                    </div>
                    <h4>{{ this.friendData.friendName }}</h4>
                </div>
            </div>
            <!--chatbox-->
            <div class="chatBox">
                <div v-for="(item, index) in chatData" :key="index">
                    <div v-if="item.actor === 'user'" class="message my_message">
                        <p>{{ item.content }}<br><span>{{ item.time }}</span></p>
                    </div>
                    <div v-if="item.actor === 'friend'" class="message frnd_message">
                        <p>{{ item.content }}<br><span>{{ item.time }}</span></p>
                    </div>
                </div>
            </div>

            <!--chat input-->
            <div class="chatbox_input">
                <div class="instrument">
                    <el-button type="primary" @click="leaveChatroom">Leave</el-button>
                </div>
                <div style="display: flex">
                    <input v-model="sendData" type="text">
                    <el-button
                        class="button"
                        @click="sendMessage"
                        type="primary"
                    >Send</el-button>
                </div>

            </div>
            <!--       listen together     -->

        </div>

    </div>
</template>

<script>
import {newRequest} from "@/utils";
import ChatList from "./chatList.vue";
import ListenTogether from "@/page/chat/listenTogether.vue";
import Invite from "@/page/chat/Invite.vue";

export default {
    name: "index",
    components: { Invite, ListenTogether, ChatList},
    data() {
        return {
            friendId: 0,
            friendList: [],
            friendData: {
                friendName: 'None',
                id: '',
                avatarUrl: ''
            },
            chatData: [],
            sendData: '',
            listenMode: '',
            ifInvited: false,
            invitedData:{
                sdkAppId: '',
                userSig: '',
                userId: '',
                roomId: 0,
                secretKey: ''
            }
        }
    },
    sockets: {
        //查看socket是否渲染成功
        connect() {
            console.log("链接成功");
        },
        //检测socket断开链接
        disconnect() {
            console.log("断开链接");
        },
        // 重新链接
        reconnect() {
            console.log("重新链接");
        },
        //客户端接收后台传输的socket事件
        kline: function (msg) {
            console.log(msg);
            //然后记性你的一系列操作
        },
        data(res){
            console.log(res, '5555555555')
        },
        send_msg(data){
            console.log(this.chatData)
            if (data.username !== this.$cookies.get('auth').username){
                this.chatData.push({
                    actor: 'friend',
                    content: data.message,
                    time: this.getNowTime()
                    })}},
        invite(data){
            console.log(data)
            this.invitedData.sdkAppId = data.sdkAppId
            this.invitedData.userSig = data.userSig
            this.invitedData.userId = data.userId
            this.invitedData.roomId = data.roomId
            this.invitedData.secretKey = data.secretKey
            this.ifInvited = true
            console.log(this.invitedData)
        }
    },
    methods: {
        getNowTime() {
            let now = new Date(Date.now()),
                y = now.getFullYear(),
                m = now.getMonth() + 1,
                d = now.getDate();
            return y + "-" + (m < 10 ? "0" + m : m) + "-" + (d < 10 ? "0" + d : d) + " " + now.toTimeString().substr(0, 8);
        },
        startChatroom(id) {
            newRequest.post(
                '/account/get_user_info',
                {
                    user_id: id
                }
            ).then(res => {
                this.friendData.id = id
                this.friendData.friendName = res.data.nickname
                this.friendData.avatarUrl = res.data.head_protrait
                newRequest.post(
                    '/chat/add_chatroom',
                    {
                        user_id: this.$cookies.get('auth').userid,
                        friend_id: this.friendData.id
                    }
                ).then(res => {
                    console.log(res)
                    if (res.code === 200) {
                        this.$message.success(res.msg)
                        this.$cookies.set(
                            'chatRoom',
                            {
                                room: res.data.chatroom_id,
                                id: res.data.id
                            }
                        )
                        this.$socket.emit(
                            'join',
                            {
                                username: this.$cookies.get('auth').username,
                                room: this.$cookies.get('chatRoom').room
                            }
                        )
                        console.log('socket join')
                    } else {
                        this.$message.error('Something Wrong! Try Again!')
                    }
                })
            })
        },
        addFriend() {
            newRequest.post(
                '/friend/addFriend',
                {
                    user_id: this.$cookies.get('auth').userid,
                    friend_id: this.friendId
                }
            ).then(res => {
                if (res.code === 200) {
                    this.$message({
                        message: 'Add new Friend Success!',
                        type: 'success'
                    })
                    this.friendId = 0
                }
            })
        },
        getFriends() {
            newRequest.post(
                '/friend/getFriends',
                {
                    user_id: this.$cookies.get('auth').userid,
                }
            ).then(res => {
                if (res.code === 200) {
                    this.friendList = res.data
                    console.log(this.friendList)
                }
            })
        },
        checkAllChatroom() {
            newRequest.post(
                '/chat/check_all_chatroom',
                {
                    user_id: this.$cookies.get('auth').userid
                }
            ).then(res => {
                console.log(res)
            })
        },
        sendMessage() {
            this.$socket.emit(
                'send_msg',
                {
                    username: this.$cookies.get('auth').username,
                    room: this.$cookies.get('chatRoom').room,
                    message: this.sendData
                }, (res)=>{
                console.log(res)
            })
            this.chatData.push(
                {
                    actor: 'user',
                    content: this.sendData,
                    time: this.getNowTime()
                }
            )
            this.sendData = ''
        },
        leaveChatroom(){
            this.$socket.emit(
                'leave',
                {
                    username: this.$cookies.get('auth').username,
                    room: this.$cookies.get('chatRoom').room
                }
            )
        }
    },
    mounted() {
        this.getFriends()
        this.checkAllChatroom()
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com css2?family-Open+Sans:wght@300;400;00;600;700&display=swap');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Open Sans', sans-serif;
}

body {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(#009688 0%, #009688 130px, #d9dbd5 130px, #d9dbd5 100%)
}

.container {
    position: relative;
    width: 1396px;
    max-width: 100%;
    height: calc(100vh - 40px);
    background: #fff;
    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.06);
    display: flex;
}

.container .leftSide {
    position: relative;
    flex: 30%;
    background: #fff;
    border-right: 1px solid rgba(0, 0, 0, 0.2);
}

.container .rightside {
    position: relative;
    flex: 70%;
    background: #e5ddd5;
}

.container .rightside::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    opacity: 0.06;
}

.header {
    position: fixed;
    width: 100%;
    height: 60px;
    background: #ededed;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
}

.userimg {
    position: relative;
    width: 40px;
    height: 40px;
    overflow: hidden;
    border-radius: 50%;
    cursor: pointer;
}

.cover {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.nav_icons {
    display: flex;
}

.nav_icons li {
    display: flex;
    list-style: none;
    cursor: pointer;
    color: #51585c;
    font-size: 1.5em;
    margin-left: 22px;
}

.search_chat {
    position: relative;
    width: 100%;
    height: 50px;
    background: #f6f6f6;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 15px;
}

.search_chat div {
    width: 100%;
}

.search_chat div input {
    width: 100%;
    outline: none;
    border: none;
    background: #fff;
    padding: 6px;
    height: 38px;
    border-radius: 30px;
    font-size: 14px;
    padding-left: 40px;
}

.search_chat div input::placeholder {
    color: #bbb;
}

.search_chat div img {
    position: absolute;
    left: 30px;
    top: 14px;
    font-size: 1.5em;
}


.message_p {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.message_p p {
    color: #aaa;
    display: -webkit-box;
    font-size: 0.9em;
    overflow: hidden;
    text-overflow: ellipsis;
}

.message_p b {
    background-color: red;
    color: #fff;
    min-width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.75em;
}

.imgText {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

.imgText h4 {
    font-weight: 500;
    line-height: 1.2em;
    margin-left: 15px;
}

.imgText h4 span {
    font-size: 0.8em;
    color: #555;
}

.chatBox {
    position: relative;
    width: 80%;
    height: 80%;
    padding: 50px;
    overflow-y: auto;
}

.message {
    position: relative;
    display: flex;
    width: 100%;
    margin: 5px 0;
}

.message p {
    position: relative;
    right: 0;
    text-align: right;
    max-width: 65%;
    padding: 12px;
    background: #dcf8c6;
    border-radius: 10px;
    font-size: 0.9em;
}

.message p::before {
    content: '';
    position: absolute;
    top: 0;
    right: -12px;
    width: 20px;
    height: 20px;
    background: linear-gradient(135deg, #dcf8c6 0%, #dcf8c6 50%, transparent 50%, transparent);
}

.message p span {
    display: block;
    margin-top: 5px;
    font-size: 0.85em;
    opacity: 0.5;
}

.my_message {
    justify-content: flex-end;
}

.frnd_message {
    justify-content: flex-start;
}

.frnd_message p {
    background: #fff;
    text-align: left;
}

.message.frnd_message p::before {
    content: '';
    position: absolute;
    top: 0;
    left: -12px;
    width: 20px;
    height: 20px;
    background: linear-gradient(225deg, #fff 0%, #fff 50%, transparent 50%, transparent);
}

.chatbox_input {
    position: fixed;
    width: 60%;
    height: 15%;
    background: #f0f0f0;
    padding: 15px;
    bottom: 5%;
    justify-content: space-between;
    align-items: center;
}

.chatbox_input input {
    position: relative;
    width: 90%;
    margin: 0 20px;
    padding: 10px 20px;
    border: none;
    outline: none;
    border-radius: 30px;
    font-size: 1em;
}
</style>