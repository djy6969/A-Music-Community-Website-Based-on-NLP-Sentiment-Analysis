<template>
    <div class="chatlist">
        <div class="block active" >
            <div class="imgbx">
                <el-avatar :src="friendInfo.avatar"/>
            </div>
            <div class="details">
                <div class="listHead">
                    <h4>{{ friendInfo.nickname }}</h4>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {newRequest} from "@/utils";

export default {
    name: "chatList",
    props: ["id"],
    data() {
        return {
            friendInfo: {
                nickname: '',
                avatar: ''
            }
        }
    },
    methods: {
        loadFriendInfo() {
            newRequest.post(
                '/account/get_user_info',
                {
                    user_id: this.id
                }
            ).then(res => {
                if (res.code === 200) {
                    this.friendInfo.nickname = res.data.nickname
                    this.friendInfo.avatar = res.data.head_protrait
                }
            })
        },
        chatWithFriend() {
            newRequest.post(
                '/chat/add_chatroom',
                {
                    user_id: this.$cookies.get('auth').userid,
                    friend_id: this.id
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
                    this.$emit('transfer', this.friendInfo.nickname)
                } else {
                    this.$message.error('Something Wrong! Try Again!')
                }
            })
        },
    },
    mounted() {
        this.loadFriendInfo()
    }
}
</script>

<style scoped>
.chatlist {
    position: relative;
    overflow-y: auto;
}

.chatlist .block {
    position: relative;
    width: 100%;
    display: flex;
    align-items: center;
    padding: 15px;
    border-bottom: 1px solid rgba(0, 0, 0, 0.06);
}

.chatlist .block.active {
    background: #ebebeb;
}

.chatlist .block:hover {
    background: #f5f5f5;
}

.chatlist .block .imgbx {
    position: relative;
    min-width: 45px;
    height: 45px;
    overflow: hidden;
    border-radius: 50%;
    margin-right: 10px;
}

.chatlist .block .details {
    position: relative;
    width: 100%;
}

.chatlist .block .details .listHead {
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
}

.chatlist .block .details .listHead h4 {
    font-size: 1.1em;
    font-weight: 600;
    color: #111;
}

.chatlist .block .details .listHead .time {
    font-size: 0.75em;
    color: #aaa;
}

.chatlist .block .details .listHead .time {
    color: #111;
}
</style>