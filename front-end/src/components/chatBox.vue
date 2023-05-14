<template>
    <div class="container">
        <!--chatBox-->
        <div>
            <div v-for="(item, index) in chatData" :key="index" class="chatBox">
                <div v-if="item.actor === 'system'">
                    <div class="message message-system">
                        <el-avatar src="https://ipa-012.ucd.ie/image/friendly-chatbot.jpg"/>
                        <p style="text-align: justify">{{ item.data }}
                            <br>
                        </p>
                    </div>
<!--                    {{ item.time }}-->
                </div>
                <div v-if="item.actor === 'user'">
                    <div class="message message-user">
                        <p style="text-align: justify">
                            {{ item.data }}
                            <br>
                        </p>
                        <el-avatar :src="userAvatarUrl"/>
                    </div>
<!--/*                    <p style="justify-content: flex-end">{{ item.time }}</p>*/-->
                </div>
            </div>
        </div>
        <!--chat input-->
        <div class="chatBox_input">
            <el-input v-model="inputData"/>
            <el-button @click="chatRequest">Enter</el-button>
        </div>
    </div>
</template>

<script>

import {newRequest} from "@/utils";

export default {
    name: "chatBox",
    props: {
        name: {
            type: String,
            required: true
        },
        artists: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            musicName: this.name,
            userAvatarUrl: this.$cookies.get('auth').avatarUrl,
            inputData: '',
            chatData: [
                {
                    actor: 'system',
                    data: 'Hello! I\'m ChatAI 😊. You can ask me any questions about this song such as: Tell me about the singer of this song.',
                    time: this.getNowTime()
                },
            ]
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
        chatRequest() {
            this.chatData.push({
                actor: 'user',
                data: this.inputData,
                time: this.getNowTime()
            })
            newRequest.post(
                '/chat/get_chat_response',
                {
                    user_input: this.inputData,
                    song_name: this.name,
                    artist_name: this.artists
                }
            ).then(res => {
                if (res.code === 200) {
                    console.log(res)
                    this.inputData = ''
                }
                this.chatData.push({
                    actor: 'system',
                    data: res.data,
                    time: this.getNowTime()
                })
              this.inputData = ''
            })
        }
    },
    watch: {
        musicName: {
            handler() {
                this.chatData = [{
                    actor: 'system',
                    data: 'Hello! I\'m ChatAI 😊. You can ask me any questions about this song such as: Tell me about the singer of this song.',
                    time: this.getNowTime()
                },]
            },
            immediate: true
        }
    }
}
</script>

<style scoped>
.container {
    position: relative;
    max-width: 100%;
    height: 80%;
    background: #fff;
    box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.06);
    display: flex;
    flex-direction: column;
    //overflow: auto;
}

.chatBox {
    position: relative;
    width: 100%;
    padding: 10px;
}


.chatBox_input {
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 10%;
    background: #f0f0f0;
    justify-content: space-between;
    align-items: center;
    display: flex;
    flex-direction: row;
}

.message {
    position: relative;
    display: flex;
    //width: 100%;
    //margin: 5px 0;
}

.message-system {
    justify-content: flex-start;
    display: flex;
}

.message-user {
    justify-content: flex-end;
    //float: right;
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
</style>